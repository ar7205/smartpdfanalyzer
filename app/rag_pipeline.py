from app.pdf_utils import extract_text
from app.text_utils import chunk_text
from app.hf_embeddings import get_embedding
from app.vector_store import VectorStore
from app.ollama_chat import generate_answer


def process_pdf(pdf_path):

    text = extract_text(pdf_path)

    chunks = chunk_text(text)

    embeddings = []

    for chunk in chunks:
        embeddings.append(get_embedding(chunk))

    vector_store = VectorStore(dimension=384)

    vector_store.add_embeddings(
        embeddings,
        chunks
    )

    return {
        "vector_store": vector_store,
        "chunks": chunks,
        "total_chunks": len(chunks),
        "text_length": len(text)
    }


def ask_question(question, vector_store):

    question_embedding = get_embedding(question)

    results = vector_store.search(
        question_embedding
    )

    answer = generate_answer(
        question,
        results
    )

    return answer, results