"""
NVIDIA Image Generation - Simple Example
========================================
Basic text-to-image generation using NVIDIA's cloud API.

Prerequisites:
1. Get NVIDIA API key from https://build.nvidia.com/
2. Add NVIDIA_API_KEY to your .env file
3. Install: uv sync --extra image

Usage:
    uv run pypthon 10_image_generation/api_integrations/nvidia_image_gen.py
"""

import os
import base64
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("NVIDIA_API_KEY")

def generate_image(prompt, model="stabilityai/stable-diffusion-xl"):
    """Generate image using NVIDIA API."""
    if not API_KEY:
        print("❌ Error: NVIDIA_API_KEY not found in .env")
        return None

    print(f"🎨 Generating: '{prompt[:40]}...' using {model}")

    # Endpoint Configuration
    if "flux" in model.lower():
        url = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux-1-dev"
        payload = {
            "prompt": prompt,
            "width": 1024, "height": 1024, "steps": 28, "guidance_scale": 3.5, "seed": 0
        }
    else:
        url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-xl"
        payload = {
            "text_prompts": [{"text": prompt, "weight": 1}],
            "cfg_scale": 5, "sampler": "K_EULER_ANCESTRAL", "steps": 25, "seed": 0
        }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=90)
        
        if response.status_code != 200:
            print(f"❌ API Error {response.status_code}: {response.text}")
            return None

        result = response.json()
        
        # Handle different response formats (NVIDIA native vs OpenAI-style)
        if "artifacts" in result:
            b64_data = result["artifacts"][0]["base64"]
        elif "data" in result:
            b64_data = result["data"][0]["b64_json"]
        else:
            print("❌ Unexpected response format")
            return None
            
        return base64.b64decode(b64_data)

    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    # Create output directory
    os.makedirs("10_image_generation/output", exist_ok=True)
    
    # Test Prompt
    prompt = "A futuristic city with flying cars, cyberpunk style"
    
    # 1. Try Default (SDXL)
    image_data = generate_image(prompt)
    
    # 2. Simple Fallback (if SDXL failed)
    if not image_data:
        print("⚠️ SDXL failed, trying Flux...")
        image_data = generate_image(prompt, model="black-forest-labs/flux-1-dev")

    # Save Result
    if image_data:
        with open("10_image_generation/output/test_gen.png", "wb") as f:
            f.write(image_data)
        print("✅ Saved to 10_image_generation/output/test_gen.png")
