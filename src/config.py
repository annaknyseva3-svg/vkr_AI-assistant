"""
Конфигурация приложения.
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_PATH = os.getenv('MODEL_PATH', './models/rugpt3')
    KNOWLEDGE_BASE_PATH = os.getenv('KNOWLEDGE_BASE_PATH', './data/knowledge_base')
    FAISS_INDEX_PATH = os.getenv('FAISS_INDEX_PATH', './data/faiss_index')
    DB_PATH = os.getenv('DB_PATH', './data/proposals.db')
    
    # Параметры генерации
    MAX_NEW_TOKENS = 512
    TEMPERATURE = 0.7
    TOP_P = 0.9
    REPETITION_PENALTY = 1.1
    
    # RAG-параметры
    TOP_K = 5
    SIMILARITY_THRESHOLD = 0.75
    CHUNK_SIZE = 300
    CHUNK_OVERLAP = 50
