import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(question, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
       model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text