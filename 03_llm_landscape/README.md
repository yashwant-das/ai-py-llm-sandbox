# Topic 3: Exploring and Comparing LLMs

> Benchmark and compare different LLM families, sizes, and providers.

## Learning Objectives

By the end of this topic, you will:
- Compare open vs closed-source models
- Understand model size vs capability trade-offs
- Run standardized benchmarks across models
- Make informed model selection decisions

## Folder Structure

```
03_llm_landscape/
├── README.md
├── model_registry.yaml            # Catalog of models to try
├── comparison_framework/
│   ├── benchmark_runner.py        # Run prompts across models
│   ├── latency_benchmark.py       # Measure response times
│   └── quality_evaluator.py       # Side-by-side comparison
└── experiments/
    ├── compare_creative_writing.py
    ├── compare_reasoning.py
    └── compare_code_generation.py
```

## Model Categories

### Open Source (Local)
| Family | Sizes | Strengths |
|--------|-------|-----------|
| Llama 3.1 | 8B, 70B, 405B | General purpose, well-rounded |
| Mistral | 7B, Mixtral 8x7B | Efficient, MoE architecture |
| Qwen 2.5 | 0.5B - 72B | Multilingual, coding |
| Phi-3 | 3.8B - 14B | Small but capable |

### Commercial APIs
| Provider | Models | Notes |
|----------|--------|-------|
| OpenAI | GPT-4o, GPT-4o-mini | Industry standard |
| Anthropic | Claude 3.5 Sonnet | Long context, reasoning |
| Google | Gemini 1.5 Pro | Multimodal, 2M context |
| Groq | Llama 3.1, Mixtral | Fast inference |

## Running Comparisons

```bash
# Run benchmark suite
python 03_llm_landscape/comparison_framework/benchmark_runner.py

# Measure latency
python 03_llm_landscape/comparison_framework/latency_benchmark.py
```

## Cross-References

- **Previous**: [02_genai_fundamentals/](../02_genai_fundamentals/)
- **Next**: [04_ethics_and_safety/](../04_ethics_and_safety/)
- **Applies To**: All topics (model selection)

## Resources

- [LMSYS Chatbot Arena](https://chat.lmsys.org/)
- [Artificial Analysis](https://artificialanalysis.ai/)
