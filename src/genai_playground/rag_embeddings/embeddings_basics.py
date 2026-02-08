"""Embeddings basics: rank documents by vector similarity.

Recommended embedding models:
- OpenAI: text-embedding-3-small
- NVIDIA: nvidia/nv-embedqa-e5-v5 (if available)
- Ollama: nomic-embed-text
"""

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
MODEL = os.getenv("LLM_EMBEDDING_MODEL", "text-embedding-3-small")


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb)


docs = [
    "Use indexes to speed up SQL WHERE lookups.",
    "Caching reduces repeated database reads.",
    "Gradient descent updates model parameters.",
]
query = "How can I make database queries faster?"

resp = client.embeddings.create(model=MODEL, input=docs + [query])
vectors = [item.embedding for item in resp.data]
doc_vecs, query_vec = vectors[:-1], vectors[-1]

scores = [(doc, cosine(vec, query_vec)) for doc, vec in zip(docs, doc_vecs)]
for doc, score in sorted(scores, key=lambda x: x[1], reverse=True):
    print(f"{score:.4f} | {doc}")
