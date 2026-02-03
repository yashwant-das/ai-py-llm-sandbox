# Prompt Engineering Playground

This repository contains hands-on examples of various prompt engineering techniques using LangChain and local LLMs via LM Studio.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start LM Studio:**
   - Load your model (e.g., `openai/gpt-oss-20b`)
   - Start the local server on port 1234

3. **Configure API keys (optional for some examples):**
   - Copy `.env.example` to `.env`
   - Add your `SERPAPI_API_KEY` if using Google search features

## Techniques Covered

| File | Technique | Description |
|------|-----------|-------------|
| `01_zero_shot.py` | **Zero-Shot Prompting** | Direct instructions without examples |
| `02_few_shot.py` | **Few-Shot Prompting** | Learning from examples in the prompt |
| `03_chain_of_thought.py` | **Chain-of-Thought (CoT)** | Step-by-step reasoning |
| `04_react_agent.py` | **ReAct Pattern** | Reasoning + Action with tools |
| `05_role_prompting.py` | **Role/Persona Prompting** | Assigning specific roles |
| `06_structured_output.py` | **Structured Output** | JSON/XML formatted responses |
| `07_self_consistency.py` | **Self-Consistency** | Multiple samples and voting |
| `08_prompt_chaining.py` | **Prompt Chaining** | Breaking tasks into steps |
| `09_advanced_techniques.py` | **Advanced Techniques** | ToT, APE, System 2 thinking |

## Quick Start

Run any example:
```bash
python src/01_zero_shot.py
```

## Key Concepts

### Zero-Shot vs Few-Shot
- **Zero-shot**: Give the model a task directly
- **Few-shot**: Show examples of input/output pairs first

### Chain-of-Thought
Add "Let's think step by step" to trigger reasoning before answering.

### ReAct Pattern
The model iteratively:
1. **Thought**: Reason about what to do
2. **Action**: Use a tool or execute
3. **Observation**: Get results
4. **Repeat** until done

### Role Prompting
Start with "You are a [role]..." to shape expertise and tone.

## Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LangChain Documentation](https://python.langchain.com/)
- [LM Studio](https://lmstudio.ai/)
