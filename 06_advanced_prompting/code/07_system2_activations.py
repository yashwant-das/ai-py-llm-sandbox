"""
System 2 Thinking (Deliberate Reasoning)
========================================
Force slow, analytical thinking instead of quick intuitive responses.

Key Idea: Inspired by Kahneman's "Thinking Fast and Slow":
- System 1: Fast, intuitive, automatic
- System 2: Slow, deliberate, analytical

LLMs often default to System 1. These techniques activate System 2.

When to use:
- Counter-intuitive problems (bat and ball problem)
- Problems where first instinct is often wrong
- Complex reasoning requiring verification
- Mathematical/logical proofs
"""

import sys
from pathlib import Path

# Add project root to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from shared import get_lmstudio_llm

# Initialize LLM
llm = get_lmstudio_llm(temperature=0.1)

print("=" * 80)
print("SYSTEM 2 THINKING (Deliberate Reasoning)")
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
system1_response = llm.invoke(system1_prompt)
print(f"Response: {system1_response.content}\n")

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

system2_response = llm.invoke(system2_prompt)
print(f"Response:\n{system2_response.content}\n")

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

reflection_response = llm.invoke(reflection_prompt)
print(f"Response:\n{reflection_response.content}\n")

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

verification_response = llm.invoke(verification_prompt)
print(f"Response:\n{verification_response.content}\n")

# Example 4: Devil's Advocate / Red Teaming Own Answer
print("=" * 80)
print("--- Example 4: Devil's Advocate (Challenge Own Answer) ---")
print("=" * 80)

ethical_question = "Should AI systems be allowed to make medical diagnoses without human oversight?"
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

da_response = llm.invoke(devils_advocate_prompt)
print(f"Response:\n{da_response.content}\n")

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
generic = llm.invoke(generic_prompt)
print(f"{generic.content}\n")

# With directional stimulus
print("Focused summary (challenges only):")
stimulus_prompt = f"Summarize this text, focusing SPECIFICALLY on the challenges and problems mentioned:\n{text_to_summarize}"
stimulus = llm.invoke(stimulus_prompt)
print(f"{stimulus.content}\n")

print("=" * 80)
print("Key Takeaway: System 2 techniques slow down reasoning for better accuracy.")
print("Techniques: Explicit verification, self-critique, step validation,")
print("            devil's advocate, directional stimulus.")
print("=" * 80)
