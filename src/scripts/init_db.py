from db import get_connection

def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE EXTENSION IF NOT EXISTS vector;

                CREATE TABLE IF NOT EXISTS context (
                    id SERIAL PRIMARY KEY,
                    content TEXT,
                    embedding VECTOR(384)
                );
            """)
        conn.commit()

if __name__ == "__main__":
    init_db()