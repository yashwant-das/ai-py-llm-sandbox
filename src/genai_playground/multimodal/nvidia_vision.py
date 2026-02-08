"""
NVIDIA Vision - Analyze Images
==============================
Analyze images using NVIDIA Vision APIs.

Usage:
    uv run python 10_image_generation/api_integrations/nvidia_vision.py
"""

import os
import base64
import requests
from dotenv import load_dotenv

# Load env vars
load_dotenv()

def encode_image(image_path):
    """Encodes image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def analyze_image(image_path, question="Describe this image"):
    """Ask a question about an image."""
    base_url = os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1")
    api_key = os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY"))
    model = os.getenv("LLM_MODEL_ID", "meta/llama-3.2-90b-vision-instruct")

    if not api_key and "nvidia" in base_url:
        print("❌ API Key Missing")
        return None

    print(f"🔍 Analyzing: '{image_path}' with '{question}'")
    print(f"  Provider: {base_url}")
    print(f"  Model:    {model}")
    
    try:
        from openai import OpenAI
        client = OpenAI(base_url=base_url, api_key=api_key or "unused")
        
        image_b64 = encode_image(image_path)
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": question},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}}
                    ]
                }
            ],
            max_tokens=512,
        )
        
        answer = response.choices[0].message.content
        print(f"✅ Answer: {answer}")
        return answer
            
    except FileNotFoundError:
        print(f"❌ File not found: {image_path}")
        return None
    except Exception as e:
        print(f"❌ Exception: {e}")
        return None

if __name__ == "__main__":
    # Check for test image
    image_paths = [
        "10_image_generation/output/test_gen.png",
        "10_image_generation/output/01_landscape.png"
    ]
    
    path = next((p for p in image_paths if os.path.exists(p)), None)
    
    if path:
        analyze_image(path, "Describe this image in detail.")
    else:
        print("⚠️ No test images found. Run nvidia_image_gen.py first.")
