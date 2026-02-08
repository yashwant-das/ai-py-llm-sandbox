# 02. LLM Fundamentals

Understand the building blocks of Large Language Models (LLMs) before building complex applications.

## Key Concepts

1.  **Tokens**: How LLMs "read" text. It's not character-by-character or word-by-word.
2.  **Temperature**: Controlling randomness and creativity.
3.  **Context Window**: The memory limit of the model.
4.  **Streaming**: Receiving text chunk-by-chunk for better UX.

## Experiments

Run these scripts to see the concepts in action:

*   **Token Counting**:
    ```bash
    uv run python 02_fundamentals/experiments/01_token_counting.py
    ```
*   **Temperature Sampling**:
    ```bash
    uv run python 02_fundamentals/experiments/02_temperature_sampling.py
    ```
*   **Context Window**:
    ```bash
    uv run python 02_fundamentals/experiments/03_context_window.py
    ```
*   **Streaming**:
    ```bash
    uv run python 02_fundamentals/experiments/04_streaming_responses.py
    ```
*   **Model Comparison**:
    ```bash
    uv run python 02_fundamentals/experiments/05_model_comparison.py
    ```
