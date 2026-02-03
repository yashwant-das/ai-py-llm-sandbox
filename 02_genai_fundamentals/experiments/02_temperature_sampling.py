"""
Temperature and Sampling Experiment
====================================
See how temperature affects LLM output randomness.

Uses raw OpenAI SDK directly. Configure your endpoint below.

Concepts:
- Temperature (0.0 = deterministic, 1.0+ = creative)
- Sampling strategies
- Reproducibility vs creativity
"""

from openai import OpenAI

# Configure your endpoint here (no .env needed)
# Option 1: LM Studio
BASE_URL = "http://127.0.0.1:1234/v1"
API_KEY = "lm-studio"
MODEL = "openai/gpt-oss-20b"  # or whatever model you loaded

# Option 2: Ollama (uncomment if using)
# BASE_URL = "http://localhost:11434/v1"
# API_KEY = "ollama"
# MODEL = "llama3.1"

# Option 3: OpenAI (uncomment if using)
# BASE_URL = "https://api.openai.com/v1"
# API_KEY = "sk-your-key-here"
# MODEL = "gpt-4o-mini"

print("=" * 70)
print("TEMPERATURE AND SAMPLING EXPERIMENT")
print("=" * 70)
print(f"Endpoint: {BASE_URL}")
print(f"Model: {MODEL}")
print()

# Initialize client
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


def get_completion(prompt, temperature, n=1):
    """Get completion with specified temperature."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=50,
        n=n,  # Number of completions to generate
    )
    return [choice.message.content.strip() for choice in response.choices]


print("1. TEMPERATURE = 0.0 (Deterministic)")
print("-" * 70)
print("Same prompt, same output every time.\n")

prompt = "Complete this sentence: The color of the sky is"
for i in range(3):
    responses = get_completion(prompt, temperature=0.0)
    print(f"  Run {i+1}: {responses[0]}")


print("\n\n2. TEMPERATURE = 0.7 (Balanced)")
print("-" * 70)
print("Some variation, but generally coherent.\n")

prompt = "Name a creative ice cream flavor:"
for i in range(5):
    responses = get_completion(prompt, temperature=0.7)
    print(f"  Run {i+1}: {responses[0]}")


print("\n\n3. TEMPERATURE = 1.5 (Creative/Random)")
print("-" * 70)
print("High variation, potentially less coherent.\n")

prompt = "Complete: Once upon a time"
for i in range(5):
    responses = get_completion(prompt, temperature=1.5)
    print(f"  Run {i+1}: {responses[0][:80]}...")


print("\n\n4. MULTIPLE SAMPLES AT SAME TEMPERATURE")
print("-" * 70)
print("Generate 5 completions at once with temperature=0.8\n")

prompt = "A good name for a pet cat:"
responses = get_completion(prompt, temperature=0.8, n=5)
for i, response in enumerate(responses, 1):
    print(f"  Sample {i}: {response}")


print("\n\n5. TASK-APPROPRIATE TEMPERATURES")
print("-" * 70)

tasks = [
    ("What is 15 × 23?", 0.0, "Math/Facts"),
    ("Write a haiku about coding", 0.7, "Creative writing"),
    ("Generate 3 random words", 1.0, "Brainstorming"),
    ("Classify: 'I love this product!' (positive/negative)", 0.0, "Classification"),
]

for prompt, temp, category in tasks:
    responses = get_completion(prompt, temperature=temp)
    print(f"\n{category} (temp={temp}):")
    print(f"  Prompt: {prompt}")
    print(f"  Response: {responses[0]}")


print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. Temperature 0.0: Deterministic, repeatable, good for facts
2. Temperature 0.7: Balanced, creative but coherent
3. Temperature 1.0+: High creativity, may drift off-topic
4. Math/Code/Facts: Use low temperature (0.0-0.3)
5. Creative writing: Use higher temperature (0.7-1.0)
6. Sampling: Generate multiple (n>1) and pick the best

RULE OF THUMB:
- If there's a "right answer", use low temp
- If there are many "good answers", use higher temp
""")
