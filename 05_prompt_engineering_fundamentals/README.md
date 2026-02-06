# Topic 5: Prompt Engineering Fundamentals

> Master the basics of effective prompting: zero-shot, few-shot, and role-based techniques.

## Learning Objectives

By the end of this topic, you will:

- Understand the anatomy of an effective prompt
- Apply zero-shot and few-shot prompting patterns
- Use role/persona prompting to shape LLM behavior
- Manage context windows and token limits

## Files

| File                        | Technique                  | Description                          |
| --------------------------- | -------------------------- | ------------------------------------ |
| `code/01_zero_shot.py`      | **Zero-Shot Prompting**    | Direct instructions without examples |
| `code/02_few_shot.py`       | **Few-Shot Prompting**     | Learning from examples in the prompt |
| `code/03_role_prompting.py` | **Role/Persona Prompting** | Assigning specific expertise roles   |

## Key Concepts

### Zero-Shot vs Few-Shot

- **Zero-shot**: Give the model a task directly, relying on pre-trained knowledge
- **Few-shot**: Provide examples of input/output pairs to guide the pattern

### Role Prompting

Start prompts with "You are a [role]..." to shape:

- Expertise level
- Tone and style
- Perspective and constraints

### Prompt Structure Template

```
[Role/Persona]
[Context/Background]
[Task/Instruction]
[Examples - if few-shot]
[Output Format]
[Constraints]
```

## Running the Examples

All examples use the shared NVIDIA client configuration.

### Quick Start

```bash
# Zero-shot prompting
python 05_prompt_engineering_fundamentals/code/01_zero_shot.py

# Few-shot prompting
python 05_prompt_engineering_fundamentals/code/02_few_shot.py

# Role prompting
python 05_prompt_engineering_fundamentals/code/03_role_prompting.py
```

## Cross-References

- **Next Topic**: [06_advanced_prompting/](../06_advanced_prompting/) - Chain-of-thought, self-consistency, structured outputs
- **Related**: [18_ai_agents/](../18_ai_agents/) - ReAct agents use prompt engineering patterns

## Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
