"""
Streaming Responses Experiment
==============================
See how streaming gives partial results before completion.

Uses raw OpenAI SDK with streaming enabled. No shared modules.

Concepts:
- Streaming vs non-streaming
- Real-time display
- Perceived performance
"""

from openai import OpenAI
import time

# Configure your endpoint
BASE_URL = "http://127.0.0.1:1234/v1"
API_KEY = "lm-studio"
MODEL = "openai/gpt-oss-20b"

# Option 2: Ollama
# BASE_URL = "http://localhost:11434/v1"
# API_KEY = "ollama"
# MODEL = "llama3.1"

print("=" * 70)
print("STREAMING RESPONSES EXPERIMENT")
print("=" * 70)
print(f"Endpoint: {BASE_URL}")
print(f"Model: {MODEL}")
print()

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


print("1. NON-STREAMING (Default)")
print("-" * 70)
print("Waits for entire response before showing anything.\n")

prompt = "Explain photosynthesis in 3 sentences."

start = time.time()
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    stream=False,  # Default
)
elapsed = time.time() - start

print(f"Prompt: {prompt}")
print(f"Response: {response.choices[0].message.content}")
print(f"Time to first token: ~{elapsed:.2f}s (waited for all)")
print(f"Total time: {elapsed:.2f}s")


print("\n\n2. STREAMING")
print("-" * 70)
print("Shows tokens as they arrive. Better UX!\n")

start = time.time()
first_token_time = None

stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    stream=True,  # Enable streaming
)

print(f"Prompt: {prompt}")
print("Response: ", end="", flush=True)

full_response = ""
for chunk in stream:
    if chunk.choices[0].delta.content:
        content = chunk.choices[0].delta.content
        print(content, end="", flush=True)
        full_response += content
        
        if first_token_time is None:
            first_token_time = time.time() - start

elapsed = time.time() - start

print()  # Newline
print(f"Time to first token: {first_token_time:.2f}s")
print(f"Total time: {elapsed:.2f}s")


print("\n\n3. STREAMING WITH METADATA")
print("-" * 70)
print("Accessing chunk metadata during streaming.\n")

prompt = "Count from 1 to 5."

stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    stream=True,
)

print(f"Prompt: {prompt}")
print("\nChunks received:")
print(f"{'#':<4} {'Content':<15} {'Finish Reason'}")
print("-" * 40)

chunk_num = 0
for chunk in stream:
    chunk_num += 1
    content = chunk.choices[0].delta.content or ""
    finish = chunk.choices[0].finish_reason or ""
    display_content = repr(content) if content else "(empty)"
    print(f"{chunk_num:<4} {display_content:<15} {finish}")


print("\n\n4. STREAMING USE CASES")
print("-" * 70)
print("""
When to use streaming:
- Chat applications (shows typing effect)
- Long-form content (user sees progress)
- Real-time applications

When NOT to use streaming:
- Need complete response for processing
- Simple/short responses
- Backend processing without user waiting
""")


print("\n\n5. SIMPLE STREAMING WRAPPER")
print("-" * 70)
print("A reusable pattern for your applications.\n")

def stream_completion(prompt, model=MODEL):
    """Stream a completion with simple output."""
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    
    print(f"Q: {prompt}")
    print("A: ", end="", flush=True)
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    
    print()


# Demo the wrapper
stream_completion("What is the speed of light?")
print()
stream_completion("Name three benefits of exercise.")


print("\n" + "=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. Streaming: stream=True in API call
2. Iterate over chunks, each contains partial text
3. chunk.choices[0].delta.content has the new text
4. Great UX - users see response build up
5. First token latency is what users perceive as "speed"
6. Slightly more complex code but worth it for interactivity
""")
