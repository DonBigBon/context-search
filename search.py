from embedder import model, clean_text
from db import get_connection
import numpy as np

THRESHOLD = 0.7 

def search_context(query):
    query_embedding = model.encode([clean_text(query)])[0]
    vector_str = "[" + ", ".join([str(x) for x in query_embedding]) + "]"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT content, 1 - (embedding <#> %s::vector) AS similarity
                FROM context
                ORDER BY embedding <#> %s::vector ASC
                LIMIT 1;
            """, (vector_str, vector_str))
            result = cur.fetchone()
            if result and result[1] >= THRESHOLD:
                return result[0]
            return "Контекст не найден"
