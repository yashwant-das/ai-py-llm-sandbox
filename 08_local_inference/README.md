# 08. Local Inference

Running LLMs on your own hardware using open-source tools.

## Why Local?

*   **Privacy**: Data never leaves your machine.
*   **Cost**: No API fees.
*   **Offline**: Works without internet.
*   **Control**: Full customization of system prompts and parameters.

## Tools

1.  **Ollama**: The easiest way to run models (macOS/Linux/Windows).
2.  **Hugging Face Transformers**: Python library for model downloads and inference.
3.  **Llama.cpp**: Low-level C++ inference engine (backend for Ollama).

## Setup

This module requires Hugging Face libraries:

```bash
uv sync --extra huggingface
```

## Comparisons

See `code/` for examples benchmarking local vs. cloud inference (if applicable).
