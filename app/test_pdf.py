from app.pdf_utils import extract_text
from app.text_utils import chunk_text
from app.hf_embeddings import get_embedding
from app.vector_store import VectorStore
from app.ollama_chat import generate_answer
print("Starting PDF test...")
# Step 1: extract text
text = extract_text("sample.pdf")

print("Raw text preview:\n")
print(text[:500])

# Step 2: chunk it
chunks = chunk_text(text)

print("\nTotal chunks:", len(chunks))

if chunks:
    print("\nFirst chunk:\n")
    print(chunks[0])

    embedding = get_embedding(chunks[0])
    print("\nEmbedding length:", len(embedding))
else:
    print("No chunks found ❌")

# Create embeddings for all chunks
embeddings = []

for chunk in chunks:
    embedding = get_embedding(chunk)
    embeddings.append(embedding)

print("\nCreated embeddings:", len(embeddings))

# Create vector store
vector_store = VectorStore(dimension=384)

# Store embeddings + chunks
vector_store.add_embeddings(embeddings, chunks)

print("Embeddings stored in FAISS ✅")

# User question
question = "What is this PDF about?"

# Convert question into embedding
question_embedding = get_embedding(question)

# Search similar chunks
results = vector_store.search(question_embedding)

print("\nTop matching chunks:\n")

for result in results:
    print(result)
    print("\n------------------\n")

# Generate final answer
final_answer = generate_answer(question, results)

print("\nFINAL ANSWER:\n")
print(final_answer)