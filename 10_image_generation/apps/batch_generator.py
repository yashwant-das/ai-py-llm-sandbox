"""
Batch Image Generator - Generate Multiple Images at Once
========================================================
Generate multiple images from a list of prompts using NVIDIA's API.

This example shows how to:
- Generate multiple images in a batch
- Organize output with clear filenames
- Handle errors gracefully
- Track progress

Prerequisites:
1. Get NVIDIA API key from https://build.nvidia.com/
2. Add NVIDIA_API_KEY to your .env file
3. Install dependencies: uv sync --extra image

Usage:
    uv run python 10_image_generation/apps/batch_generator.py
"""

import time
from datetime import datetime
from pathlib import Path

from ..shared.nvidia_api import generate_image as _generate_image

# Output directory for generated images
OUTPUT_DIR = Path("10_image_generation/output/batch")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_image(
    prompt, model="stabilityai/stable-diffusion-xl", negative_prompt=None
):
    """
    Generate an image from text prompt using NVIDIA API.

    Args:
        prompt: Text description of the image to generate
        model: Model to use
        negative_prompt: Things to avoid in the image (optional)

    Returns:
        Image data (bytes) or None if failed
    """
    return _generate_image(prompt, model, negative_prompt)


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
    return filepath


def sanitize_filename(text):
    """
    Convert text to a safe filename.

    Args:
        text: Text to convert

    Returns:
        Safe filename string
    """
    # Remove or replace unsafe characters
    unsafe_chars = '<>:"/\\|?*'
    for char in unsafe_chars:
        text = text.replace(char, "_")

    # Prevent path traversal
    text = text.replace("..", "_")

    # Remove leading/trailing dots and spaces
    text = text.strip(". ")

    # Limit length
    if len(text) > 50:
        text = text[:50]

    # Ensure filename is not empty
    if not text:
        text = "unnamed"

    return text


def generate_batch(prompts, model="stabilityai/stable-diffusion-xl", delay=1):
    """
    Generate multiple images from a list of prompts.

    Args:
        prompts: List of prompt dictionaries with 'prompt' and optional 'negative_prompt'
        model: Model to use for generation
        delay: Delay between requests in seconds (to avoid rate limits)

    Returns:
        Dictionary with results and statistics
    """
    import os

    if not os.environ.get("NVIDIA_API_KEY"):
        print("❌ Error: NVIDIA_API_KEY not found in .env file")
        return {"success": False, "error": "No API key"}

    results = {
        "success": True,
        "total": len(prompts),
        "generated": 0,
        "failed": 0,
        "images": [],
        "errors": [],
    }

    print(f"🎨 Starting batch generation of {len(prompts)} images...")
    print(f"   Model: {model}")
    print(f"   Output directory: {OUTPUT_DIR}")
    print()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for i, prompt_data in enumerate(prompts, 1):
        prompt = prompt_data.get("prompt", "")
        negative_prompt = prompt_data.get("negative_prompt")

        print(f"[{i}/{len(prompts)}] Generating: {prompt[:60]}...")

        # Generate image
        image_data = generate_image(prompt, model, negative_prompt)

        if image_data:
            # Create filename
            safe_name = sanitize_filename(prompt)
            filename = f"{timestamp}_{i:03d}_{safe_name}.png"

            # Save image
            filepath = save_image(image_data, filename)
            print(f"   ✅ Saved: {filepath.name}")

            results["generated"] += 1
            results["images"].append(
                {
                    "index": i,
                    "prompt": prompt,
                    "filename": filename,
                    "filepath": str(filepath),
                }
            )
        else:
            print("   ❌ Failed to generate")
            results["failed"] += 1
            results["errors"].append(
                {"index": i, "prompt": prompt, "error": "Generation failed"}
            )

        # Add delay between requests
        if i < len(prompts):
            time.sleep(delay)

    print()
    return results


def print_summary(results):
    """Print a summary of the batch generation results."""
    print("=" * 70)
    print("BATCH GENERATION SUMMARY")
    print("=" * 70)
    print(f"Total prompts: {results['total']}")
    print(f"✅ Generated: {results['generated']}")
    print(f"❌ Failed: {results['failed']}")
    print()

    if results["images"]:
        print("Generated images:")
        for img in results["images"]:
            print(f"  {img['index']}. {img['filename']}")
            print(f"     Prompt: {img['prompt'][:60]}...")
        print()

    if results["errors"]:
        print("Failed generations:")
        for err in results["errors"]:
            print(f"  {err['index']}. {err['prompt'][:60]}...")
            print(f"     Error: {err['error']}")
        print()

    print(f"📁 All images saved to: {OUTPUT_DIR}")
    print("=" * 70)


def main():
    """Run batch generation examples."""
    print("=" * 70)
    print("BATCH IMAGE GENERATOR")
    print("=" * 70)
    print()

    # Example 1: Simple batch
    print("--- Example 1: Simple Batch ---")
    prompts1 = [
        {"prompt": "A serene mountain landscape at sunset"},
        {"prompt": "A futuristic cyberpunk city street at night"},
        {"prompt": "An oil painting of a cozy coffee shop"},
        {"prompt": "A majestic dragon flying over ancient ruins"},
        {"prompt": "A peaceful Japanese garden with cherry blossoms"},
    ]

    results1 = generate_batch(prompts1, delay=2)
    print_summary(results1)
    print()

    # Example 2: Batch with negative prompts
    print("--- Example 2: Batch with Negative Prompts ---")
    prompts2 = [
        {
            "prompt": "A portrait of a woman in renaissance style",
            "negative_prompt": "blurry, low quality, distorted features",
        },
        {
            "prompt": "A space station orbiting a distant planet",
            "negative_prompt": "cartoonish, low resolution, grainy",
        },
        {
            "prompt": "A magical forest with glowing mushrooms",
            "negative_prompt": "dark, scary, horror",
        },
    ]

    results2 = generate_batch(prompts2, delay=2)
    print_summary(results2)
    print()

    # Example 3: Thematic batch
    print("--- Example 3: Thematic Batch (Seasons) ---")
    prompts3 = [
        {"prompt": "Spring meadow with colorful flowers and butterflies"},
        {"prompt": "Summer beach with golden sand and turquoise water"},
        {"prompt": "Autumn forest with red and orange falling leaves"},
        {"prompt": "Winter wonderland with snow-covered pine trees"},
    ]

    results3 = generate_batch(prompts3, delay=2)
    print_summary(results3)
    print()

    print("✨ All batch generations completed!")


if __name__ == "__main__":
    main()
