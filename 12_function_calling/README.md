# Topic 12: Function Calling and Tool Integration

> Extend LLM capabilities with external tools: APIs, databases, calculations.

## Learning Objectives

By the end of this topic, you will:
- Implement native function calling (OpenAI-style)
- Parse tool calls from text (for local models)
- Orchestrate multiple tools
- Handle tool errors gracefully

## Folder Structure

```
12_function_calling/
├── README.md
├── fundamentals/
│   ├── 01_native_function_calling.py
│   ├── 02_manual_tool_parsing.py
│   └── 03_multi_tool_orchestration.py
├── implementations/
│   ├── calculator_tool.py
│   ├── weather_tool.py
│   └── file_system_tools.py
└── framework/
    └── langchain_tools_integration.py
```

## Tool Design Principles

1. **Clear Names**: Descriptive function names
2. **Explicit Schemas**: Type hints and docstrings
3. **Error Handling**: Graceful failures
4. **Idempotency**: Same input → same output

## Running Examples

```bash
# Native function calling
python 12_function_calling/fundamentals/01_native_function_calling.py

# Manual parsing (for models without native support)
python 12_function_calling/fundamentals/02_manual_tool_parsing.py

# Multi-tool orchestration
python 12_function_calling/fundamentals/03_multi_tool_orchestration.py
```

## Cross-References

- **Builds On**: [06_advanced_prompting/](../06_advanced_prompting/) - Structured output
- **Next**: [18_ai_agents/](../18_ai_agents/) - Agents use tools
- **Related**: [16_rag_systems/](../16_rag_systems/) - Retrieval as tool
