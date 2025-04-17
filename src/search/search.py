from keybert import KeyBERT
from src.embeddings.embedder import model, clean_text
from src.db.db import get_connection
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

THRESHOLD = 0.7
keybert_model = KeyBERT()

def search_context(query):
    keywords = keybert_model.extract_keywords(query, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=3)
    keywords_text = " ".join([kw[0] for kw in keywords])

    logging.info(f"Extracted keywords: {keywords_text}")

    query_embedding = model.encode([clean_text(keywords_text)])[0]
    vector_str = "[" + ", ".join([str(x) for x in query_embedding]) + "]"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT content, 1 - (embedding <#> %s::vector) AS similarity
                FROM context
                ORDER BY embedding <#> %s::vector ASC
                LIMIT 5;
            """, (vector_str, vector_str))
            results = cur.fetchall()
            if results:
                return [{"content": row[0], "similarity": row[1]} for row in results]
            return [{"content": "Контекст не найден", "similarity": 0}]