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
        doc_resp = client.embeddings.create(
            model=EMBED_MODEL, input=knowledge, extra_body={"input_type": "passage"}
        )
        query_resp = client.embeddings.create(
            model=EMBED_MODEL, input=[question], extra_body={"input_type": "query"}
        )
        knowledge_vecs = [
            x.embedding for x in sorted(doc_resp.data, key=lambda x: x.index)
        ]
        q_vec = query_resp.data[0].embedding
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
            extra_body={"chat_template_kwargs": {"enable_thinking": False}},
            model=CHAT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Return only the final answer. Do not include reasoning text.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0,
            max_tokens=260,
        )
    except Exception as exc:
        print(f"Chat completion failed: {exc}")
        return 1

    print("Retrieved context:")
    print(context)
    print("\nAnswer:")
    print(chat_resp.choices[0].message.content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
