"""Prompt chaining: break one task into simple steps."""

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

note = "Customer says checkout is slow, payment fails on mobile, and error messages are unclear."

step1 = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": f"Extract the 3 distinct issues from this note as bullets: {note}",
        }
    ],
    temperature=0,
    max_tokens=120,
).choices[0].message.content

step2 = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": f"Prioritize these issues as High/Medium/Low with one line reason each:\n{step1}",
        }
    ],
    temperature=0,
    max_tokens=140,
).choices[0].message.content

step3 = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": f"Write a concise action plan from this prioritization:\n{step2}",
        }
    ],
    temperature=0.2,
    max_tokens=140,
).choices[0].message.content

print("Step 1: Extract")
print(step1)
print("\nStep 2: Prioritize")
print(step2)
print("\nStep 3: Action Plan")
print(step3)
