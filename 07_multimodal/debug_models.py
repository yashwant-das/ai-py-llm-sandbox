
import os
import requests
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def list_models():
    api_key = os.getenv("NVIDIA_API_KEY")
    
    # 1. Check API Key
    if not api_key:
        print("❌ NVIDIA_API_KEY is not configured in .env")
        print("   Get a key from https://build.nvidia.com/")
        return

    print(f"✅ NVIDIA_API_KEY found: {api_key[:4]}...{api_key[-4:]}")

    # 2. List LLMs via Standard API
    print("\n--- Listing Available LLMs (via /models) ---")
    try:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key
        )
        response = client.models.list()
        
        llm_count = 0
        for model in response:
             print(f" - {model.id}")
             llm_count += 1
        
        print(f"Total LLMs found: {llm_count}")
            
    except Exception as e:
        print(f"❌ Error listing LLMs: {e}")

    # 3. Check Image Generation Availability (Direct Endpoint Check)
    print("\n--- Checking Image Generation Availability ---")
    
    # Define endpoints to check
    image_models = [
        ("stabilityai/stable-diffusion-xl", "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-xl"),
        ("black-forest-labs/flux-1-dev", "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux-1-dev")
    ]
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }
    
    for name, url in image_models:
        try:
            # We use GET to check connectivity/auth without generating
            # Expect 405 (Method Not Allowed) if auth works but GET is invalid for generation
            # Expect 404 if model/endpoint doesn't exist
            # Expect 401/403 if auth fails
            resp = requests.get(url, headers=headers, timeout=10)
            
            if resp.status_code in [405, 200, 422]:
                print(f"✅ {name}: Available (Endpoint reachable)")
            elif resp.status_code in [401, 403]:
                print(f"❌ {name}: Unauthorized (Check API Key permissions)")
            elif resp.status_code == 404:
                print(f"❌ {name}: Not Found (Endpoint unavailable)")
            else:
                print(f"⚠️  {name}: Unexpected status {resp.status_code}")
                
        except Exception as e:
            print(f"❌ {name}: Connection Error ({e})")

    print("\nTo generate an image, run:")
    print("python3 10_image_generation/api_integrations/nvidia_image_gen.py")

if __name__ == "__main__":
    list_models()
