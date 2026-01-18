import os

from ddgs import DDGS
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from serpapi import GoogleSearch

# Load environment variables from .env file
load_dotenv()


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

# Create agent with tools
tools = [search_google]
agent = create_agent(llm, tools)

# Run agent
prompt = "How many kids do the band members of Metallica have?"
result = agent.invoke({"messages": [("user", prompt)]})
print(result["messages"][-1].content)
