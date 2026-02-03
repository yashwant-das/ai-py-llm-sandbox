"""
Role/Persona Prompting
======================
Assigning a specific role or persona to the model to guide its
response style, tone, and expertise level.

When to use:
- Need domain-specific expertise
- Want a specific tone or style
- Explaining complex topics to different audiences
- Creative writing tasks

Tips:
- Be specific about the role ("You are a...")
- Define the audience if relevant
- Combine with other techniques (CoT, few-shot) for best results

Topic: 05_prompt_engineering_fundamentals
Refer to: ../README.md for more information
"""

import sys
from pathlib import Path

# Add project root to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from shared import get_lmstudio_llm

# Initialize LLM
llm = get_lmstudio_llm(temperature=0.7)

print("=" * 80)
print("ROLE/PERSONA PROMPTING EXAMPLES")
print("=" * 80)

# Example 1: Explaining to different audiences
print("\n--- Example 1: Same Topic, Different Audiences ---")

topic = "How does photosynthesis work?"

# Role: Expert to expert
prompt1 = f"""You are a PhD-level plant biologist speaking at a conference of botanists.
Explain {topic}

Explanation:"""
response1 = llm.invoke(prompt1)
print(f"ROLE: Expert Botanist to Botanists")
print(f"Response: {response1.content[:300]}...")
print()

# Role: Teacher to 5-year-old
prompt2 = f"""You are a kindergarten teacher explaining to a class of 5-year-olds.
Explain {topic} using simple words and analogies they understand.

Explanation:"""
response2 = llm.invoke(prompt2)
print(f"ROLE: Kindergarten Teacher")
print(f"Response: {response2.content[:300]}...")

# Example 2: Domain expert consultant
print("\n--- Example 2: Security Expert Consultant ---")
prompt3 = """You are a cybersecurity expert with 20 years of experience.
A small business owner asks you: "What are the top 3 things I should do 
to protect my business from hackers?"

Provide practical, actionable advice."""
response3 = llm.invoke(prompt3)
print(f"ROLE: Cybersecurity Expert")
print(f"Response:\n{response3.content}")

# Example 3: Creative writing roles
print("\n--- Example 3: Creative Writing - Different Styles ---")
story_prompt = "Write a 3-sentence description of a rainy evening in the city."

# Role: Noir detective novelist
prompt4 = f"""You are a noir detective novelist from the 1940s.
{story_prompt}"""
response4 = llm.invoke(prompt4)
print(f"ROLE: Noir Detective Novelist")
print(f"Response: {response4.content}")
print()

# Role: Optimistic children's author
prompt5 = f"""You are an optimistic children's book author.
{story_prompt}"""
response5 = llm.invoke(prompt5)
print(f"ROLE: Children's Book Author")
print(f"Response: {response5.content}")

# Example 4: Critical reviewer role
print("\n--- Example 4: Code Reviewer Role ---")
code_snippet = """
def process_data(data):
    result = []
    for i in range(len(data)):
        result.append(data[i] * 2)
    return result
"""
prompt6 = f"""You are a senior software engineer conducting a code review.
Review the following Python code for:
1. Potential bugs
2. Performance issues
3. Code style improvements

Code:
{code_snippet}

Code Review:"""
response6 = llm.invoke(prompt6)
print(f"ROLE: Senior Software Engineer (Code Reviewer)")
print(f"Response:\n{response6.content}")

# Example 5: Debate format with multiple roles
print("\n--- Example 5: Multi-Persona Debate ---")
topic = "Should companies allow remote work permanently?"

prompt7 = f"""You are participating in a debate on: "{topic}"

First, argue as a CEO who wants employees in the office:
CEO Argument:"""
response7 = llm.invoke(prompt7)
print(f"ROLE: CEO")
print(f"Response: {response7.content[:200]}...")

prompt8 = f"""Now argue as an employee who prefers working from home:
Employee Argument:"""
response8 = llm.invoke(prompt8)
print(f"\nROLE: Remote Employee")
print(f"Response: {response8.content[:200]}...")

# Example 6: Role with constraints
print("\n--- Example 6: Role with Constraints ---")
prompt9 = """You are a travel agent who specializes in budget travel.
Your constraints:
- Only recommend destinations under $1000 for a week
- Focus on experiences, not luxury
- Be enthusiastic but honest about drawbacks

A customer asks: "Where should I go for my first international trip?"

Recommendation:"""
response9 = llm.invoke(prompt9)
print(f"ROLE: Budget Travel Agent (with constraints)")
print(f"Response:\n{response9.content}")

print("\n" + "=" * 80)
print("Key Takeaway: Role prompting shapes the model's expertise, tone,")
print("and perspective. Combine with other techniques for powerful results.")
print("=" * 80)
