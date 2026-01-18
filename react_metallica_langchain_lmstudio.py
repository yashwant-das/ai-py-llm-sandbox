from ddgs import DDGS
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


@tool
def search(query: str) -> str:
    """Search the web via DuckDuckGo and return results."""
    with DDGS() as ddg:
        results = ddg.text(query, max_results=3)
    if results:
        return results[0].get("body") or results[0].get("title", "No snippet")
    return "No results found."


# Initialize LLM (LM Studio)
llm = ChatOpenAI(
    model="google/gemma-3-4b",
    temperature=0.1,
    openai_api_key="lm-studio",
    openai_api_base="http://127.0.0.1:1234/v1",
)

# Create agent with tools
tools = [search]
agent = create_agent(llm, tools)

# Run agent
prompt = "How many kids do the band members of Metallica have?"
result = agent.invoke({"messages": [("user", prompt)]})
print(result["messages"][-1].content)
