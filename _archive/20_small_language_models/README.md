# Topic 20: Building with Small Language Models (SLMs)

> Efficient models for edge and resource-constrained environments.

## Learning Objectives

By the end of this topic, you will:
- Work with sub-10B parameter models
- Optimize via quantization
- Deploy on edge devices
- Understand quality/cost trade-offs

## Folder Structure

```
20_small_language_models/
├── README.md
├── models/
│   ├── phi_3_examples.py          # Microsoft's Phi-3
│   ├── gemma_examples.py          # Google's Gemma
│   ├── qwen_examples.py           # Alibaba's Qwen
│   └── llama_3_1b_8b.py           # Meta's smaller models
├── optimizations/
│   ├── quantization_comparison.py
│   ├── onnx_export.py
│   └── edge_deployment.md
└── apps/
    ├── on_device_chat.py
    └── embedded_assistant.py
```

## SLM Landscape

| Model | Size | Strengths |
|-------|------|-----------|
| Phi-3 Mini | 3.8B | Quality, reasoning |
| Gemma 2B | 2B | Lightweight, fast |
| Qwen2.5 | 0.5-7B | Multilingual |
| Llama 3.2 | 1-3B | Mobile-optimized |

## Optimization Techniques

- **Quantization**: 4-bit, 8-bit weights
- **ONNX Export**: Runtime optimization
- **Speculative Decoding**: Faster inference
- **Caching**: Reuse computations

## Running Examples

```bash
# Phi-3 examples
python 20_small_language_models/models/phi_3_examples.py

# Quantization comparison
python 20_small_language_models/optimizations/quantization_comparison.py
```

## Cross-References

- **Previous**: [19_fine_tuning/](../19_fine_tuning/)
- **Next**: [21_mistral_meta_families/](../21_mistral_meta_families/)
