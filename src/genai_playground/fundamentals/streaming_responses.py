"""Streaming basics: compare blocking vs streamed output."""

from __future__ import annotations

import os
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


MODEL = require_env("LLM_MODEL_ID")
client = OpenAI(
    base_url=require_env("LLM_BASE_URL"),
    api_key=require_env("LLM_API_KEY"),
)

prompt = "Explain HTTP vs HTTPS in 4 short bullets."

print("Non-streaming")
print("-" * 50)
start = time.time()
resp = client.chat.completions.create(
    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
    model=MODEL,
    messages=[
        {"role": "system", "content": "Return only the final answer. Do not include reasoning text."},
        {"role": "user", "content": prompt},
    ],
    stream=False,
)
print(resp.choices[0].message.content)
print(f"Total time: {time.time() - start:.2f}s")

print("\nStreaming")
print("-" * 50)
start = time.time()
first_token = None
stream = client.chat.completions.create(
    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
    model=MODEL,
    messages=[
        {"role": "system", "content": "Return only the final answer. Do not include reasoning text."},
        {"role": "user", "content": prompt},
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta.content
    if delta:
        if first_token is None:
            first_token = time.time() - start
        print(delta, end="", flush=True)
print()
if first_token is not None:
    print(f"Time to first token: {first_token:.2f}s")
else:
    print("Time to first token: not available (no delta chunks received)")
print(f"Total time: {time.time() - start:.2f}s")
