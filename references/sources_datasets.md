# Используемые датасеты и источники данных

## Для обучения моделей (на этапе разработки)

### Русскоязычные датасеты диалогов
- **Russian Speech Recognition Dataset** (1000+ часов колл-центров)  
  URL: https://huggingface.co/datasets/AxonData/russian-speech-recognition-dataset  
  Формат: аудио + транскрипты, разделение агент/клиент  
  Лицензия: Commercial (запрос на AxonLabs)

- **AI Agent Outbound Calls Dataset in Russian**  
  URL: https://data.macgence.com/dataset/ai-agent-outbound-calls-dataset-in-russian  
  Формат: аудио + JSON-метаданные  
  Лицензия: Commercial (OTS)

### Для RAG и эмбеддингов
- **Kindred E-commerce Merchant Deals Dataset**  
  URL: https://github.com/kindred-app/kindred-ecommerce-merchant-deals-dataset  
  Формат: CSV/JSONL, 90K брендов, 4M предложений  
  Лицензия: CC BY 4.0

### Для обучения ИИ-агентов работе с инструментами
- **TOUCAN Dataset**  
  URL: https://huggingface.co/datasets/mit-llm/toucan  
  Формат: реальные взаимодействия с API и инструментами  
  Лицензия: Open

## Для дообучения ruBERT
- **RuSentiment** (через референс-проект)  
  URL: https://github.com/Geroinageroine/llm-model  
  Описание: пример дообучения ruBERT на задачу классификации

## Платформы для поиска дополнительных данных
- Hugging Face Datasets: https://huggingface.co/datasets
- Kaggle: https://www.kaggle.com/datasets
- Toloka: https://toloka.ai/ru/datasets
- Nexdata: https://nexdata.ai/datasets
