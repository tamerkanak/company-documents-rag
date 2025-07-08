from typing import List

def build_vector_db(paragraphs: List[str], embedder, chroma_client):
    EMBEDDING_MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'
    CHROMA_COLLECTION_NAME = 'company_docs'
    embeddings = embedder.encode(paragraphs, show_progress_bar=True)
    embeddings = embeddings.tolist()
    if CHROMA_COLLECTION_NAME in [c.name for c in chroma_client.list_collections()]:
        chroma_client.delete_collection(CHROMA_COLLECTION_NAME)
    collection = chroma_client.create_collection(CHROMA_COLLECTION_NAME)
    ids = [f"para_{i}" for i in range(len(paragraphs))]
    collection.add(documents=paragraphs, embeddings=embeddings, ids=ids)
    return collection

def search_similar_paragraphs(question: str, embedder, collection, top_k=5):
    q_emb = embedder.encode([question])[0]
    q_emb = q_emb.tolist()
    results = collection.query(query_embeddings=[q_emb], n_results=top_k)
    docs = results['documents'][0]
    ids = results['ids'][0]
    return list(zip(ids, docs)) 