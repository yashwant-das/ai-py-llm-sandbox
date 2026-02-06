"""
Prompt Enhancer - NVIDIA-Powered Image Prompt Improvement
=========================================================
Use NVIDIA's LLMs to enhance simple prompts for better image generation.
"""

import sys
from pathlib import Path

import requests

# Add project root to path for shared imports
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from shared import get_settings

# Recommended LLMs for prompt enhancement
PROMPT_MODELS = {
    "llama_8b": "meta/llama-3.1-8b-instruct",  # Fast, good quality
    "llama_70b": "meta/llama-3.1-70b-instruct",  # High quality
    "nemotron_70b": "nvidia/llama-3.1-nemotron-70b-instruct",  # NVIDIA optimized
    "deepseek_v3": "deepseek-ai/deepseek-v3.2",  # Strong reasoning
    "gemma_27b": "google/gemma-2-27b-it",  # Good balance
}


def enhance_prompt(simple_prompt, model="meta/llama-3.1-8b-instruct", style="detailed"):
    """
    Enhance a simple prompt for better image generation.

    Args:
        simple_prompt: Basic prompt to enhance
        model: NVIDIA LLM model to use for enhancement
        style: Enhancement style (detailed, artistic, photorealistic, cinematic)

    Returns:
        Enhanced prompt or None if failed
    """
    settings = get_settings()

    if not settings.nvidia_api_key:
        print("❌ Error: NVIDIA_API_KEY not found in .env file")
        return None

    # API endpoint for chat completions
    base_url = "https://integrate.api.nvidia.com/v1"
    url = f"{base_url}/chat/completions"

    # Style-specific instructions
    style_instructions = {
        "detailed": "Add specific details about textures, lighting, colors, and composition.",
        "artistic": "Focus on artistic style, brushwork, color palette, and artistic techniques.",
        "photorealistic": "Emphasize photorealistic qualities, camera settings, lighting, and realistic details.",
        "cinematic": "Add cinematic elements like camera angles, lighting, mood, and film-like qualities.",
    }

    instruction = style_instructions.get(style, style_instructions["detailed"])

    # System prompt for the LLM
    system_prompt = f"""You are an expert at writing prompts for AI image generation.
Your task is to enhance simple prompts to create more detailed, vivid, and effective image generation prompts.

Guidelines:
1. Keep the core idea from the original prompt
2. Add specific details about the subject, setting, and atmosphere
3. Include lighting, color, and composition details
4. {instruction}
5. Keep the prompt concise but descriptive (under 200 words)
6. Output ONLY the enhanced prompt, no explanations or extra text"""

    # Request headers
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json",
    }

    # Request body
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Enhance this prompt for image generation: {simple_prompt}",
            },
        ],
        "max_tokens": 300,
        "temperature": 0.7,
    }

    try:
        print(f"✨ Enhancing prompt with {model}...")
        print(f"   Style: {style}")

        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        # Parse response
        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            enhanced = result["choices"][0]["message"]["content"].strip()
            print("✅ Enhancement complete!")
            return enhanced
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


def generate_variations(
    base_prompt, num_variations=3, model="meta/llama-3.1-8b-instruct"
):
    """
    Generate multiple variations of a prompt.

    Args:
        base_prompt: Original prompt to vary
        num_variations: Number of variations to generate
        model: NVIDIA LLM model to use

    Returns:
        List of prompt variations
    """
    settings = get_settings()

    if not settings.nvidia_api_key:
        print("❌ Error: NVIDIA_API_KEY not found in .env file")
        return []

    # API endpoint for chat completions
    base_url = "https://integrate.api.nvidia.com/v1"
    url = f"{base_url}/chat/completions"

    # System prompt
    system_prompt = f"""Generate {num_variations} different creative variations of the given image generation prompt.
Each variation should:
1. Keep the core concept
2. Change the style, mood, or perspective
3. Add unique details
4. Be concise and effective

Output each variation on a separate line, numbered 1-{num_variations}."""

    # Request headers
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json",
    }

    # Request body
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Generate variations of: {base_prompt}"},
        ],
        "max_tokens": 500,
        "temperature": 0.9,
    }

    try:
        print(f"🎨 Generating {num_variations} variations...")

        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        # Parse response
        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            content = result["choices"][0]["message"]["content"].strip()

            # Parse numbered list
            variations = []
            for line in content.split("\n"):
                line = line.strip()
                if line and (line[0].isdigit() or line.startswith("-")):
                    # Remove number/bullet and clean up
                    clean_line = line.split(".", 1)[-1].split("-", 1)[-1].strip()
                    if clean_line:
                        variations.append(clean_line)

            print(f"✅ Generated {len(variations)} variations!")
            return variations
        else:
            print("❌ No response from model")
            return []

    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        return []
    except Exception as e:
        print(f"❌ Error: {e}")
        return []


def main():
    """Run prompt enhancement examples."""
    print("=" * 70)
    print("PROMPT ENHANCER - NVIDIA-POWERED IMAGE PROMPT IMPROVEMENT")
    print("=" * 70)
    print()

    # Example 1: Simple to detailed
    print("--- Example 1: Simple to Detailed ---")
    simple_prompt1 = "A cat sitting on a windowsill"
    print(f"📝 Original: {simple_prompt1}")
    print()

    enhanced1 = enhance_prompt(
        simple_prompt1, model=PROMPT_MODELS["llama_8b"], style="detailed"
    )
    if enhanced1:
        print(f"✨ Enhanced: {enhanced1}")
    print()

    # Example 2: Artistic style
    print("--- Example 2: Artistic Style Enhancement ---")
    simple_prompt2 = "A mountain landscape"
    print(f"📝 Original: {simple_prompt2}")
    print()

    enhanced2 = enhance_prompt(
        simple_prompt2, model=PROMPT_MODELS["llama_8b"], style="artistic"
    )
    if enhanced2:
        print(f"✨ Enhanced (Artistic): {enhanced2}")
    print()

    # Example 3: Photorealistic style
    print("--- Example 3: Photorealistic Style Enhancement ---")
    simple_prompt3 = "A portrait of a woman"
    print(f"📝 Original: {simple_prompt3}")
    print()

    enhanced3 = enhance_prompt(
        simple_prompt3, model=PROMPT_MODELS["llama_8b"], style="photorealistic"
    )
    if enhanced3:
        print(f"✨ Enhanced (Photorealistic): {enhanced3}")
    print()

    # Example 4: Generate variations
    print("--- Example 4: Generate Multiple Variations ---")
    base_prompt = "A futuristic city at night"
    print(f"📝 Base: {base_prompt}")
    print()

    variations = generate_variations(
        base_prompt, num_variations=3, model=PROMPT_MODELS["llama_8b"]
    )
    if variations:
        for i, variation in enumerate(variations, 1):
            print(f"   Variation {i}: {variation}")
    print()

    # Example 5: Compare different models
    print("--- Example 5: Compare Different NVIDIA Models ---")
    test_prompt = "A cozy coffee shop interior"
    print(f"📝 Original: {test_prompt}")
    print()

    for model_name, model_id in PROMPT_MODELS.items():
        print(f"🤖 Model: {model_name}")
        enhanced = enhance_prompt(test_prompt, model=model_id, style="detailed")
        if enhanced:
            print(f"   {enhanced}")
        print()

    print("=" * 70)
    print("✨ All examples completed!")
    print()
    print("💡 Tip: Use these enhanced prompts with nvidia_image_gen.py")
    print("   for better image generation results!")
    print("=" * 70)


if __name__ == "__main__":
    main()
