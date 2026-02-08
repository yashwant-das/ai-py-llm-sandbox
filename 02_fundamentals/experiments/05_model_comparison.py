"""
Model Comparison Experiment
===========================
Compare how different models respond to the same prompts.

Uses raw OpenAI SDK via NVIDIA API to compare different NVIDIA-hosted models.

Concepts:
- Model capabilities
- Speed vs quality trade-offs
- Consistency across models
"""

import sys
from pathlib import Path
import time

# Add project root to path for shared imports
project_root = str(Path(__file__).parent.parent.parent.absolute())
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from shared import get_nvidia_client, get_settings

print("=" * 70)
print("MODEL COMPARISON EXPERIMENT (NVIDIA API)")
print("=" * 70)

# Initialize client
client = get_nvidia_client()
settings = get_settings()

# Define models to compare
# These should be models available in your NVIDIA account / credits
MODELS = {
    "Llama 3 405B": "meta/llama-3.1-405b-instruct",
    "Llama 3 8B": "meta/llama-3.1-8b-instruct",
    "Nemotron 70B": "nvidia/llama-3.1-nemotron-70b-instruct",
}

print(f"Comparing models: {list(MODELS.keys())}")
print()


def test_model(name, model_id, prompt, max_tokens=100):
    """Test a single model."""
    start = time.time()
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        elapsed = time.time() - start

        content = response.choices[0].message.content
        tokens = response.usage.completion_tokens if response.usage else "?"

        return {
            "success": True,
            "content": content,
            "time": elapsed,
            "tokens": tokens,
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "success": False,
            "error": str(e),
            "time": elapsed,
        }


def compare_all(prompt, title, max_tokens=100):
    """Run prompt against all configured models."""
    print(f"\n{'=' * 70}")
    print(f"TEST: {title}")
    print(f"Prompt: {prompt}")
    print(f"{'=' * 70}\n")

    results = {}
    for name, model_id in MODELS.items():
        print(f"{name}... ", end="", flush=True)
        result = test_model(name, model_id, prompt, max_tokens)
        results[name] = result

        if result["success"]:
            print(f"✓ ({result['time']:.2f}s)")
        else:
            print(f"✗ Error: {result['error'][:50]}")

    # Display results side by side
    print(f"\n{'-' * 70}")
    print("RESULTS:")
    print(f"{'-' * 70}")

    for name, result in results.items():
        print(f"\n{name}:")
        if result["success"]:
            print(f"  Time: {result['time']:.2f}s")
            print(f"  Tokens: {result['tokens']}")
            print(f"  Response: {result['content'][:200]}...")
        else:
            print(f"  ERROR: {result['error']}")

    return results


# Test 1: Simple factual question
compare_all("What is the capital of Japan?", "Simple Fact", max_tokens=50)


# Test 2: Reasoning
compare_all(
    "If a train travels 60 km in 30 minutes, what is its speed in km/h?",
    "Math Reasoning",
    max_tokens=100,
)


# Test 3: Creative writing
compare_all(
    "Write a one-sentence story about a robot learning to paint.",
    "Creative Writing",
    max_tokens=100,
)


# Test 4: Instruction following
compare_all(
    "List three fruits. Format: 1. fruit 2. fruit 3. fruit",
    "Instruction Following",
    max_tokens=50,
)


# Test 5: Code generation
compare_all(
    "Write a Python function that reverses a string.", "Code Generation", max_tokens=150
)


print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
Things to observe when comparing models:

1. SPEED
   - Time to first token (perceived responsiveness)
   - Total generation time

2. QUALITY
   - Accuracy of facts
   - Coherence of reasoning
   - Following instructions precisely

3. RELIABILITY
   - Error rates
   - Consistency across runs
""")
