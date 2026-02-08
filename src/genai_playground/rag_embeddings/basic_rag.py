"""Minimal RAG: retrieve with embeddings, then answer with context."""

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
CHAT_MODEL = require_env("LLM_MODEL_ID")
EMBED_MODEL = require_env("LLM_EMBEDDING_MODEL")


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb)


def keyword_rank(docs: list[str], query: str) -> list[str]:
    q = {w.lower().strip(".,?!") for w in query.split() if w.strip()}

    def score(doc: str) -> int:
        words = {w.lower().strip(".,?!") for w in doc.split() if w.strip()}
        return len(words.intersection(q))

    return sorted(docs, key=score, reverse=True)


def main() -> int:
    knowledge = [
        "JWT access tokens should be short-lived and signed.",
        "Refresh tokens should be stored securely and rotated.",
        "Never store plaintext passwords; hash with bcrypt or Argon2.",
    ]
    question = "How should I manage user session tokens securely?"

    ranked_docs: list[str]
    try:
        embed_resp = client.embeddings.create(model=EMBED_MODEL, input=knowledge + [question])
        vectors = [x.embedding for x in embed_resp.data]
        knowledge_vecs, q_vec = vectors[:-1], vectors[-1]
        ranked = sorted(
            zip(knowledge, knowledge_vecs),
            key=lambda x: cosine(x[1], q_vec),
            reverse=True,
        )
        ranked_docs = [item[0] for item in ranked]
        print(f"Retrieval mode: embeddings ({EMBED_MODEL})")
    except Exception as exc:
        print(f"Embedding retrieval unavailable ({exc})")
        print("Falling back to keyword retrieval.")
        ranked_docs = keyword_rank(knowledge, question)

    context = "\n".join(ranked_docs[:2])
    prompt = f"""Answer using only this context.

Context:
{context}

Question: {question}
"""

    try:
        chat_resp = client.chat.completions.create(
            model=CHAT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=140,
        )
    except Exception as exc:
        print(f"Chat completion failed: {exc}")
        return 0

    print("Retrieved context:")
    print(context)
    print("\nAnswer:")
    print(chat_resp.choices[0].message.content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
