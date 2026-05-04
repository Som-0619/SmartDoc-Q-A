from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model once
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

chunks = []
index = None


def load_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    return text


def chunk_text(text, size=800, overlap=200):
    chunk_list = []

    for i in range(0, len(text), size - overlap):
        chunk = text[i:i+size]

        if len(chunk.strip()) > 100:
            chunk_list.append(chunk)

    return chunk_list


def create_index(text):
    global chunks, index

    chunks = chunk_text(text)

    embeddings = embed_model.encode(chunks)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))


def retrieve(query, k=7):
    global index, chunks

    if index is None:
        return ["No documents processed yet."]

    q_emb = embed_model.encode([query])
    distances, indices = index.search(q_emb, k)

    results = []
    for i in indices[0]:
        if i < len(chunks):
            results.append(chunks[i])

    return results