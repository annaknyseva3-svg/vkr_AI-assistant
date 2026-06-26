# vkr_AI-assistant
Система контроля версий разработки ИИ-ассистента для подготовки коммерческих предложений - ВКР, магистратура

# ИИ-ассистент для подготовки коммерческих предложений

## Описание
Интеллектуальная система для автоматической генерации персонализированных коммерческих предложений на основе краткого ввода менеджера. Использует RAG (Retrieval-Augmented Generation), тонкую настройку ruGPT-3 и многоэтапную калибровку для минимизации галлюцинаций.

## Стек технологий
- **Backend:** Python 3.10, Flask, PyTorch 2.1
- **NLP:** Hugging Face Transformers, PEFT (LoRA), Sentence Transformers
- **Поиск:** FAISS, RuBERT
- **База данных:** SQLite, SQLAlchemy
- **DevOps:** Docker, GitHub Actions

## Установка
```bash
# Клонирование репозитория
git clone https://github.com/yourusername/ai-assistant-proposal.git
cd ai-assistant-proposal

# Установка зависимостей
pip install -r requirements.txt

# Настройка переменных окружения
cp .env.example .env
# Отредактируйте .env (укажите путь к модели, данные, БД)

# Запуск приложения
python app/main.py
