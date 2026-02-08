"""
Token Counting Experiment
=========================
Understand how text is converted to tokens (the unit LLMs process).

This uses the raw tiktoken library (what OpenAI uses internally).
No shared modules, no .env - just direct learning.

Concepts:
- Tokens vs characters vs words
- Different models use different tokenizers
- Why token limits matter
"""

import tiktoken

print("=" * 70)
print("TOKEN COUNTING EXPERIMENT")
print("=" * 70)

# Sample texts to analyze
texts = [
    "Hello world",
    "The quick brown fox jumps over the lazy dog",
    "GPT-4 is a large language model trained by OpenAI",
    "Programming in Python is fun! 🐍",
    "The price is $42.50",
]

# Different encoders for different models
encoders = {
    "GPT-4 / GPT-3.5": tiktoken.get_encoding("cl100k_base"),
    "GPT-3": tiktoken.get_encoding("p50k_base"),
}

print("\n1. BASIC TOKENIZATION")
print("-" * 70)

for text in texts:
    encoder = encoders["GPT-4 / GPT-3.5"]
    tokens = encoder.encode(text)

    print(f"\nText: '{text}'")
    print(f"  Characters: {len(text)}")
    print(f"  Words: {len(text.split())}")
    print(f"  Tokens: {len(tokens)}")
    print(f"  Token IDs: {tokens}")
    print(f"  Tokens -> Text: {[encoder.decode([t]) for t in tokens]}")


print("\n\n2. TOKENIZER COMPARISON")
print("-" * 70)

test_text = "Hello world! This is a test."

for name, encoder in encoders.items():
    tokens = encoder.encode(test_text)
    print(f"\n{name}:")
    print(f"  Tokens: {len(tokens)}")
    print(f"  Breakdown: {[encoder.decode([t]) for t in tokens]}")


print("\n\n3. CONTEXT WINDOW VISUALIZATION")
print("-" * 70)

# Typical context window sizes
context_windows = {
    "GPT-3.5": 4096,
    "GPT-4": 8192,
    "GPT-4 Turbo": 128000,
}

# A "page" of text is roughly 500 words ~ 750 tokens
words_per_page = 500
tokens_per_page = 750

print(f"\nAssuming ~{tokens_per_page} tokens per page (500 words):")

for model, window in context_windows.items():
    pages = window / tokens_per_page
    print(f"\n{model}:")
    print(f"  Context window: {window:,} tokens")
    print(f"  Equivalent to: ~{pages:.1f} pages of text")


print("\n\n4. PRACTICAL EXAMPLE: FITTING IN CONTEXT")
print("-" * 70)

encoder = encoders["GPT-4 / GPT-3.5"]

# Simulate a conversation
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain quantum computing in simple terms."},
    {
        "role": "assistant",
        "content": "Quantum computing uses quantum mechanics principles...",
    },
]

# Count tokens in conversation
system_tokens = encoder.encode(conversation[0]["content"])
user_tokens = encoder.encode(conversation[1]["content"])
assistant_tokens = encoder.encode(conversation[2]["content"])

# Rough estimate (actual API includes role tokens, format tokens)
estimated_total = len(system_tokens) + len(user_tokens) + len(assistant_tokens) + 10

print("\nConversation token estimate:")
print(f"  System message: {len(system_tokens)} tokens")
print(f"  User message: {len(user_tokens)} tokens")
print(f"  Assistant message: {len(assistant_tokens)} tokens")
print("  Format overhead: ~10 tokens")
print(f"  TOTAL: ~{estimated_total} tokens")
print(f"  Remaining in 4K context: ~{4096 - estimated_total} tokens")


print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. Tokens != Words: 1 word ≈ 1.3 tokens (English average)
2. Short words may be 1 token, long words may be 2-3 tokens
3. Punctuation and spaces are tokens too
4. Different models may tokenize slightly differently
5. Context windows limit how much text you can process
6. Pricing is per token, so shorter prompts = cheaper
""")
