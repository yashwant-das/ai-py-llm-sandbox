"""
NVIDIA Vision Models - Simple Example
=====================================
Using NVIDIA's vision models for image understanding and analysis.

This example uses NVIDIA's vision-language models to:
- Describe images
- Analyze image content
- Answer questions about images

Prerequisites:
1. Get NVIDIA API key from https://build.nvidia.com/
2. Add NVIDIA_API_KEY to your .env file
3. Install dependencies: uv sync --extra image

Usage:
    uv run python 10_image_generation/api_integrations/nvidia_vision.py
"""

import base64
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# NVIDIA API Configuration
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"

# Recommended vision models from your available list
VISION_MODELS = {
    "neva": "nvidia/neva-22b",  # General vision understanding
    "vila": "nvidia/vila",  # Vision-language assistant
    "nemotron_vl": "nvidia/llama-3.1-nemotron-nano-vl-8b-v1",  # Small vision model
    "llama_vision": "meta/llama-3.2-90b-vision-instruct",  # Large vision model
}


def encode_image(image_path):
    """
    Encode an image file to base64 string.

    Args:
        image_path: Path to the image file

    Returns:
        Base64 encoded string or None if failed
    """
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        print(f"❌ Error: Image file not found: {image_path}")
        return None
    except PermissionError:
        print(f"❌ Error: Permission denied reading: {image_path}")
        return None
    except Exception as e:
        print(f"❌ Error reading image: {e}")
        return None


def analyze_image(image_path, question, model="nvidia/neva-22b"):
    """
    Analyze an image using NVIDIA's vision model.

    Args:
        image_path: Path to the image file
        question: Question to ask about the image
        model: Vision model to use

    Returns:
        Model's response text or None if failed
    """
    if not NVIDIA_API_KEY:
        print("❌ Error: NVIDIA_API_KEY not found in .env file")
        return None

    if not os.path.exists(image_path):
        print(f"❌ Error: Image file not found: {image_path}")
        return None

    # API endpoint for chat completions
    url = f"{NVIDIA_BASE_URL}/chat/completions"

    # Encode image
    image_base64 = encode_image(image_path)
    if not image_base64:
        return None

    # Request headers
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json",
    }

    # Request body with image
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                    },
                ],
            }
        ],
        "max_tokens": 512,
        "temperature": 0.1,
    }

    try:
        print(f"🔍 Analyzing image: {image_path}")
        print(f"   Question: {question}")
        print(f"   Model: {model}")

        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        # Parse response
        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            answer = result["choices"][0]["message"]["content"]
            print("✅ Analysis complete!")
            return answer
        else:
            print("❌ No response from model")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        if hasattr(e, "response") and e.response:
            print(f"   Response: {e.response.text}")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def describe_image(image_path, model="nvidia/neva-22b"):
    """
    Get a detailed description of an image.

    Args:
        image_path: Path to the image file
        model: Vision model to use

    Returns:
        Image description
    """
    question = "Describe this image in detail. What do you see? Include information about the subject, setting, colors, mood, and any notable details."
    return analyze_image(image_path, question, model)


def main():
    """Run simple vision model examples."""
    print("=" * 70)
    print("NVIDIA VISION MODELS - SIMPLE EXAMPLES")
    print("=" * 70)
    print()

    # Check if we have any images to analyze
    # You can use images generated from nvidia_image_gen.py or your own images
    output_dir = Path("10_image_generation/output")

    # Try to find an image from the output directory
    image_files = (
        list(output_dir.glob("*.png"))
        + list(output_dir.glob("*.jpg"))
        + list(output_dir.glob("*.jpeg"))
    )

    if not image_files:
        print("⚠️  No images found in output directory.")
        print("   Please run nvidia_image_gen.py first to generate some images,")
        print("   or place your own images in the output directory.")
        print()
        print("   Example usage with your own image:")
        print(
            "   python -c \"from api_integrations.nvidia_vision import describe_image; print(describe_image('path/to/your/image.jpg'))\""
        )
        return

    # Use the first available image
    test_image = image_files[0]
    print(f"📷 Using image: {test_image}")
    print()

    # Example 1: Basic description
    print("--- Example 1: Image Description ---")
    description = describe_image(test_image, model=VISION_MODELS["neva"])
    if description:
        print(f"\n📝 Description:\n{description}")
    print()

    # Example 2: Specific questions
    print("--- Example 2: Specific Questions ---")

    questions = [
        "What is the main subject of this image?",
        "What is the mood or atmosphere of this image?",
        "What colors are most prominent?",
        "What style is this image in (photorealistic, artistic, etc.)?",
    ]

    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        answer = analyze_image(test_image, question, model=VISION_MODELS["neva"])
        if answer:
            print(f"💬 Answer: {answer}")
    print()

    # Example 3: Compare different models
    print("--- Example 3: Comparing Vision Models ---")
    print("Testing different vision models on the same image...")
    print()

    test_question = "Describe this image in one sentence."

    for model_name, model_id in VISION_MODELS.items():
        print(f"\n🤖 Model: {model_name} ({model_id})")
        answer = analyze_image(test_image, test_question, model=model_id)
        if answer:
            print(f"   {answer}")
    print()

    print("=" * 70)
    print("✨ All examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()
