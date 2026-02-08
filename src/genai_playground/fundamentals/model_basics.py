"""First chat completion call.

Recommended models:
- OpenAI: gpt-4o-mini
- NVIDIA: meta/llama-3.1-8b-instruct
- Ollama: llama3.1:8b (via local_inference/ollama_demo.py)
"""

from __future__ import annotations

import os
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

messages = [
    {"role": "system", "content": "You are a concise technical tutor."},
    {
        "role": "user",
        "content": "Explain in 3 bullets what tokens are in LLMs.",
    },
]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    temperature=0.2,
    max_tokens=180,
)

print("Model:", MODEL)
print("\nResponse:\n")
print(response.choices[0].message.content)
if response.usage:
    print("\nToken usage:")
    print("prompt_tokens:", response.usage.prompt_tokens)
    print("completion_tokens:", response.usage.completion_tokens)
    print("total_tokens:", response.usage.total_tokens)
