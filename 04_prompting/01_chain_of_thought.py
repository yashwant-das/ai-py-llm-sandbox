"""
Chain-of-Thought (CoT) Prompting
=================================
Prompting the model to show its reasoning step-by-step before giving
the final answer. This improves performance on complex reasoning tasks.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

def get_completion(prompt, temperature=0.1):
    """Helper to get completion from NVIDIA API"""
    response = client.chat.completions.create(
        model="meta/llama-3.1-405b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content


print("=" * 80)
print("CHAIN-OF-THOUGHT PROMPTING EXAMPLES (NVIDIA API)")
print("=" * 80)

# Example 1: Math problem with zero-shot CoT
print("\n--- Example 1: Math Problem (Zero-shot CoT) ---")
prompt1 = """Solve this math problem step by step.

Problem: A baker made 48 cookies. She sold 1/3 of them in the morning 
and 1/4 of the remaining in the afternoon. How many cookies does she have left?

Let's think step by step."""
response1 = get_completion(prompt1)
print(f"Prompt:\n{prompt1}")
print(f"\nResponse:\n{response1}")

# Example 2: Logic puzzle with CoT
print("\n--- Example 2: Logic Puzzle ---")
prompt2 = """Solve this puzzle by thinking through each clue.

Puzzle: Three friends - Alice, Bob, and Carol - have different favorite colors:
red, blue, and green. Clues:
1. Alice doesn't like red
2. Bob doesn't like blue
3. The person who likes green is not Alice or Bob

What is each person's favorite color? Think step by step."""
response2 = get_completion(prompt2)
print(f"Prompt:\n{prompt2}")
print(f"\nResponse:\n{response2}")

# Example 3: Few-shot CoT for math
print("\n--- Example 3: Few-shot CoT (Math Problems) ---")
prompt3 = """Solve the following problems by showing your reasoning.

Problem: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. 
Each can has 3 tennis balls. How many tennis balls does he have now?
Reasoning: Roger starts with 5 balls. 2 cans of 3 balls each is 2 * 3 = 6 balls.
5 + 6 = 11. So Roger has 11 tennis balls.
Answer: 11

Problem: A train travels 60 miles per hour. How far will it travel in 2.5 hours?
Reasoning: Distance equals speed times time. 60 miles/hour * 2.5 hours = 150 miles.
Answer: 150

Problem: A rectangle has a length of 8 cm and a width of 5 cm. What is its area?
Reasoning:"""
response3 = get_completion(prompt3)
print(f"Prompt:\n{prompt3}")
print(f"\nResponse:\n{response3}")

# Example 4: Decision making with CoT
print("\n--- Example 4: Decision Making ---")
prompt4 = """Help make a decision by weighing the pros and cons.

Scenario: Should I buy a laptop or a desktop for programming work?
I work from home 3 days a week and travel 2 days a week.

Think through the factors step by step and provide a recommendation."""
response4 = get_completion(prompt4)
print(f"Prompt:\n{prompt4}")
print(f"\nResponse:\n{response4}")

# Example 5: Code explanation with CoT
print("\n--- Example 5: Code Analysis ---")
prompt5 = """Analyze this code step by step and find any bugs.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n)
```

Walk through your analysis step by step."""
response5 = get_completion(prompt5)
print(f"Prompt:\n{prompt5}")
print(f"\nResponse:\n{response5}")

# Example 6: Comparison - Without vs With CoT
print("\n--- Example 6: Comparison (Without vs With CoT) ---")

# Without CoT
prompt_without = """What is 15% of 80 plus 20% of 50?"""
response_without = get_completion(prompt_without)
print(f"WITHOUT CoT:\nPrompt: {prompt_without}")
print(f"Response: {response_without}")

# With CoT
prompt_with = """What is 15% of 80 plus 20% of 50?

Think step by step."""
response_with = get_completion(prompt_with)
print(f"\nWITH CoT:\nPrompt: {prompt_with}")
print(f"Response: {response_with}")

print("\n" + "=" * 80)
print("Key Takeaway: CoT prompting dramatically improves complex reasoning.")
print("The phrase 'Let's think step by step' is a simple but effective trigger.")
print("=" * 80)
