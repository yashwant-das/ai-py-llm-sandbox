"""Few-shot prompting: teach output pattern with examples."""

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

prompt = """Extract Name | Role from each sentence.

Sentence: Maya leads backend engineering.
Output: Maya | Backend Engineering Lead

Sentence: Ali manages hiring and onboarding.
Output: Ali | Hiring and Onboarding Manager

Sentence: Priya owns product analytics.
Output:"""

resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    max_tokens=80,
)

print(resp.choices[0].message.content)
