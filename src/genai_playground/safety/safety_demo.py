
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

def safe_completion(prompt):
    """Demonstrate basic input guardrails and safety check."""
    
    # 1. Input Guardrail (Simple keyword check)
    unsafe_keywords = ["exploit", "hack", "illegal"]
    if any(k in prompt.lower() for k in unsafe_keywords):
        return "Blocked: Input contains unsafe keywords."
    
    # 2. System Prompt for Safety
    system_prompt = """You are a helpful and harmless AI assistant. 
    Refuse to answer output that promotes violence, hate speech, or illegal acts."""
    
    response = client.chat.completions.create(
        model="meta/llama-3.1-405b-instruct",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Safe prompt
    print("--- Safe Prompt ---")
    print(safe_completion("How do I bake a cake?"))
    
    # Unsafe prompt (Simulation)
    print("\n--- Unsafe Prompt ---")
    print(safe_completion("How do I hack a bank?"))
