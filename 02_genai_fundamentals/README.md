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
    ├── 01_token_counting.py           # Count tokens (tiktoken)
    ├── 02_temperature_sampling.py     # Temperature effects
    ├── 03_context_window.py           # Context limits
    ├── 04_streaming_responses.py      # Streaming demo
    └── 05_model_comparison.py         # Compare endpoints
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

All experiments use the **raw OpenAI SDK** (no LangChain, no shared modules) for maximum transparency.

### Configure Your Endpoint

Before running, edit the experiment files to set your endpoint (top of each file):

```python
# Option 1: LM Studio (default)
BASE_URL = "http://127.0.0.1:1234/v1"
API_KEY = "lm-studio"
MODEL = "openai/gpt-oss-20b"

# Option 2: Ollama (uncomment if using)
# BASE_URL = "http://localhost:11434/v1"
# API_KEY = "ollama"
# MODEL = "llama3.1"

# Option 3: OpenAI (uncomment if using)
# BASE_URL = "https://api.openai.com/v1"
# API_KEY = "sk-your-key-here"
# MODEL = "gpt-4o-mini"
```

### Run the Experiments

```bash
# 1. Token counting (no LLM needed - uses tiktoken)
python 02_genai_fundamentals/experiments/01_token_counting.py

# 2. Temperature and sampling
python 02_genai_fundamentals/experiments/02_temperature_sampling.py

# 3. Context window limits
python 02_genai_fundamentals/experiments/03_context_window.py

# 4. Streaming responses
python 02_genai_fundamentals/experiments/04_streaming_responses.py

# 5. Compare multiple endpoints
python 02_genai_fundamentals/experiments/05_model_comparison.py
```

### What Each Experiment Teaches

| Experiment | Concept | Key Takeaway |
|------------|---------|--------------|
| `01_token_counting.py` | Tokenization | Tokens ≠ words; affects pricing and limits |
| `02_temperature_sampling.py` | Sampling | Temperature controls randomness |
| `03_context_window.py` | Context limits | Input + output must fit in window |
| `04_streaming_responses.py` | Streaming | Better UX with token-by-token display |
| `05_model_comparison.py` | Evaluation | Compare speed, quality, cost across models |

## Cross-References

- **Next**: [03_llm_landscape/](../03_llm_landscape/) - Compare different models
- **Applies To**: All prompt engineering topics (token awareness)

## Resources

- [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [Let's Build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) - Karpathy
