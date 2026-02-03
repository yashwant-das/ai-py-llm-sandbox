"""
ReAct (Reasoning + Acting) Pattern
===================================
Combines Chain-of-Thought reasoning with actions (like tool usage).
The model iteratively: THINK -> ACT -> OBSERVE -> REPEAT until solved.

When to use:
- Tasks requiring external information (search, APIs, databases)
- Multi-step problems that need verification
- Interactive tasks requiring tool use

Key Components:
1. Thought: Reason about what to do next
2. Action: Execute a tool/action
3. Observation: Get results from the action
4. Repeat until done

This is the foundation of many agent frameworks like LangChain agents.
"""

import os

from ddgs import DDGS
from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain import hub

# Load environment variables
load_dotenv()

# Initialize LLM (LM Studio)
llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    temperature=0.1,
    openai_api_key="lm-studio",
    openai_api_base="http://127.0.0.1:1234/v1",
)


# Define tools
@tool
def search_duckduckgo(query: str) -> str:
    """Search the web via DuckDuckGo and return results."""
    with DDGS() as ddg:
        results = ddg.text(query, max_results=3)
    if results:
        return results[0].get("body") or results[0].get("title", "No snippet")
    return "No results found."


@tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression safely."""
    try:
        # Only allow basic math operations
        allowed_chars = set("0123456789+-*/.() ")
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return str(result)
        return "Error: Invalid characters in expression"
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def get_current_date() -> str:
    """Get today's date."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")


# Create tools list
tools = [search_duckduckgo, calculate, get_current_date]

# Get the ReAct prompt template from LangChain hub
# This includes the standard ReAct instructions
prompt = hub.pull("hwchase17/react")

# Create the agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

print("=" * 80)
print("ReAct AGENT EXAMPLES")
print("=" * 80)

# Example 1: Search + Calculation
print("\n--- Example 1: Multi-step Research Task ---")
query1 = "What is the current age of the oldest living person? Calculate how many years older they are than a 30-year-old."
print(f"Query: {query1}")
print("-" * 80)
result1 = agent_executor.invoke({"input": query1})
print(f"\nFinal Answer: {result1['output']}")

# Example 2: Date-dependent query
print("\n--- Example 2: Date-Aware Query ---")
query2 = "How many days are left until the end of this year?"
print(f"Query: {query2}")
print("-" * 80)
result2 = agent_executor.invoke({"input": query2})
print(f"\nFinal Answer: {result2['output']}")

# Example 3: Multi-hop question (requires multiple searches)
print("\n--- Example 3: Multi-hop Question ---")
query3 = "What is the capital city of the country where the Eiffel Tower is located?"
print(f"Query: {query3}")
print("-" * 80)
result3 = agent_executor.invoke({"input": query3})
print(f"\nFinal Answer: {result3['output']}")

print("\n" + "=" * 80)
print("Key Takeaway: ReAct agents combine reasoning with actions.")
print("They can use tools, observe results, and adapt their next steps.")
print("This is the foundation of autonomous AI agents.")
print("=" * 80)
