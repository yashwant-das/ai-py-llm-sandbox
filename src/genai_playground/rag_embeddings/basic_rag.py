"""Minimal RAG: retrieve with embeddings, then answer with context."""

from __future__ import annotations

import math
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "unused")),
)
CHAT_MODEL = os.getenv("LLM_MODEL_ID", "meta/llama-3.1-8b-instruct")
EMBED_MODEL = os.getenv("LLM_EMBEDDING_MODEL", "text-embedding-3-small")


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb)


knowledge = [
    "JWT access tokens should be short-lived and signed.",
    "Refresh tokens should be stored securely and rotated.",
    "Never store plaintext passwords; hash with bcrypt or Argon2.",
]
question = "How should I manage user session tokens securely?"

embed_resp = client.embeddings.create(model=EMBED_MODEL, input=knowledge + [question])
vectors = [x.embedding for x in embed_resp.data]
knowledge_vecs, q_vec = vectors[:-1], vectors[-1]

ranked = sorted(
    zip(knowledge, knowledge_vecs),
    key=lambda x: cosine(x[1], q_vec),
    reverse=True,
)
context = "\n".join([item[0] for item in ranked[:2]])

prompt = f"""Answer using only this context.

Context:
{context}

Question: {question}
"""

chat_resp = client.chat.completions.create(
    model=CHAT_MODEL,
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    max_tokens=140,
)

print("Retrieved context:")
print(context)
print("\nAnswer:")
print(chat_resp.choices[0].message.content)
