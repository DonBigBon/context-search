from embedder import extract_paragraphs, embed_paragraphs
from db import get_connection
from tqdm import tqdm

def upload_embeddings(pdf_path):
    paragraphs = extract_paragraphs(pdf_path)
    embeddings = embed_paragraphs(paragraphs)

    with get_connection() as conn:
        with conn.cursor() as cur:
            for i in tqdm(range(len(paragraphs))):
                cur.execute(
                    "INSERT INTO context (content, embedding) VALUES (%s, %s)",
                    (paragraphs[i], embeddings[i].tolist())
                )
        conn.commit()

if __name__ == "__main__":
    upload_embeddings("Лесной кодекс Республики Казахстан.pdf")
