"""
System 2 Thinking (Deliberate Reasoning)
========================================
Force slow, analytical thinking instead of quick intuitive responses.

Key Idea: Inspired by Kahneman's "Thinking Fast and Slow":
- System 1: Fast, intuitive, automatic
- System 2: Slow, deliberate, analytical

LLMs often default to System 1. These techniques activate System 2.
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
print("SYSTEM 2 THINKING (Deliberate Reasoning) [NVIDIA API]")
print("=" * 80)

# Example 1: The Classic Bat and Ball Problem
print("\n--- Example 1: Bat and Ball (Counter-Intuitive) ---")
print("Many people's intuition says $1, but the correct answer is $0.50\n")

problem = """A bat and a ball cost $11 in total.
The bat costs $10 more than the ball.
How much does the ball cost?"""

# System 1 (quick response) - simulate by asking directly
print("=" * 60)
print("SYSTEM 1 (Quick Intuition):")
print("=" * 60)
system1_prompt = f"{problem}\n\nAnswer immediately:"
system1_response = get_completion(system1_prompt)
print(f"Response: {system1_response}\n")

# System 2 (deliberate analysis)
print("=" * 60)
print("SYSTEM 2 (Deliberate Analysis):")
print("=" * 60)
system2_prompt = f"""Solve this carefully. Many people get this wrong on first instinct.

{problem}

DO NOT rush. Follow these steps:
1. Define variables
2. Set up equations
3. Solve algebraically
4. VERIFY your answer by substituting back
5. Confirm the bat costs exactly $10 more than the ball

Step-by-step solution:"""

system2_response = get_completion(system2_prompt)
print(f"Response:\n{system2_response}\n")

# Example 2: Self-Correction / Reflection
print("=" * 80)
print("--- Example 2: Self-Correction with Reflection ---")
print("=" * 80)

logic_problem = """If it takes 5 machines 5 minutes to make 5 widgets,
how long would it take 100 machines to make 100 widgets?"""

print(f"Problem: {logic_problem}\n")

reflection_prompt = f"""Solve this problem: 

{logic_problem}

First, write your initial answer.
Then, critique your own reasoning - look for assumptions or errors.
Finally, provide your corrected final answer.

Format:
Initial Answer: 
Self-Critique:
Final Answer:"""

reflection_response = get_completion(reflection_prompt)
print(f"Response:\n{reflection_response}\n")

# Example 3: Step Verification
print("=" * 80)
print("--- Example 3: Step-by-Step Verification ---")
print("=" * 80)

math_problem = "Calculate: 17 * 24"
print(f"Problem: {math_problem}\n")

verification_prompt = f"""Solve this multiplication step by step:

{math_problem}

For each step:
1. Show the calculation
2. VERIFY the step is correct
3. Only proceed if verified

Example format:
Step 1: ...
Verification: ...
Step 2: ...
Verification: ...
Final Answer: ...
Verification of final answer: ..."""

verification_response = get_completion(verification_prompt)
print(f"Response:\n{verification_response}\n")

# Example 4: Devil's Advocate / Red Teaming Own Answer
print("=" * 80)
print("--- Example 4: Devil's Advocate (Challenge Own Answer) ---")
print("=" * 80)

ethical_question = (
    "Should AI systems be allowed to make medical diagnoses without human oversight?"
)
print(f"Question: {ethical_question}\n")

devils_advocate_prompt = f"""Analyze this question: {ethical_question}

Step 1: Provide your initial position with arguments.

Step 2: Play devil's advocate. Challenge every argument you made.
Look for: weak premises, overlooked counter-examples, hidden assumptions.

Step 3: Synthesize a balanced conclusion that addresses the strongest
arguments on both sides.

Format:
Initial Position:
Devil's Advocate Challenges:
Balanced Conclusion:"""

da_response = get_completion(devils_advocate_prompt)
print(f"Response:\n{da_response}\n")

# Example 5: Directional Stimulus (Guide Focus)
print("=" * 80)
print("--- Example 5: Directional Stimulus Prompting ---")
print("=" * 80)

text_to_summarize = """Artificial intelligence has made significant strides in recent years. 
Machine learning models can now process natural language, recognize images, 
and even generate creative content. However, challenges remain in areas 
like reasoning, common sense understanding, and ensuring AI safety. 
Researchers are working on alignment problems to ensure AI systems 
benefit humanity."""

print("Text to summarize (about AI progress)...\n")

# Without stimulus
print("Generic summary:")
generic_prompt = f"Summarize this text:\n{text_to_summarize}"
generic = get_completion(generic_prompt)
print(f"{generic}\n")

# With directional stimulus
print("Focused summary (challenges only):")
stimulus_prompt = f"Summarize this text, focusing SPECIFICALLY on the challenges and problems mentioned:\n{text_to_summarize}"
stimulus = get_completion(stimulus_prompt)
print(f"{stimulus}\n")

print("=" * 80)
print("Key Takeaway: System 2 techniques slow down reasoning for better accuracy.")
print("Techniques: Explicit verification, self-critique, step validation,")
print("            devil's advocate, directional stimulus.")
print("=" * 80)
