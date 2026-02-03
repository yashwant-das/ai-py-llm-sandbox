# Topic 21: Building with Mistral and Meta Model Families

> Deep dive into two major open model ecosystems.

## Learning Objectives

By the end of this topic, you will:
- Use Mistral models (7B, Mixtral, Codestral)
- Deploy Llama 3.1 models (8B to 405B)
- Implement Llama Guard for safety
- Compare performance across families

## Folder Structure

```
21_mistral_meta_families/
├── README.md
├── mistral/
│   ├── mistral_7b_examples.py
│   ├── mixtral_moe_explained.py
│   ├── mistral_large_api.py
│   └── codestral_examples.py
├── meta_llama/
│   ├── llama_3_1_explained.md
│   ├── llama_3_1_8b_local.py
│   ├── llama_3_1_70b_groq.py
│   └── llama_guard_safety.py
└── comparisons/
    └── llama_vs_mistral_benchmark.py
```

## Mistral Models

| Model | Type | Notes |
|-------|------|-------|
| Mistral 7B | Dense | Efficient, good quality |
| Mixtral 8x7B | MoE | Sparse, 47B active 13B |
| Codestral | Code | 22B, code-specialized |
| Mistral Large | API | Commercial, high quality |

## Meta Llama 3.1

| Size | Use Case |
|------|----------|
| 8B | Local, edge |
| 70B | Server, complex tasks |
| 405B | Research, maximum quality |

### Llama Guard
- Safety classifier
- Input/output moderation
- Customizable categories

## Running Examples

```bash
# Mistral 7B
python 21_mistral_meta_families/mistral/mistral_7b_examples.py

# Llama 3.1 local
python 21_mistral_meta_families/meta_llama/llama_3_1_8b_local.py

# Llama Guard
python 21_mistral_meta_families/meta_llama/llama_guard_safety.py
```

## Cross-References

- **Previous**: [20_small_language_models/](../20_small_language_models/)
- **Applies To**: All application topics

## Resources

- [Mistral Documentation](https://docs.mistral.ai/)
- [Meta Llama](https://llama.meta.com/)
