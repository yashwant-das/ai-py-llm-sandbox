"""
NVIDIA Image Generation - Simple Example
========================================
Basic text-to-image generation using NVIDIA's cloud API.

This is a simple, standalone example for learning purposes.
No complex classes or abstractions - just direct API calls.

Prerequisites:
1. Get NVIDIA API key from https://build.nvidia.com/
2. Add NVIDIA_API_KEY to your .env file
3. Install dependencies: uv sync --extra image

Usage:
    uv run python 10_image_generation/api_integrations/nvidia_image_gen.py
"""

import sys
from pathlib import Path

# Add project root to path for shared imports
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now we can use absolute imports from the project root
from shared.image_generation import generate_image as _generate_image

# Output directory for generated images
OUTPUT_DIR = Path("10_image_generation/output")
OUTPUT_DIR.mkdir(exist_ok=True)


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
    print(f"🎨 Generating image with prompt: '{prompt}'")
    print(f"   Model: {model}")

    image_data = _generate_image(prompt, model, negative_prompt)

    if image_data:
        print("✅ Image generated successfully!")
    else:
        print("❌ Failed to generate image")

    return image_data


def save_image(image_data, filename):
    """
    Save image data to a file.

    Args:
        image_data: Image data (bytes)
        filename: Name of the file to save
    """
    filepath = OUTPUT_DIR / filename
    with open(filepath, "wb") as f:
        f.write(image_data)
    print(f"💾 Saved to: {filepath}")


def main():
    """Run simple image generation examples."""
    print("=" * 70)
    print("NVIDIA IMAGE GENERATION - SIMPLE EXAMPLES")
    print("=" * 70)
    print()

    # Example 1: Simple landscape
    print("--- Example 1: Simple Landscape ---")
    prompt1 = "A serene mountain landscape at sunset, with a lake reflecting the golden light, photorealistic, 4K"
    image1 = generate_image(prompt1)
    if image1:
        save_image(image1, "01_landscape.png")
    print()

    # Example 2: Portrait with style
    print("--- Example 2: Portrait with Style ---")
    prompt2 = "A futuristic cyberpunk city street at night, neon lights, rain, highly detailed, cinematic lighting"
    negative_prompt2 = "blurry, low quality, distorted"
    image2 = generate_image(prompt2, negative_prompt=negative_prompt2)
    if image2:
        save_image(image2, "02_cyberpunk.png")
    print()

    # Example 3: Artistic style
    print("--- Example 3: Artistic Style ---")
    prompt3 = "An oil painting of a cozy coffee shop interior, warm lighting, impressionist style, vibrant colors"
    image3 = generate_image(prompt3)
    if image3:
        save_image(image3, "03_coffee_shop.png")
    print()

    # Example 4: Fantasy creature
    print("--- Example 4: Fantasy Creature ---")
    prompt4 = "A majestic dragon flying over ancient ruins, epic fantasy art, detailed scales, dramatic lighting"
    image4 = generate_image(prompt4)
    if image4:
        save_image(image4, "04_dragon.png")
    print()

    print("=" * 70)
    print("✨ All examples completed!")
    print(f"📁 Images saved to: {OUTPUT_DIR}")
    print("=" * 70)


if __name__ == "__main__":
    main()
