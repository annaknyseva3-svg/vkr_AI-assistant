"""
RAG-компонент: поиск релевантных фрагментов в FAISS.
"""
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from app.config import Config

class Retriever:
    def __init__(self):
        self.embedder = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        self.index = None
        self.chunks = []
        self.metadata = []
        self.is_loaded = False
    
    def load_index(self, index_path, chunks_path):
        """Загрузка индекса и чанков из файлов"""
        self.index = faiss.read_index(f"{index_path}/faiss.index")
        with open(f"{chunks_path}/chunks.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.chunks = data['chunks']
            self.metadata = data['metadata']
        self.is_loaded = True
    
    def retrieve(self, query, k=Config.TOP_K, threshold=Config.SIMILARITY_THRESHOLD):
        """Поиск релевантных фрагментов по запросу"""
        if not self.is_loaded:
            return []
        
        query_vec = self.embedder.encode([query], normalize_embeddings=True)
        distances, indices = self.index.search(query_vec.astype(np.float32), k)
        
        results = []
        for i, idx in enumerate(indices[0]):
            if idx == -1:
                continue
            score = float(distances[0][i])
            if score >= threshold:
                results.append({
                    'text': self.chunks[idx],
                    'score': score,
                    'source': self.metadata[idx].get('source', 'unknown'),
                    'title': self.metadata[idx].get('title', '')
                })
        return results
