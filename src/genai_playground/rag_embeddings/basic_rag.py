
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "nvapi-dummy"))
)

# Simulated Document Database
documents = [
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome."
]

def retrieve(query):
    """(Simulated) Vector Search / Retrieval Step."""
    print(f"\nRetrieving documents relevant to: '{query}'...")
    # In a real system, you'd embed the query and search a vector DB.
    # Here, we do a simple keyword match for demonstration.
    results = [doc for doc in documents if any(word in doc.lower() for word in query.lower().split())]
    return results if results else ["No relevant documents found."]

def generate_answer(query, context):
    """Augmented Generation Step."""
    prompt = f"""Use the following context to answer the question.
    
    Context:
    {context}
    
    Question: {query}
    
    Answer:"""
    
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL_ID", "meta/llama-3.1-405b-instruct"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    user_query = "What is the capital of France?"
    
    # 1. Retrieve
    retrieved_docs = retrieve(user_query)
    context_text = "\n".join(retrieved_docs)
    print(f"Context found: {context_text}")
    
    # 2. Generate
    answer = generate_answer(user_query, context_text)
    print(f"\nRAG Answer: {answer}")
