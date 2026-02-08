
import requests
import json

# This script assumes you have Ollama running locally.
# Installation: https://ollama.com/
# Run: ollama serve

OLLAMA_URL = "http://localhost:11434/api/generate"

def run_local_model(prompt, model="llama3"):
    """Run inference on a local model via Ollama."""
    print(f"Running prompt on local model '{model}'...")
    
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
