# Topic 16: Retrieval-Augmented Generation (RAG) and Vector Databases

> Ground LLM outputs in external knowledge: ingestion, retrieval, generation.

## Learning Objectives

By the end of this topic, you will:
- Build end-to-end RAG pipelines
- Implement chunking strategies
- Evaluate RAG system quality
- Apply advanced techniques (reranking, hybrid search)

## Folder Structure

```
16_rag_systems/
├── README.md
├── fundamentals/
│   ├── 01_basic_rag_pipeline.py
│   ├── 02_chunking_strategies.py
│   ├── 03_embedding_models.py
│   └── 04_rag_evaluation.py
├── advanced/
│   ├── 01_hybrid_retrieval.py
│   ├── 02_reranking.py
│   ├── 03_query_expansion.py
│   ├── 04_contextual_compression.py
│   └── 05_parent_document_retrieval.py
└── apps/
    ├── document_qa/
    └── code_assistant/
```

## RAG Pipeline

```
Documents → Chunk → Embed → Index → Retrieve → Generate
```

### Chunking Strategies
- Fixed size
- Recursive
- Semantic
- Agentic

### Retrieval Techniques
| Technique | Description |
|-----------|-------------|
| Hybrid | Keyword + semantic |
| Reranking | Cross-encoder scoring |
| Query Expansion | HyDE, multi-query |
| Parent Doc | Retrieve chunks, return full docs |

## Running Examples

```bash
# Basic RAG
python 16_rag_systems/fundamentals/01_basic_rag_pipeline.py

# Chunking comparison
python 16_rag_systems/fundamentals/02_chunking_strategies.py

# Hybrid retrieval
python 16_rag_systems/advanced/01_hybrid_retrieval.py
```

## Cross-References

- **Prerequisite**: [09_search_with_vectors/](../09_search_with_vectors/)
- **Builds On**: [12_function_calling/](../12_function_calling/)
- **Next**: [17_huggingface_ecosystem/](../17_huggingface_ecosystem/)

## Resources

- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
- [RAG Survey Paper](https://arxiv.org/abs/2312.10997)
