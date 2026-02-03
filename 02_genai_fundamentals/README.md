# Topic 2: Introduction to Generative AI and LLMs

> Understand how Large Language Models work: tokens, embeddings, context windows, and sampling.

## Learning Objectives

By the end of this topic, you will:
- Understand transformer architecture basics (high-level)
- Work with tokenization and context windows
- Experiment with temperature and sampling parameters
- Estimate costs and compute requirements

## Folder Structure

```
02_genai_fundamentals/
├── README.md
├── notes/
│   ├── what_are_llms.md
│   ├── transformer_basics.md
│   ├── tokens_and_embeddings.md
│   └── inference_vs_training.md
└── experiments/
    ├── token_counting.py          # Count tokens in prompts
    ├── explore_temperature.py     # Visualize temperature effects
    └── top_p_sampling_demo.py     # Nucleus sampling exploration
```

## Key Concepts

### What are LLMs?
- Neural networks trained to predict the next token
- Built on transformer architecture (attention mechanisms)
- Trained on vast text corpora (internet, books, code)
- Emergent capabilities at scale

### Tokens vs Words
| Concept | Description |
|---------|-------------|
| Token | Unit of text (subword) processed by model |
| ~0.75 tokens/word | English average |
| Context window | Max tokens model can process |
| Pricing | Usually per 1K tokens |

### Sampling Parameters
| Parameter | Effect | Typical Range |
|-----------|--------|---------------|
| Temperature | Randomness (0=deterministic, 1=creative) | 0.0 - 1.0 |
| Top-p | Nucleus sampling threshold | 0.1 - 1.0 |
| Top-k | Limit to k most likely tokens | 1 - 100 |
| Max tokens | Output length limit | 100 - 4000 |

## Running Experiments

```bash
# Count tokens in different texts
python 02_genai_fundamentals/experiments/token_counting.py

# See temperature effects
python 02_genai_fundamentals/experiments/explore_temperature.py
```

## Cross-References

- **Next**: [03_llm_landscape/](../03_llm_landscape/) - Compare different models
- **Applies To**: All prompt engineering topics (token awareness)

## Resources

- [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [Let's Build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) - Karpathy
