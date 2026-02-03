"""
Zero-Shot Prompting
===================
The simplest form of prompting - just give the model an instruction
directly without any examples. The model relies on its pre-trained knowledge.

When to use:
- Simple, straightforward tasks
- When the model already knows the pattern
- Quick prototyping

Tips:
- Be specific and clear in your instructions
- Include constraints directly in the prompt

Topic: 05_prompt_engineering_fundamentals
Refer to: ../README.md for more information
"""

import os
import sys
from pathlib import Path

# Add project root to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from shared import get_llm

# Initialize LLM (reads LLM_PROVIDER from env, defaults to "lmstudio")
# Options: "lmstudio", "ollama", "openai", or "auto" (tries all)
llm = get_llm(provider=os.getenv("LLM_PROVIDER", "lmstudio"), temperature=0.1)

print("=" * 80)
print("ZERO-SHOT PROMPTING EXAMPLES")
print("=" * 80)

# Example 1: Simple classification
print("\n--- Example 1: Sentiment Classification ---")
prompt1 = """Classify the sentiment of this text as Positive, Negative, or Neutral:
"I absolutely loved the movie! The acting was superb."

Sentiment:"""
response1 = llm.invoke(prompt1)
print(f"Prompt: {prompt1}")
print(f"Response: {response1.content}")

# Example 2: Summarization with constraints
print("\n--- Example 2: Summarization with Constraints ---")
prompt2 = """Summarize the following text in exactly 2 sentences:

The James Webb Space Telescope (JWST) is a space telescope designed to conduct 
infrared astronomy. It was launched on December 25, 2021, and is the largest 
optical telescope in space. Its high resolution and sensitivity allow it to 
view objects too old, distant, or faint for the Hubble Space Telescope.

Summary:"""
response2 = llm.invoke(prompt2)
print(f"Prompt: {prompt2}")
print(f"Response: {response2.content}")

# Example 3: Format conversion
print("\n--- Example 3: Format Conversion ---")
prompt3 = """Convert this unstructured data into a bullet list:
Apple was founded by Steve Jobs Steve Wozniak and Ronald Wayne in 1976 
in Cupertino California.

Bullet list:"""
response3 = llm.invoke(prompt3)
print(f"Prompt: {prompt3}")
print(f"Response: {response3.content}")

# Example 4: Code generation
print("\n--- Example 4: Code Generation ---")
prompt4 = """Write a Python function that takes a list of numbers and returns 
the sum of all even numbers in the list.

Function:"""
response4 = llm.invoke(prompt4)
print(f"Prompt: {prompt4}")
print(f"Response:\n{response4.content}")

# Example 5: Question answering
print("\n--- Example 5: Question Answering ---")
prompt5 = """Answer the following question concisely:
What is the difference between HTTP and HTTPS?

Answer:"""
response5 = llm.invoke(prompt5)
print(f"Prompt: {prompt5}")
print(f"Response: {response5.content}")

print("\n" + "=" * 80)
print("Key Takeaway: Zero-shot works well for straightforward tasks where")
print("the pattern is clear. Add examples (few-shot) when results are inconsistent.")
print("=" * 80)
