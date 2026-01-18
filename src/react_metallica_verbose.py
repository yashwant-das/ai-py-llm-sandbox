import os

from ddgs import DDGS
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.globals import set_verbose
from langchain_openai import ChatOpenAI
from serpapi import GoogleSearch

# Load environment variables from .env file
load_dotenv()

# Enable verbose output to see ReAct reasoning steps
set_verbose(True)

# Display configuration
MAX_CONTENT_LENGTH = 800
MAX_OBSERVATION_LENGTH = 600


@tool
def search_duckduckgo(query: str) -> str:
    """Search the web via DuckDuckGo and return results."""
    with DDGS() as ddg:
        results = ddg.text(query, max_results=3)
    if results:
        return results[0].get("body") or results[0].get("title", "No snippet")
    return "No results found."


@tool
def search_google(query: str) -> str:
    """Search Google via SerpAPI and return results."""
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "Error: SERPAPI_API_KEY environment variable not set."

    params = {"q": query, "api_key": api_key, "num": 3}

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        # Extract first organic result
        if "organic_results" in results and results["organic_results"]:
            first_result = results["organic_results"][0]
            snippet = first_result.get("snippet") or first_result.get(
                "title", "No snippet"
            )
            return snippet
        return "No results found."
    except Exception as e:
        return f"Error searching: {str(e)}"


# Initialize LLM (LM Studio)
llm = ChatOpenAI(
    model="google/gemma-3-4b",
    temperature=0.1,
    openai_api_key="lm-studio",
    openai_api_base="http://127.0.0.1:1234/v1",
)

# Create agent with both tools - agent will reason about which to use
tools = [search_duckduckgo, search_google]
agent = create_agent(llm, tools)

# More complex query that requires multiple reasoning steps
# This better demonstrates the ReAct pattern: Think -> Act -> Observe -> Think -> Act...
prompt = (
    "First, find out who the current members of Metallica are. "
    "Then, for each member, search for how many children they have. "
    "Finally, calculate and tell me the total number of children across all band members."
)

print("=" * 80)
print("ReAct Agent Execution - Reasoning Steps Will Be Visible Below")
print("=" * 80)
print()

# Run agent - verbose output will show the reasoning process
result = agent.invoke({"messages": [("user", prompt)]})

# Print all messages to see the ReAct reasoning steps
print("\n" + "=" * 80)
print("ReAct Reasoning Steps (Full Conversation History):")
print("=" * 80 + "\n")

for i, msg in enumerate(result["messages"], 1):
    msg_type = msg.__class__.__name__
    
    # Get message type/role
    if hasattr(msg, "type"):
        role = msg.type
    elif "HumanMessage" in msg_type or "user" in msg_type.lower():
        role = "user"
    elif "AIMessage" in msg_type:
        role = "assistant"
    elif "ToolMessage" in msg_type:
        role = "tool"
    else:
        role = "unknown"
    
    # Display AI reasoning (Thought in ReAct pattern)
    if "AIMessage" in msg_type and hasattr(msg, "content"):
        content = msg.content
        if content and content.strip():
            print(f"[Step {i}] 💭 Thought ({role}):")
            print("-" * 80)
            display_content = content
            if len(content) > MAX_CONTENT_LENGTH:
                display_content = content[:MAX_CONTENT_LENGTH] + f"\n... [truncated, showing first {MAX_CONTENT_LENGTH} chars]"
            print(display_content)
            print()
    
    # Display tool calls (Action in ReAct pattern)
    if hasattr(msg, "tool_calls") and msg.tool_calls:
        print(f"[Step {i}] 🔧 Action (Tool Call):")
        print("-" * 80)
        for tool_call in msg.tool_calls:
            tool_name = tool_call.get('name', 'unknown') if isinstance(tool_call, dict) else getattr(tool_call, 'name', 'unknown')
            tool_args = tool_call.get('args', {}) if isinstance(tool_call, dict) else getattr(tool_call, 'args', {})
            print(f"  Tool: {tool_name}")
            print(f"  Arguments: {tool_args}")
        print()
    
    # Display tool observations (Observation in ReAct pattern)
    if "ToolMessage" in msg_type and hasattr(msg, "content"):
        obs_content = msg.content
        if obs_content:
            print(f"[Step {i}] 👁️  Observation ({role}):")
            print("-" * 80)
            if len(obs_content) > MAX_OBSERVATION_LENGTH:
                obs_content = obs_content[:MAX_OBSERVATION_LENGTH] + "... [truncated]"
            print(obs_content)
            print()
    
    # Display user messages
    if "HumanMessage" in msg_type and hasattr(msg, "content"):
        content = msg.content
        if content:
            print(f"[Step {i}] 👤 User Query:")
            print("-" * 80)
            print(content)
            print()

print("=" * 80)
print("Final Answer:")
print("=" * 80)
print(result["messages"][-1].content)
