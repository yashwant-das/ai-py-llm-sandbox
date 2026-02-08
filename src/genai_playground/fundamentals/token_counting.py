"""Token counting fundamentals with tiktoken."""

from __future__ import annotations

import tiktoken

ENCODING = tiktoken.get_encoding("cl100k_base")

samples = [
    "Hello world",
    "The quick brown fox jumps over the lazy dog.",
    "Write clean prompts for better model output.",
]

print("Token counting with cl100k_base")
print("-" * 50)

for text in samples:
    tokens = ENCODING.encode(text)
    print(f"\nText: {text}")
    print(f"chars: {len(text)} | words: {len(text.split())} | tokens: {len(tokens)}")
    print("token_ids:", tokens)


def estimate_chat_budget(context_window: int, reserve_for_output: int = 512) -> int:
    return max(0, context_window - reserve_for_output)

print("\nBudget example")
print("-" * 50)
print("Model context window: 8,192")
print("Reserved output tokens: 512")
print("Safe input budget:", estimate_chat_budget(8192, 512))
