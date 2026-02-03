"""
Automatic Prompt Engineering (APE)
==================================
Use LLMs to generate and optimize prompts automatically.

Key Idea: Instead of manually crafting prompts, use an LLM to:
1. Generate candidate prompts for a task
2. Score/evaluate each candidate
3. Select or refine the best one

When to use:
- Finding optimal prompts through search
- Scaling prompt engineering across many tasks
- Meta-learning: prompts that write prompts

Reference: Zhou et al. "Large Language Models Are Human-Level Prompt Engineers"
"""

import sys
from pathlib import Path

# Add project root to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from shared import get_lmstudio_llm

# Initialize LLM
llm = get_lmstudio_llm(temperature=0.7)

print("=" * 80)
print("AUTOMATIC PROMPT ENGINEERING (APE)")
print("=" * 80)

# Example 1: Generating and Selecting Prompts
print("\n--- Example 1: Generate → Score → Refine ---")

task_description = "Classify customer support tickets by urgency: Low, Medium, High"

print(f"Task: {task_description}\n")

# Step 1: Generate candidate prompts
print("=" * 60)
print("STEP 1: Generate Candidate Prompts")
print("=" * 60)

ape_prompt = f"""Given this task: "{task_description}"

Generate 3 different prompts that could be used with an LLM.
Make them:
- Clear and specific
- Include expected output format
- Add any necessary context or constraints

Candidate 1:"""

candidates_response = llm.invoke(ape_prompt)
candidates_text = candidates_response.content

print(f"Candidate Prompts:\n{candidates_text}\n")

# Step 2: Score each candidate
print("=" * 60)
print("STEP 2: Score Candidates")
print("=" * 60)

score_prompt = f"""Evaluate these prompts for the task: "{task_description}"

Prompts:
{candidates_text}

Score each prompt 1-10 on:
1. Clarity (unambiguous instructions)
2. Completeness (covers edge cases)
3. Efficiency (minimal token usage)

Provide numerical scores and brief justification for each."""

scoring = llm.invoke(score_prompt)
print(f"Scoring:\n{scoring.content}\n")

# Step 3: Select and refine the best
print("=" * 60)
print("STEP 3: Refine Best Prompt")
print("=" * 60)

refine_prompt = f"""Based on the evaluation above, create an optimized version
of the best prompt by incorporating the strengths of all candidates.

Original candidates:
{candidates_text}

Optimized prompt (single best version):"""

optimized = llm.invoke(refine_prompt)
print(f"Optimized Prompt:\n{optimized.content}\n")

# Example 2: APE for Few-Shot Example Generation
print("=" * 80)
print("--- Example 2: Auto-Generate Few-Shot Examples ---")
print("=" * 80)

few_shot_task = "Extract product names and prices from product descriptions"

print(f"Task: {few_shot_task}\n")

# Generate examples
example_gen_prompt = f"""For this extraction task: "{few_shot_task}"

Generate 3 diverse examples showing:
- Input: Product description text
- Output: JSON with extracted product_name and price

Make examples cover different product types and price formats."""

examples = llm.invoke(example_gen_prompt)
print(f"Generated Examples:\n{examples.content}\n")

# Use the generated examples to create a complete few-shot prompt
complete_prompt = f"""{few_shot_task}

Examples:
{examples.content}

Now extract from this description:
{{input}}

Output (JSON only):"""

print("=" * 60)
print("Complete Few-Shot Prompt Template:")
print("=" * 60)
print(complete_prompt)

# Example 3: Iterative Prompt Improvement
print("\n" + "=" * 80)
print("--- Example 3: Iterative Improvement Loop ---")
print("=" * 80)

initial_prompt = "Summarize this text."
print(f"Initial prompt: '{initial_prompt}'")

iterations = 3
for i in range(iterations):
    improve_prompt = f"""Improve this prompt for text summarization:
    
Current prompt: "{initial_prompt}"

Critique its weaknesses and provide an improved version.

Improved version:"""
    
    improved = llm.invoke(improve_prompt)
    initial_prompt = improved.content.strip()
    print(f"\nIteration {i+1}: {initial_prompt[:100]}...")

print("\n" + "=" * 80)
print("Key Takeaway: APE automates the search for effective prompts.")
print("Use it when: scaling to many tasks, or when manual iteration is slow.")
print("Combine with: evaluation metrics to objectively score candidates.")
print("=" * 80)
