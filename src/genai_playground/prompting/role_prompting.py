"""
Role/Persona Prompting
======================
Assigning a specific role or persona to the model to guide its
response style, tone, and expertise level.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "nvapi-dummy"))
)

def get_completion(prompt, temperature=0.7):
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL_ID", "meta/llama-3.1-405b-instruct"),
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=1024,
    )
    return response.choices[0].message.content

print("=" * 80)
print("ROLE/PERSONA PROMPTING EXAMPLES (NVIDIA API)")
print("=" * 80)

# Example 1: Explaining to different audiences
print("\n--- Example 1: Same Topic, Different Audiences ---")

topic = "How does photosynthesis work?"

# Role: Expert to expert
prompt1 = f"""You are a PhD-level plant biologist speaking at a conference of botanists.
Explain {topic}

Explanation:"""
response1 = get_completion(prompt1)
print("ROLE: Expert Botanist to Botanists")
print(f"Response: {response1[:300]}...")
print()

# Role: Teacher to 5-year-old
prompt2 = f"""You are a kindergarten teacher explaining to a class of 5-year-olds.
Explain {topic} using simple words and analogies they understand.

Explanation:"""
response2 = get_completion(prompt2)
print("ROLE: Kindergarten Teacher")
print(f"Response: {response2[:300]}...")

# Example 2: Domain expert consultant
print("\n--- Example 2: Security Expert Consultant ---")
prompt3 = """You are a cybersecurity expert with 20 years of experience.
A small business owner asks you: "What are the top 3 things I should do 
to protect my business from hackers?"

Provide practical, actionable advice."""
response3 = get_completion(prompt3)
print("ROLE: Cybersecurity Expert")
print(f"Response:\n{response3}")

# Example 3: Creative writing roles
print("\n--- Example 3: Creative Writing - Different Styles ---")
story_prompt = "Write a 3-sentence description of a rainy evening in the city."

# Role: Noir detective novelist
prompt4 = f"""You are a noir detective novelist from the 1940s.
{story_prompt}"""
response4 = get_completion(prompt4)
print("ROLE: Noir Detective Novelist")
print(f"Response: {response4}")
print()

# Role: Optimistic children's author
prompt5 = f"""You are an optimistic children's book author.
{story_prompt}"""
response5 = get_completion(prompt5)
print("ROLE: Children's Book Author")
print(f"Response: {response5}")

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
response6 = get_completion(prompt6)
print("ROLE: Senior Software Engineer (Code Reviewer)")
print(f"Response:\n{response6}")

# Example 5: Multi-Persona Debate
print("\n--- Example 5: Multi-Persona Debate ---")
topic = "Should companies allow remote work permanently?"

prompt7 = f"""You are participating in a debate on: "{topic}"

First, argue as a CEO who wants employees in the office:
CEO Argument:"""
response7 = get_completion(prompt7)
print("ROLE: CEO")
print(f"Response: {response7[:200]}...")

prompt8 = """Now argue as an employee who prefers working from home:
Employee Argument:"""
response8 = get_completion(prompt8)
print("\nROLE: Remote Employee")
print(f"Response: {response8[:200]}...")

# Example 6: Role with constraints
print("\n--- Example 6: Role with Constraints ---")
prompt9 = """You are a travel agent who specializes in budget travel.
Your constraints:
- Only recommend destinations under $1000 for a week
- Focus on experiences, not luxury
- Be enthusiastic but honest about drawbacks

A customer asks: "Where should I go for my first international trip?"

Recommendation:"""
response9 = get_completion(prompt9)
print("ROLE: Budget Travel Agent (with constraints)")
print(f"Response:\n{response9}")

print("\n" + "=" * 80)
print("Key Takeaway: Role prompting shapes the model's expertise, tone,")
print("and perspective. Combine with other techniques for powerful results.")
print("=" * 80)
