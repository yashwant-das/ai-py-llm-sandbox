# Topic 9: Building Search Applications with Vector Databases

> Semantic search without full RAG: embeddings, similarity, and vector stores.

## Learning Objectives

By the end of this topic, you will:
- Understand vector embeddings and similarity
- Implement semantic search with FAISS
- Use persistent vector databases (Chroma)
- Combine keyword and semantic search (hybrid)

## Folder Structure

```
09_search_with_vectors/
├── README.md
├── notes/
│   ├── vector_embeddings_explained.md
│   └── similarity_metrics.md
├── code/
│   ├── 01_basic_semantic_search.py
│   ├── 02_faiss_indexing.py
│   ├── 03_chroma_integration.py
│   └── 04_hybrid_search.py
└── datasets/
    └── sample_documents.json
```

## Key Concepts

### Embeddings
- Text → Dense vector (typically 384-4096 dimensions)
- Similar texts have similar vectors
- Cosine similarity for comparison

### Vector Stores
| Store | Type | Best For |
|-------|------|----------|
| FAISS | In-memory | Prototyping, small datasets |
| Chroma | Persistent | Production apps |
| Pinecone | Cloud | Managed, scale |
| Weaviate | Self-hosted | Complex queries |

## Running Examples

```bash
# Basic semantic search
python 09_search_with_vectors/code/01_basic_semantic_search.py

# FAISS indexing
python 09_search_with_vectors/code/02_faiss_indexing.py

# Hybrid search
python 09_search_with_vectors/code/04_hybrid_search.py
```

## Cross-References

- **Previous**: [08_chat_applications/](../08_chat_applications/)
- **Next**: [16_rag_systems/](../16_rag_systems/) - Full RAG with generation
