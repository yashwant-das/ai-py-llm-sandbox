"""
Raw SDK vs LangChain: A Side-by-Side Comparison
================================================

This file demonstrates the same zero-shot prompting task using:
1. Raw OpenAI SDK (transparent, explicit)
2. LangChain (convenient, abstracted)

Understanding both approaches helps you:
- See what LangChain is doing under the hood
- Debug issues when things go wrong
- Choose the right tool for the job

Topic: 05_prompt_engineering_fundamentals
"""

import os
import sys
from pathlib import Path

# Add project root to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# =============================================================================
# OPTION 1: Raw OpenAI SDK (Explicit, Transparent)
# =============================================================================
# Best for: Learning, debugging, minimal dependencies, understanding the API

from openai import OpenAI
from shared import get_settings

print("=" * 80)
print("OPTION 1: Raw OpenAI SDK")
print("=" * 80)

settings = get_settings()

# Create client - this is exactly what happens under the hood
raw_client = OpenAI(
    base_url=settings.lmstudio_base_url,  # http://127.0.0.1:1234/v1
    api_key=settings.lmstudio_api_key,     # lm-studio
)

# Make the API call - explicit, no magic
raw_response = raw_client.chat.completions.create(
    model=settings.default_model,  # openai/gpt-oss-20b
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is 2+2? Answer in one word."}
    ],
    temperature=0.1,
    max_tokens=10,
)

# Access the response - you see the full data structure
print(f"\nFull response object:")
print(f"  Type: {type(raw_response)}")
print(f"  Model: {raw_response.model}")
print(f"  Usage: {raw_response.usage}")
print(f"\nContent:")
print(f"  {raw_response.choices[0].message.content}")


# =============================================================================
# OPTION 2: LangChain (Convenient, Abstracted)
# =============================================================================
# Best for: Chains, agents, RAG, rapid prototyping, ecosystem integration

from shared import get_llm

print("\n" + "=" * 80)
print("OPTION 2: LangChain")
print("=" * 80)

# Get LLM - configuration is abstracted
lc_llm = get_llm(provider=os.getenv("LLM_PROVIDER", "lmstudio"), temperature=0.1)

# Invoke - simpler interface, but less visibility
lc_response = lc_llm.invoke("What is 2+2? Answer in one word.")

print(f"\nResponse object:")
print(f"  Type: {type(lc_response)}")
print(f"\nContent:")
print(f"  {lc_response.content}")


# =============================================================================
# KEY DIFFERENCES
# =============================================================================

print("\n" + "=" * 80)
print("KEY DIFFERENCES")
print("=" * 80)

print("""
1. MESSAGE FORMAT
   Raw SDK:    messages=[{"role": "user", "content": "..."}]
   LangChain:  llm.invoke("...") or ChatPromptTemplate

2. RESPONSE ACCESS
   Raw SDK:    response.choices[0].message.content
   LangChain:  response.content

3. CONFIGURATION
   Raw SDK:    Explicit base_url, api_key, model per call
   LangChain:  Abstracted via environment/config files

4. DEBUGGING
   Raw SDK:    Full response object visible (usage, model, etc.)
   LangChain:  Simplified output (content, metadata)

5. EXTENSIBILITY
   Raw SDK:    Manual chaining, tool calling, error handling
   LangChain:  Built-in chains, agents, memory, vector stores
""")


# =============================================================================
# WHEN TO USE WHICH?
# =============================================================================

print("=" * 80)
print("WHEN TO USE WHICH?")
print("=" * 80)

print("""
Use RAW OPENAI SDK when:
- Learning how LLM APIs work
- Debugging issues with LangChain
- Building minimal dependencies
- You need full control over the request/response
- Educational purposes (like this repo!)

Use LANGCHAIN when:
- Building chains of operations
- Creating agents with tools
- Working with RAG (retrieval)
- Need memory/conversation history
- Rapid prototyping
- Using the broader LangChain ecosystem

RECOMMENDATION FOR LEARNING:
- Start with Raw SDK (Topics 5-6) to understand the fundamentals
- Switch to LangChain (Topics 12, 16, 18) when you need its features
- This repo uses LangChain for convenience, but now you know what's under the hood!
""")


# =============================================================================
# BONUS: Raw SDK with Different Providers
# =============================================================================

print("\n" + "=" * 80)
print("BONUS: Raw SDK Works with Any OpenAI-Compatible Endpoint")
print("=" * 80)

print("""
The beauty of the OpenAI SDK pattern is it works with:

1. LM Studio:    base_url="http://localhost:1234/v1"
2. Ollama:       base_url="http://localhost:11434/v1"
3. OpenAI:       base_url="https://api.openai.com/v1" (default)
4. Groq:         base_url="https://api.groq.com/openai/v1"
5. Together:     base_url="https://api.together.xyz/v1"

Same code, just different base_url!
""")

print("=" * 80)
print("End of comparison")
print("=" * 80)
