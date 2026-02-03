# Topic 18: AI Agents and Agent Frameworks

> Build autonomous systems that reason, plan, and take actions using tools.

## Learning Objectives

By the end of this topic, you will:
- Understand the ReAct (Reasoning + Acting) pattern
- Implement agents from scratch and with frameworks
- Design multi-step planning and execution workflows
- Compare agent frameworks (LangGraph, AutoGen, CrewAI)

## Files

### Fundamentals (Raw Implementation)
| File | Pattern | Description |
|------|---------|-------------|
| `fundamentals/01_react_pattern.py` | **ReAct** | LangChain ReAct agent with tools |
| `fundamentals/02_react_from_scratch.py` | **ReAct (Raw)** | Manual implementation without frameworks |
| `fundamentals/03_plan_and_execute.py` | **Plan & Execute** | Decomposition-based agents |
| `fundamentals/04_multi_agent_patterns.md` | **Multi-Agent** | Collaboration patterns |

### Framework Implementations
| File | Framework | Description |
|------|-----------|-------------|
| `frameworks/langgraph_agents.py` | LangGraph | State machine agents with persistence |

### Example Applications
| Application | Description |
|-------------|-------------|
| `apps/research_assistant/` | Web search + synthesis agent |
| `apps/coding_agent/` | File operations + code generation |
| `apps/personal_assistant/` | Multi-tool coordinator |

## Key Concepts

### ReAct Pattern
The foundation of most LLM agents. The model iteratively:

1. **Thought**: Reason about what to do next
2. **Action**: Use a tool or execute a step
3. **Observation**: Get results
4. **Repeat** until task complete

```
Question: What is the weather in Paris?
Thought: I need to get current weather information for Paris.
Action: weather_tool(location="Paris")
Observation: {"temperature": 18, "condition": "sunny"}
Thought: I have the weather data. I can now answer.
Final Answer: It's 18°C and sunny in Paris.
```

### Tool Design Principles
- **Clear names**: Descriptive function names
- **Explicit schemas**: Type hints and docstrings
- **Error handling**: Graceful failures
- **Idempotency**: Same input → same output (where possible)

### Planning vs. Reacting
| Pattern | Use When | Trade-off |
|---------|----------|-----------|
| ReAct | Dynamic environments, unknown steps | More LLM calls |
| Plan & Execute | Known task types, optimization | Less adaptive |

## Running the Examples

```bash
# ReAct agent with LangChain
python 18_ai_agents/fundamentals/01_react_pattern.py

# Manual ReAct implementation (no frameworks)
python 18_ai_agents/fundamentals/02_react_from_scratch.py

# Plan and execute decomposition
python 18_ai_agents/fundamentals/03_plan_and_execute.py

# LangGraph state machines
python 18_ai_agents/frameworks/langgraph_agents.py
```

## Cross-References

- **Builds On**: 
  - [05_prompt_engineering_fundamentals/](../05_prompt_engineering_fundamentals/) - Role prompting
  - [06_advanced_prompting/](../06_advanced_prompting/) - Chain-of-thought reasoning
  - [12_function_calling/](../12_function_calling/) - Tool definitions
- **Enables**:
  - [16_rag_systems/](../16_rag_systems/) - Retrieval as a tool
  - [07_text_generation_apps/](../07_text_generation_apps/) - Autonomous content generation

## Resources

- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [LangChain Agents Documentation](https://python.langchain.com/docs/modules/agents/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
