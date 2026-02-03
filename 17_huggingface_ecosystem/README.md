# Topic 17: Open-Source Models and Hugging Face Ecosystem

> Work with open models: Transformers, tokenizers, quantization, local inference.

## Learning Objectives

By the end of this topic, you will:
- Use Hugging Face Transformers library
- Load and run models locally
- Understand quantization (GGUF, AWQ, GPTQ)
- Integrate with Ollama and llama.cpp

## Folder Structure

```
17_huggingface_ecosystem/
├── README.md
├── setup/
│   ├── transformers_basics.md
│   └── local_inference_options.md
├── code/
│   ├── 01_pipeline_api.py
│   ├── 02_model_loading.py
│   ├── 03_tokenizers.py
│   └── 04_quantization_basics.py
├── integrations/
│   ├── ollama_integration.py
│   └── llama_cpp_integration.py
└── experiments/
    └── model_comparison_hf.py
```

## Key Components

### Transformers Library
- `pipeline()`: Simple inference
- `AutoModel`: Direct model access
- `AutoTokenizer`: Text preprocessing

### Quantization
| Format | Use Case |
|--------|----------|
| GGUF | llama.cpp, Ollama |
| AWQ | 4-bit inference |
| GPTQ | GPU optimization |
| BitsAndBytes | Easy loading |

### Local Inference Options
- Transformers (Hugging Face)
- llama.cpp (C++ backend)
- Ollama (easy setup)
- vLLM (high throughput)

## Running Examples

```bash
# Pipeline API
python 17_huggingface_ecosystem/code/01_pipeline_api.py

# Quantized loading
python 17_huggingface_ecosystem/code/04_quantization_basics.py
```

## Cross-References

- **Previous**: [16_rag_systems/](../16_rag_systems/)
- **Next**: [18_ai_agents/](../18_ai_agents/)
- **Related**: [20_small_language_models/](../20_small_language_models/)

## Resources

- [Hugging Face Documentation](https://huggingface.co/docs/transformers/)
- [Quantization Guide](https://huggingface.co/docs/transformers/quantization)
