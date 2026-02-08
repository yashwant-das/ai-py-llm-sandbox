# Topic 18: AI Agents and Agent Frameworks

> Build autonomous systems that reason, plan, and take actions using tools.

## Learning Objectives

By the end of this topic, you will:

- Understand the ReAct (Reasoning + Acting) pattern
- Implement agents from scratch using raw Tool Calling
- Design multi-step planning and execution workflows

## Files

### Fundamentals (Raw Implementation)

| File                               | Pattern          | Description                        |
| ---------------------------------- | ---------------- | ---------------------------------- |
| `fundamentals/01_react_pattern.py` | **Modern ReAct** | OpenAI Tool Calling Loop (Raw SDK) |

## Key Concepts

### ReAct Pattern

The foundation of most LLM agents. The model iteratively:

1. **Thought**: Reason about what to do next
2. **Action**: Use a tool or execute a step
3. **Observation**: Get results
4. **Repeat** until task complete

### Tool Design Principles

- **Clear names**: Descriptive function names
- **Explicit schemas**: Type hints and docstrings
- **Error handling**: Graceful failures

## Running the Examples

All examples use the shared NVIDIA client configuration.

```bash
# Modern ReAct Agent (Raw OpenAI SDK + Tool Calling)
python 18_ai_agents/fundamentals/01_react_pattern.py
```

## Cross-References

- **Builds On**:
  - [06_advanced_prompting/](../06_advanced_prompting/) - Chain-of-thought reasoning
  - [12_function_calling/](../12_function_calling/) - Tool definitions

## Resources

- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [OpenAI Tool Calling](https://platform.openai.com/docs/guides/function-calling)
