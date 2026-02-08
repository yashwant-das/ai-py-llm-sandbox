
import sys
import requests
from pathlib import Path

# Add project root to path
# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.absolute()))

# Create shared module import capability
try:
    from shared import get_nvidia_client, get_settings
except ImportError:
    # Fallback if running from proper location
    sys.path.append("..")
    from shared import get_nvidia_client, get_settings


def list_models():
    settings = get_settings()
    
    # 1. Check API Key
    if not settings.nvidia_api_key:
        print("❌ NVIDIA_API_KEY is not configured in .env")
        print("   Get a key from https://build.nvidia.com/")
        return

    print(f"✅ NVIDIA_API_KEY found: {settings.nvidia_api_key[:4]}...{settings.nvidia_api_key[-4:]}")

    # 2. List LLMs via Standard API
    print("\n--- Listing Available LLMs (via /models) ---")
    try:
        client = get_nvidia_client()
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
        "Authorization": f"Bearer {settings.nvidia_api_key}",
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
