# 04. Prompt Engineering

Master the art of communicating with LLMs, from basic instructions to complex reasoning chains.

## Structure

*   **`code/`**: Basic prompting techniques (Zero-shot, Few-shot).
*   **`advanced/code/`**: Advanced techniques (Chain-of-Thought, Tree-of-Thoughts, React).
*   **`notes/`**: Theoretical concepts and patterns.

## Key Techniques

1.  **Zero-Shot**: Direct instruction without examples.
2.  **Few-Shot**: Providing examples to guide style and format.
3.  **Chain-of-Thought (CoT)**: Asking the model to "think step-by-step".
4.  **Structured Output**: Forcing JSON or specific formats (critical for systems).
5.  **Self-Consistency**: Sampling multiple reasoning paths and voting.

## Examples

Run these to see the difference in output quality:

```bash
# Basic
uv run python 04_prompting/code/01_zero_shot.py
uv run python 04_prompting/code/02_few_shot.py

# Advanced
uv run python 04_prompting/advanced/code/01_chain_of_thought.py
uv run python 04_prompting/advanced/code/04_structured_output.py
```
