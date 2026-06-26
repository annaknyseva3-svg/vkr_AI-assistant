"""
Модуль генерации на основе ruGPT-3 с LoRA.
"""
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from peft import PeftModel, PeftConfig
from app.config import Config
from app.models.retriever import Retriever
from app.models.calibrator import Calibrator

class ProposalGenerator:
    def __init__(self):
        self.retriever = Retriever()
        self.retriever.load_index('./data/faiss_index', './data/knowledge_base')
        
        self.calibrator = Calibrator()
        
        # Загрузка модели ruGPT-3 + LoRA
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = AutoModelForCausalLM.from_pretrained(
            Config.MODEL_PATH,
            torch_dtype=torch.float16 if self.device == 'cuda' else torch.float32
        ).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_PATH)
        
        # Применение LoRA
        peft_config = PeftConfig.from_pretrained('./models/lora')
        self.model = PeftModel.from_pretrained(self.model, './models/lora')
        self.model.eval()
        
        # Пайплайн генерации
        self.generator = pipeline(
            'text-generation',
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if self.device == 'cuda' else -1
        )
    
    def _build_prompt(self, query, fragments):
        """Формирование промпта с подстановкой RAG-фрагментов"""
        frag_text = '\n'.join([f['text'] for f in fragments[:3]])
        return f"""
Ты — ассистент менеджера по продажам. Составь коммерческое предложение.

Информация о клиенте: {query}

Актуальные данные из базы знаний:
{frag_text}

Требования:
- Структура: Заголовок → Проблема → Решение → Выгоды → Цена → Призыв → Контакты
- Тон: деловой, дружелюбный
- Не используй вымышленные цены и сроки

КП:
"""
    
    def generate(self, query):
        """Полный цикл генерации: RAG → LLM → калибровка"""
        # 1. Поиск релевантных фрагментов
        fragments = self.retriever.retrieve(query)
        
        # 2. Формирование промпта
        prompt = self._build_prompt(query, fragments)
        
        # 3. Генерация
        output = self.generator(
            prompt,
            max_new_tokens=Config.MAX_NEW_TOKENS,
            temperature=Config.TEMPERATURE,
            top_p=Config.TOP_P,
            repetition_penalty=Config.REPETITION_PENALTY,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )[0]['generated_text']
        
        # 4. Калибровка
        calibrated = self.calibrator.calibrate(output, fragments)
        
        return calibrated
