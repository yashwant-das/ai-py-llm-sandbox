"""Streaming basics: compare blocking vs streamed output."""

from __future__ import annotations

import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("LLM_MODEL_ID", "meta/llama-3.1-8b-instruct")
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "unused")),
)

prompt = "Explain HTTP vs HTTPS in 4 short bullets."

print("Non-streaming")
print("-" * 50)
start = time.time()
resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    stream=False,
)
print(resp.choices[0].message.content)
print(f"Total time: {time.time() - start:.2f}s")

print("\nStreaming")
print("-" * 50)
start = time.time()
first_token = None
stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        if first_token is None:
            first_token = time.time() - start
        print(delta, end="", flush=True)
print()
print(f"Time to first token: {first_token:.2f}s")
print(f"Total time: {time.time() - start:.2f}s")
