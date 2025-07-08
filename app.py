from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, session, jsonify
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from pdf_utils import extract_paragraphs_from_pdf
from vector_db import build_vector_db, search_similar_paragraphs
from llm_utils import ask_llm

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Geliştirici için örnek
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Global değişkenler (örnek, daha sonra session ile iyileştirilebilir)
all_paragraphs = []
file_map = {}
collection = None
embedder = None
chroma_client = None

@app.route('/', methods=['GET'])
def index():
    last_question = session.get('last_question')
    answer = session.get('answer')
    session['last_question'] = None
    session['answer'] = None
    return render_template('index.html', last_question=last_question, answer=answer)

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    global all_paragraphs, file_map, collection, embedder, chroma_client
    files = request.files.getlist('pdfs')
    all_paragraphs = []
    file_map = {}
    for file in files:
        if not file or not file.filename:
            continue
        filename = secure_filename(file.filename or "")
        if not filename:
            continue
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        paragraphs = extract_paragraphs_from_pdf(filepath)
        all_paragraphs.extend(paragraphs)
        for i, para in enumerate(paragraphs):
            file_map[f"para_{len(file_map)}"] = (filename, para)
    from sentence_transformers import SentenceTransformer
    import chromadb
    from chromadb.config import Settings
    embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    chroma_client = chromadb.Client(Settings(anonymized_telemetry=False))
    collection = build_vector_db(all_paragraphs, embedder, chroma_client)
    return jsonify({'success': True, 'message': 'Belgeler başarıyla yüklendi!'})

@app.route('/ask_question', methods=['POST'])
def ask_question():
    global all_paragraphs, file_map, collection, embedder, chroma_client
    api_key = os.getenv("OPENROUTER_API_KEY")
    question = request.form.get('question')
    last_question = question
    answer = None
    used_sources = []
    if collection and embedder and question and api_key:
        top_k = 5
        results = search_similar_paragraphs(question, embedder, collection, top_k=top_k)
        context = "\n\n".join([f"[{i+1}] {doc}" for i, (_, doc) in enumerate(results)])
        try:
            answer = ask_llm(context, question, api_key)
            import re
            used_nums = set(int(n) for n in re.findall(r'\[(\d+)\]', answer))
            for i, (pid, doc) in enumerate(results):
                if (i+1) in used_nums:
                    fname, para = file_map.get(pid, ("Bilinmiyor", doc))
                    used_sources.append((i+1, fname, para))
            if used_sources:
                answer += "<br><br><b>Kullanılan Kaynaklar:</b><ul>" + ''.join([f'<li>[{idx}] {fname}: {para}</li>' for idx, fname, para in used_sources]) + "</ul>"
        except Exception as e:
            return jsonify({'success': False, 'error': f'Yanıt alınamadı: {e}'})
    session['last_question'] = last_question
    session['answer'] = answer
    return jsonify({'success': True, 'question': last_question, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True) 