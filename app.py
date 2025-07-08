import streamlit as st
import tempfile
import os
from typing import List, Dict
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

from pdf_utils import extract_paragraphs_from_pdf
from vector_db import build_vector_db, search_similar_paragraphs
from llm_utils import ask_llm
from ui_utils import render_footer

# --- CONFIG ---
EMBEDDING_MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'
CHROMA_COLLECTION_NAME = 'company_docs'

# --- ENV ---
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# --- CACHING ---
@st.cache_resource(show_spinner=False)
def get_embedder():
    return SentenceTransformer(EMBEDDING_MODEL_NAME)

@st.cache_resource(show_spinner=False)
def get_chroma_client():
    return chromadb.Client(Settings(anonymized_telemetry=False))

# --- STREAMLIT UI ---
st.set_page_config(page_title="Şirket Belgeleri RAG", layout="wide")
st.title("Şirket Belgeleri RAG Asistanı")
st.markdown('<div style="font-size:18px; color:#666; margin-bottom:18px;">Şirket dokümanlarınızdan hızlı, güvenilir ve kaynaklı yanıtlar alın.</div>', unsafe_allow_html=True)

st.sidebar.header("PDF Belgeleri Yükle")
uploaded_files = st.sidebar.file_uploader("PDF Dosyalarını seçin", type=["pdf"], accept_multiple_files=True)

# --- SORU GÖNDERME BUTONU ---
question = st.text_input("Sorunuzu yazın:")
submit = st.button("Soruyu Gönder")

if uploaded_files and api_key:
    st.info("Belgeleriniz yükleniyor, lütfen bekleyin...")
    all_paragraphs = []
    file_map = {}
    for file in uploaded_files:
        paragraphs = extract_paragraphs_from_pdf(file)
        all_paragraphs.extend(paragraphs)
        for i, para in enumerate(paragraphs):
            file_map[f"para_{len(file_map)}"] = (file.name, para)
    embedder = get_embedder()
    chroma_client = get_chroma_client()
    collection = build_vector_db(all_paragraphs, embedder, chroma_client)
    st.success("Belgeleriniz başarıyla yüklendi!")

    if question and submit:
        top_k = 5  # Kaç kaynak kullanılacağını sabitliyoruz
        results = search_similar_paragraphs(question, embedder, collection, top_k=top_k)
        # Paragrafları numaralandır
        context = "\n\n".join([f"[{i+1}] {doc}" for i, (_, doc) in enumerate(results)])
        with st.spinner("Yanıt alınıyor..."):
            try:
                answer = ask_llm(context, question, api_key)
                st.markdown(f"### Yanıt\n{answer}")
                # Cevaptaki kullanılan kaynak numaralarını bul
                import re
                used_nums = set(int(n) for n in re.findall(r'\[(\d+)\]', answer))
                with st.expander("Kullanılan Kaynaklar"):
                    for i, (pid, doc) in enumerate(results):
                        if (i+1) in used_nums:
                            fname, para = file_map.get(pid, ("Bilinmiyor", doc))
                            st.markdown(f"**[{i+1}] {fname}:** {para}")
            except Exception as e:
                st.error(f"Yanıt alınamadı: {e}")
elif not api_key:
    st.warning("API anahtarı bulunamadı. Lütfen .env dosyanıza OPENROUTER_API_KEY ekleyin.")
else:
    st.info("Lütfen PDF dosyalarını yükleyin.")

# --- FOOTER ---
render_footer() 