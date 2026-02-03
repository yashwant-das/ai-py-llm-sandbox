"""
Model Comparison Experiment
===========================
Compare how different models or settings respond to the same prompts.

Uses raw OpenAI SDK. Configure multiple endpoints to compare.

Concepts:
- Model capabilities
- Speed vs quality trade-offs
- Consistency across models
"""

from openai import OpenAI
import time

# Configure endpoints to compare
# Add or remove as needed - these are examples

ENDPOINTS = {
    "LM Studio": {
        "base_url": "http://127.0.0.1:1234/v1",
        "api_key": "lm-studio",
        "model": "openai/gpt-oss-20b",
    },
    # Uncomment to add Ollama comparison:
    # "Ollama": {
    #     "base_url": "http://localhost:11434/v1",
    #     "api_key": "ollama",
    #     "model": "llama3.1",
    # },
}

print("=" * 70)
print("MODEL COMPARISON EXPERIMENT")
print("=" * 70)
print(f"Configured endpoints: {list(ENDPOINTS.keys())}")
print()


def test_endpoint(name, config, prompt, max_tokens=100):
    """Test a single endpoint."""
    client = OpenAI(
        base_url=config["base_url"],
        api_key=config["api_key"],
    )
    
    start = time.time()
    try:
        response = client.chat.completions.create(
            model=config["model"],
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
    """Run prompt against all configured endpoints."""
    print(f"\n{'='*70}")
    print(f"TEST: {title}")
    print(f"Prompt: {prompt}")
    print(f"{'='*70}\n")
    
    results = {}
    for name, config in ENDPOINTS.items():
        print(f"{name}... ", end="", flush=True)
        result = test_endpoint(name, config, prompt, max_tokens)
        results[name] = result
        
        if result["success"]:
            print(f"✓ ({result['time']:.2f}s)")
        else:
            print(f"✗ Error: {result['error'][:50]}")
    
    # Display results side by side
    print(f"\n{'-'*70}")
    print("RESULTS:")
    print(f"{'-'*70}")
    
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
compare_all(
    "What is the capital of Japan?",
    "Simple Fact",
    max_tokens=50
)


# Test 2: Reasoning
compare_all(
    "If a train travels 60 km in 30 minutes, what is its speed in km/h?",
    "Math Reasoning",
    max_tokens=100
)


# Test 3: Creative writing
compare_all(
    "Write a one-sentence story about a robot learning to paint.",
    "Creative Writing",
    max_tokens=100
)


# Test 4: Instruction following
compare_all(
    "List three fruits. Format: 1. fruit 2. fruit 3. fruit",
    "Instruction Following",
    max_tokens=50
)


# Test 5: Code generation
compare_all(
    "Write a Python function that reverses a string.",
    "Code Generation",
    max_tokens=150
)


print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
Things to observe when comparing models:

1. SPEED
   - Time to first token (perceived responsiveness)
   - Total generation time
   - Tokens per second

2. QUALITY
   - Accuracy of facts
   - Coherence of reasoning
   - Following instructions precisely
   - Code correctness

3. STYLE
   - Verbosity (concise vs verbose)
   - Tone (formal vs casual)
   - Confidence calibration

4. RELIABILITY
   - Error rates
   - Consistency across runs
   - Handling of edge cases

TIPS:
- Run multiple times for consistency check
- Test with your actual use cases
- Consider speed vs quality trade-off
- Test with long contexts if that's your use case
""")
