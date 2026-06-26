"""
Индексация чанков в FAISS.
"""
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

def index_faiss(kb_path, index_path):
    """Создание FAISS-индекса из чанков"""
    with open(f"{kb_path}/chunks.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
        chunks = data['chunks']
    
    embedder = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    embeddings = embedder.encode(chunks, normalize_embeddings=True)
    
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings.astype(np.float32))
    
    os.makedirs(index_path, exist_ok=True)
    faiss.write_index(index, f"{index_path}/faiss.index")
    
    print(f"Индекс создан: {index.ntotal} векторов")

if __name__ == '__main__':
    index_faiss('./data/knowledge_base', './data/faiss_index')
