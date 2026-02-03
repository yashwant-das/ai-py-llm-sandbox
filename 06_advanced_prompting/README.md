# Topic 6: Advanced Prompt Engineering Techniques

> Advanced patterns for complex reasoning, reliable outputs, and prompt optimization.

## Learning Objectives

By the end of this topic, you will:
- Implement Chain-of-Thought (CoT) reasoning
- Use self-consistency for improved accuracy
- Build prompt chains for complex tasks
- Generate and validate structured outputs (JSON/XML)
- Explore Tree of Thoughts, APE, and System-2 thinking

## Files

| File | Technique | Description |
|------|-----------|-------------|
| `code/01_chain_of_thought.py` | **Chain-of-Thought (CoT)** | Step-by-step reasoning |
| `code/02_self_consistency.py` | **Self-Consistency** | Multiple samples and voting |
| `code/03_prompt_chaining.py` | **Prompt Chaining** | Breaking tasks into steps |
| `code/04_structured_output.py` | **Structured Output** | JSON/XML formatted responses |
| `code/05_tree_of_thoughts.py` | **Tree of Thoughts (ToT)** | Explore multiple reasoning paths |
| `code/06_auto_prompt_engineering.py` | **APE** | Automatic prompt optimization |
| `code/07_system2_activations.py` | **System 2 Thinking** | Reflection, critique, verification |

## Key Concepts

### Chain-of-Thought (CoT)
Add "Let's think step by step" or demonstrate reasoning in examples to trigger step-by-step thinking before answering.

**When to use:** Math problems, logic puzzles, multi-step reasoning

### Self-Consistency
Generate multiple answers to the same prompt, then vote or select the most common answer.

**When to use:** Factual accuracy is critical; reasoning tasks with clear correct answers

### Prompt Chaining
Break complex tasks into sequential prompts where output of one becomes input to the next.

**When to use:** Long-form content generation, multi-stage processing

### Structured Output
Constrain LLM output to parseable formats (JSON, XML) using schema descriptions and examples.

**When to use:** API responses, database insertion, downstream automation

### Tree of Thoughts (ToT)
Generate multiple solution paths, evaluate each, and select or combine the best.

**When to use:** Open-ended problems, creative tasks, optimization problems

## Running the Examples

All examples support multiple LLM providers via the `LLM_PROVIDER` environment variable (defaults to `lmstudio`).

```bash
# Chain-of-Thought reasoning (uses LM Studio by default)
python 06_advanced_prompting/code/01_chain_of_thought.py

# Use Ollama instead
LLM_PROVIDER=ollama python 06_advanced_prompting/code/01_chain_of_thought.py

# Self-consistency with voting
python 06_advanced_prompting/code/02_self_consistency.py

# Multi-step prompt chains
python 06_advanced_prompting/code/03_prompt_chaining.py

# JSON/XML output formatting
python 06_advanced_prompting/code/04_structured_output.py

# Tree of Thoughts exploration
python 06_advanced_prompting/code/05_tree_of_thoughts.py

# Automatic prompt engineering
python 06_advanced_prompting/code/06_auto_prompt_engineering.py

# System-2 reflective reasoning
python 06_advanced_prompting/code/07_system2_activations.py
```

### Provider Options
Set `LLM_PROVIDER` environment variable or add to `.env`:
- `lmstudio` (default) - LM Studio on port 1234
- `ollama` - Ollama on port 11434
- `openai` - OpenAI API (requires key)
- `auto` - Tries LM Studio → Ollama → OpenAI

## Cross-References

- **Prerequisite**: [05_prompt_engineering_fundamentals/](../05_prompt_engineering_fundamentals/)
- **Applies To**: 
  - [12_function_calling/](../12_function_calling/) - Structured outputs enable tool use
  - [16_rag_systems/](../16_rag_systems/) - Prompt chaining for query transformation
  - [18_ai_agents/](../18_ai_agents/) - ReAct combines CoT with tool use

## Resources

- [Chain-of-Thought Paper](https://arxiv.org/abs/2201.11903)
- [Tree of Thoughts Paper](https://arxiv.org/abs/2305.10601)
- [Self-Consistency Paper](https://arxiv.org/abs/2203.11171)
