"""
NVIDIA API Image Generation Functions
=====================================
Common functions for interacting with NVIDIA's cloud APIs for image generation.
"""

import base64
import requests
from shared import get_settings


def generate_image(
    prompt, model="stabilityai/stable-diffusion-xl", negative_prompt=None
):
    """
    Generate an image from text prompt using NVIDIA API.

    Args:
        prompt: Text description of the image to generate
        model: Model to use (default: stabilityai/stable-diffusion-xl)
        negative_prompt: Things to avoid in the image (optional)

    Returns:
        Image data (bytes) or None if failed
    """
    settings = get_settings()

    if not settings.nvidia_api_key:
        print("❌ Error: NVIDIA_API_KEY not found in .env file")
        print("   Get your API key from: https://build.nvidia.com/")
        return None

    # API endpoint for image generation
    base_url = "https://integrate.api.nvidia.com/v1"
    url = f"{base_url}/images/generations"

    # Request headers
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json",
    }

    # Request body
    payload = {
        "model": model,
        "prompt": prompt,
        "num_inference_steps": 50,
        "guidance_scale": 7.5,
        "width": 1024,
        "height": 1024,
        "num_images": 1,
    }

    if negative_prompt:
        payload["negative_prompt"] = negative_prompt

    try:
        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        # Parse response
        result = response.json()
        
        # Extract base64 image data
        # NVIDIA API typically returns: {"artifacts": [{"base64": "..."}]}
        # or OpenAI format: {"data": [{"b64_json": "..."}]}
        
        image_data = None
        if "artifacts" in result and len(result["artifacts"]) > 0:
            image_data = result["artifacts"][0].get("base64")
        elif "data" in result and len(result["data"]) > 0:
             image_data = result["data"][0].get("b64_json")
             
        if image_data:
            return base64.b64decode(image_data)
            
        return None

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("   ❌ Error: 404 Not Found (Endpoint unavailable)")
            print("   ℹ️  Note: Your current NVIDIA API key/entitlements may not include Image Generation models.")
            print("       This feature requires specific access to models like 'stabilityai/stable-diffusion-xl'.")
            print("       Check your available models list.")
        else:
            print(f"   ❌ API Error: {e}")
            if hasattr(e, "response") and e.response:
                print(f"   Response: {e.response.text}")
        return None
