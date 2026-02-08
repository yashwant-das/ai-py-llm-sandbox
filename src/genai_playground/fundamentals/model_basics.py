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

MODEL = os.getenv("LLM_MODEL_ID", "meta/llama-3.1-8b-instruct")
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "unused")),
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
