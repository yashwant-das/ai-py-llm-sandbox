"""
Context Window and Token Limits Experiment
==========================================
Demonstrate how context windows work and what happens when you exceed them.

Uses raw OpenAI SDK via NVIDIA API.

Concepts:
- Context window size
- Token overflow handling
- Input vs output tokens
"""

import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

DEFAULT_MODEL = "meta/llama-3.1-405b-instruct"

print(f"Model: {DEFAULT_MODEL}")
print()


def count_tokens_approx(text):
    """Rough estimation: ~4 characters per token."""
    return len(text) // 4


def make_request(messages, max_tokens=100):
    """Make a chat completion request."""
    start = time.time()
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=messages,
        max_tokens=max_tokens,
    )
    elapsed = time.time() - start
    return response, elapsed


print("1. SHORT CONVERSATION")
print("-" * 70)

short_messages = [{"role": "user", "content": "What is 2+2?"}]

response, elapsed = make_request(short_messages)
approx_input = count_tokens_approx(short_messages[0]["content"])
approx_output = count_tokens_approx(response.choices[0].message.content)

print(f"Input: '{short_messages[0]['content']}'")
print(f"Approx input tokens: {approx_input}")
print(f"Response: {response.choices[0].message.content}")
print(f"Approx output tokens: {approx_output}")
print(f"Time: {elapsed:.2f}s")


print("\n\n2. INCREASING CONTEXT SIZE")
print("-" * 70)

base_question = "Summarize the following in 5 words:"
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "The quick brown fox jumps over the lazy dog. " * 10,
    "The quick brown fox jumps over the lazy dog. " * 50,
]

for text in texts:
    messages = [{"role": "user", "content": f"{base_question}\n\n{text}"}]
    approx_tokens = count_tokens_approx(messages[0]["content"])

    try:
        response, elapsed = make_request(messages)
        print(f"\nApprox {approx_tokens} tokens:")
        print(f"  Response: {response.choices[0].message.content}")
        print(f"  Time: {elapsed:.2f}s")
    except Exception as e:
        print(f"\nApprox {approx_tokens} tokens:")
        print(f"  ERROR: {e}")


print("\n\n3. MAX_TOKENS PARAMETER")
print("-" * 70)
print("Controlling output length\n")

prompt = "List the first 20 prime numbers:"

for max_tok in [20, 50, 100]:
    response, _ = make_request(
        [{"role": "user", "content": prompt}], max_tokens=max_tok
    )
    content = response.choices[0].message.content
    print(f"max_tokens={max_tok}:")
    print(f"  Output: {content[:60]}...")
    print(
        f"  Length: {len(content)} chars (approx {count_tokens_approx(content)} tokens)"
    )
    print()


print("\n4. CONVERSATION HISTORY ACCUMULATION")
print("-" * 70)
print("Simulating a multi-turn conversation\n")

conversation = []
questions = [
    "What is the capital of France?",
    "What is its population?",
    "What is the currency there?",
    "What about the time zone?",
]

total_approx_tokens = 0

for i, question in enumerate(questions, 1):
    conversation.append({"role": "user", "content": question})

    # Approximate tokens in conversation so far
    convo_text = " ".join([m["content"] for m in conversation])
    approx_tokens = count_tokens_approx(convo_text)
    total_approx_tokens += approx_tokens

    response, elapsed = make_request(conversation, max_tokens=50)
    answer = response.choices[0].message.content

    conversation.append({"role": "assistant", "content": answer})

    print(f"Turn {i}:")
    print(f"  Q: {question}")
    print(f"  A: {answer[:50]}...")
    print(f"  Approx context so far: {total_approx_tokens} tokens")
    print()


print("5. CONTEXT WINDOW TRADE-OFFS")
print("-" * 70)
print("""
Model Context Windows:
- Llama 3.1 405B: 128k tokens
- GPT-4o: 128k tokens
- Claude 3.5: 200k tokens

Trade-offs:
- Larger window = more context but slower/more expensive
- Small window = faster but forgets earlier conversation
- Input + Output must fit in window

Strategies for long contexts:
1. Summarize older messages
2. Use retrieval (RAG) instead of putting everything in context
3. Selective inclusion of relevant history
""")


print("=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. Context window = input tokens + output tokens
2. Exceeding limit causes errors or truncation
3. max_tokens controls output size, not input
4. Longer context = slower inference
5. Conversation history accumulates - manage it actively
6. Different models have different limits
""")
