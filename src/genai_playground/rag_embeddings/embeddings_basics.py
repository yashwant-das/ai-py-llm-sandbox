"""Embeddings basics: rank documents by vector similarity.

Recommended embedding models:
- OpenAI: text-embedding-3-small
- NVIDIA: nvidia/llama-3.2-nemoretriever-300m-embed-v2
- Ollama: nomic-embed-text
"""

from __future__ import annotations

import math
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


client = OpenAI(
    base_url=require_env("LLM_BASE_URL"),
    api_key=require_env("LLM_API_KEY"),
)
MODEL = require_env("LLM_EMBEDDING_MODEL")


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb)


def main() -> int:
    docs = [
        "Use indexes to speed up SQL WHERE lookups.",
        "Caching reduces repeated database reads.",
        "Gradient descent updates model parameters.",
    ]
    query = "How can I make database queries faster?"

    try:
        resp = client.embeddings.create(model=MODEL, input=docs + [query])
    except Exception as exc:
        print(f"Embedding endpoint unavailable for model '{MODEL}': {exc}")
        print("Set LLM_EMBEDDING_MODEL in .env to a model your provider supports.")
        return 0

    vectors = [item.embedding for item in resp.data]
    doc_vecs, query_vec = vectors[:-1], vectors[-1]

    scores = [(doc, cosine(vec, query_vec)) for doc, vec in zip(docs, doc_vecs)]
    for doc, score in sorted(scores, key=lambda x: x[1], reverse=True):
        print(f"{score:.4f} | {doc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
