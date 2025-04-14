# Context Search — Поиск релевантного контекста из документа

Проект выполняет векторный поиск наиболее подходящего фрагмента текста из PDF-документа на основе пользовательского запроса.

## Технологии
- Python, VSCode
- PostgreSQL + pgvector
- HuggingFace Embeddings: `paraphrase-multilingual-MiniLM-L12-v2`
- Sentence-Transformers, psycopg2, dotenv

## Установка
```bash
git clone https://github.com/DonBigBon/context-search.git
cd context-search
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
