from sentence_transformers import SentenceTransformer
import fitz  # PyMuPDF
import re

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip())

def extract_paragraphs(pdf_path, chunk_size=512):
    doc = fitz.open(pdf_path)
    paragraphs = []
    for page in doc:
        text = clean_text(page.get_text())
        paragraphs.extend(re.split(r'\n{2,}', text))
    return [p for p in paragraphs if len(p) > 50]  # отсекаем слишком короткие

def embed_paragraphs(paragraphs):
    return model.encode(paragraphs, convert_to_numpy=True)
