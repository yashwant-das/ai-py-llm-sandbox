# 06. Tools & Agents

Moving beyond text generation to taking action.

## Concepts

1.  **Function Calling** (Tool Use): The LLM generates structured arguments to call a function (e.g., `get_weather(city="London")`). It *does not* run the code itself; it just tells you what to run.
2.  **Agents**: Systems that use an LLM as a reasoning engine to decide which tools to call and in what order to solve a problem.

## Patterns

*   **ReAct**: **Re**asoning + **Act**ing. The agent loops: Thought -> Action -> Observation -> Thought...
*   **Tool Use**: Defining schemas and handling model outputs.

## Examples

```bash
# ReAct Agent (with Search and Calc tools)
uv run python 06_tools_agents/agents/fundamentals/01_react_pattern.py
```
