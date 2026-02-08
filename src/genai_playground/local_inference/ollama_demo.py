
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# Installation: https://ollama.com/
# Run: ollama serve

# Use configured URL or default to Ollama's default
OLLAMA_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434/api/generate").replace("/v1", "/api/generate")
DEFAULT_MODEL = os.getenv("LLM_MODEL_ID", "llama3")

def run_local_model(prompt, model=DEFAULT_MODEL):
    """Run inference on a local model via Ollama."""
    print(f"Running prompt on local model '{model}' at {OLLAMA_URL}...")
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
        
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Is it running?"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    prompt = "Explain quantum computing in one sentence."
    response = run_local_model(prompt)
    print(f"\nResponse:\n{response}")
