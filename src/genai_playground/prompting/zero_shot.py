"""Zero-shot prompting: instruction only, no examples."""

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

prompt = "Classify sentiment as Positive, Neutral, or Negative: 'The onboarding was fast and clear.'"

resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    max_tokens=30,
)

print("Prompt:")
print(prompt)
print("\nModel output:")
print(resp.choices[0].message.content)
