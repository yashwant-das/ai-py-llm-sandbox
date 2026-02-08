# 05. Embeddings & RAG

Retrieval-Augmented Generation (RAG) allows LLMs to "see" your private data.

## Concepts

1.  **Embeddings**: Converting text into numbers (vectors) that represent meaning.
2.  **Vector Store**: A database specialized for searching these vectors (e.g., FAISS, Chroma).
3.  **RAG**: The flow of: `Query -> Search Vector DB -> Retrieve Context -> Prompt LLM with Context`.

## Structure

*   **`code/`**: Basic embedding generation and similarity search.
*   **`rag/`**: Full RAG pipeline examples (Ingestion, Retrieval, Generation).
*   **`datasets/`**: Sample data for experiments.

## Examples

```bash
# Generate Embeddings
uv run python 05_embeddings_rag/code/01_generate_embeddings.py

# Semantic Search
uv run python 05_embeddings_rag/code/02_semantic_search.py

# RAG Output (if implemented)
# uv run python 05_embeddings_rag/rag/01_basic_rag.py
```
