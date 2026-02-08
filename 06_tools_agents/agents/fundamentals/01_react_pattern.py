"""
ReAct (Reasoning + Acting) Pattern
===================================
Combines reasoning with actions (tool usage).
The model iteratively: THINK -> ACT -> OBSERVE -> REPEAT until solved.

Refactored to use the raw OpenAI SDK with native Tool Calling (Function Calling).

Topic: 18_ai_agents
"""

import sys
from pathlib import Path
import json

# Add project root to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from duckduckgo_search import DDGS
from shared import get_nvidia_client, get_settings

# Initialize client
client = get_nvidia_client()
settings = get_settings()

print("=" * 80)
print("ReAct AGENT (Raw SDK + Tool Calling)")
print("=" * 80)
print(f"Model: {settings.default_model}")

# --- Tool Definitions ---


def search_duckduckgo(query: str) -> str:
    """Search the web via DuckDuckGo and return results."""
    print(f"\n[Tool: Searching for '{query}']")
    with DDGS() as ddg:
        results = ddg.text(query, max_results=3)
    if results:
        return results[0].get("body") or results[0].get("title", "No snippet")
    return "No results found."


def calculate(expression: str) -> str:
    """Evaluate a mathematical expression safely."""
    print(f"\n[Tool: Calculating '{expression}']")
    try:
        # Only allow basic math operations
        allowed_chars = set("0123456789+-*/.() ")
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return str(result)
        return "Error: Invalid characters in expression"
    except Exception as e:
        return f"Error: {str(e)}"


def get_current_date() -> str:
    """Get today's date."""
    print("\n[Tool: Getting Date]")
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d")


# Map function names to functions
available_tools = {
    "search_duckduckgo": search_duckduckgo,
    "calculate": calculate,
    "get_current_date": get_current_date,
}

# Define tools schema for the API
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "search_duckduckgo",
            "description": "Search the web via DuckDuckGo and return results.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"}
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The math expression (e.g., '2 + 2')",
                    }
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_date",
            "description": "Get today's date.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
]

# --- Agent Loop ---


def run_agent(query):
    print(f"\n--- Query: {query} ---")
    messages = [{"role": "user", "content": query}]

    # Loop for multi-step reasoning
    for _ in range(5):  # Limit turns
        try:
            response = client.chat.completions.create(
                model=settings.default_model,
                messages=messages,
                tools=tools_schema,
                tool_choice="auto",
                temperature=0.0,
            )

            message = response.choices[0].message

            # Append assistant message to history
            messages.append(message)

            # Check if tool calls required
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)

                    if function_name in available_tools:
                        function_to_call = available_tools[function_name]
                        tool_output = function_to_call(**function_args)

                        # Add tool execution result to message history
                        messages.append(
                            {
                                "tool_call_id": tool_call.id,
                                "role": "tool",
                                "name": function_name,
                                "content": str(tool_output),
                            }
                        )
            else:
                # No tool calls, just final response
                print(f"\nFinal Answer: {message.content}")
                return message.content

        except Exception as e:
            print(f"Error: {e}")
            break


# Example 1: Search + Calculation
run_agent("Who is the oldest living person and what year were they born?")

# Example 2: Date-dependent query
run_agent("How many days are left until the end of this year?")

# Example 3: Multi-hop
run_agent("What is the capital city of the country where the Eiffel Tower is located?")

print("\n" + "=" * 80)
print("Key Takeaway: Agents loop through THINK -> ACT -> OBSERVE.")
print("With raw SDK, we use `tools` and `tool_calls` to handle this loop.")
print("=" * 80)
