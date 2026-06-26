"""
Сборка базы знаний из исходных документов.
"""
import json
import os
from app.config import Config

def chunk_text(text, chunk_size=300, overlap=50):
    """Разбиение текста на чанки с перекрытием"""
    chunks = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def build_knowledge_base(input_dir, output_dir):
    """Сборка базы знаний из документов"""
    all_chunks = []
    all_metadata = []
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                chunks = chunk_text(text, Config.CHUNK_SIZE, Config.CHUNK_OVERLAP)
                for chunk in chunks:
                    all_chunks.append(chunk)
                    all_metadata.append({
                        'source': filename,
                        'title': filename.replace('.txt', '')
                    })
    
    # Сохранение
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'chunks.json'), 'w', encoding='utf-8') as f:
        json.dump({'chunks': all_chunks, 'metadata': all_metadata}, f, ensure_ascii=False, indent=2)
    
    print(f"Создано {len(all_chunks)} чанков")

if __name__ == '__main__':
    build_knowledge_base('./data/raw', './data/knowledge_base')
