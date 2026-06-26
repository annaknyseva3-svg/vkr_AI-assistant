import pytest
from app.models.retriever import Retriever

def test_retriever():
    retriever = Retriever()
    retriever.load_index('./data/faiss_index', './data/knowledge_base')
    results = retriever.retrieve('CRM система для учёта клиентов', k=3)
    assert len(results) > 0
    assert 'score' in results[0]
