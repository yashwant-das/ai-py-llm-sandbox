"""
Tree of Thoughts (ToT) Prompting
================================
Explore multiple reasoning paths and evaluate them to find the best solution.

Key Idea: Instead of linear reasoning (CoT), branch out and explore multiple
solution paths, then evaluate and select the best one.

When to use:
- Problems with multiple valid approaches
- Creative tasks requiring exploration
- Optimization problems
- When a single reasoning path might get stuck

Reference: Yao et al. "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
"""

import sys
from pathlib import Path

# Add project root to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import os
from shared import get_llm

# Initialize LLM (provider configurable via LLM_PROVIDER env var)
# Options: "lmstudio", "ollama", "openai", or "auto"
llm = get_llm(provider=os.getenv("LLM_PROVIDER", "lmstudio"), temperature=0.5)

print("=" * 80)
print("TREE OF THOUGHTS (ToT)")
print("=" * 80)

# Example: River Crossing Puzzle (classic planning problem)
print("\n--- Example 1: River Crossing Puzzle ---")
print("Explore multiple solution paths and evaluate each.\n")

tot_problem = """A farmer needs to transport a wolf, a goat, and a cabbage across a river.
The boat can only carry the farmer and one item at a time.
If left alone, the wolf will eat the goat, and the goat will eat the cabbage.
How can the farmer get everything across safely?"""

print(f"Problem:\n{tot_problem}\n")

# Step 1: Generate multiple solution attempts (breadth)
print("=" * 60)
print("STEP 1: Generate Multiple Solution Approaches")
print("=" * 60)

num_solutions = 3
solutions = []

for i in range(num_solutions):
    tot_prompt = f"""Solve this river crossing puzzle.
Show your step-by-step solution.
Think carefully about the constraints.

{tot_problem}

Solution {i+1} (provide detailed steps):"""
    
    solution = llm.invoke(tot_prompt)
    solutions.append(solution.content)
    print(f"\n--- Solution {i+1} ---")
    print(solution.content[:400] + "..." if len(solution.content) > 400 else solution.content)

# Step 2: Evaluate solutions (scoring)
print("\n" + "=" * 60)
print("STEP 2: Evaluate Solutions")
print("=" * 60)

eval_prompt = f"""Evaluate these {num_solutions} solutions to the river crossing puzzle.
Score each solution on:
1. Correctness (follows all rules): 0-10
2. Completeness (all items get across): 0-10
3. Efficiency (fewest steps): 0-10

Solution 1:
{solutions[0]}

Solution 2:
{solutions[1]}

Solution 3:
{solutions[2]}

Provide scores and identify the best solution. If none are fully correct, 
describe what the correct solution should be."""

evaluation = llm.invoke(eval_prompt)
print(f"\n{evaluation.content}")

# Example 2: Creative Writing with Multiple Paths
print("\n" + "=" * 80)
print("--- Example 2: Creative Writing Exploration ---")
print("=" * 80)

story_prompt = "Write an opening paragraph for a mystery novel about a missing painting."

# Generate diverse approaches
approaches = [
    "atmospheric and gothic",
    "fast-paced and action-oriented", 
    "character-driven and introspective"
]

stories = []
for style in approaches:
    prompt = f"{story_prompt}\n\nStyle: {style}\n\nOpening paragraph:"
    story = llm.invoke(prompt)
    stories.append((style, story.content))
    print(f"\n--- {style.title()} ---")
    print(story.content[:300] + "...")

# Evaluate and select or combine
print("\n--- Evaluation ---")
selection_prompt = f"""Given these three opening paragraphs for a mystery novel:

1. Gothic: {stories[0][1][:200]}

2. Action: {stories[1][1][:200]}

3. Character-driven: {stories[2][1][:200]}

Evaluate each on:
- Hook (grabs attention immediately)
- Tone consistency
- Mystery setup (establishes the puzzle)

Which approach works best and why?"""

selection = llm.invoke(selection_prompt)
print(selection.content)

print("\n" + "=" * 80)
print("Key Takeaway: Tree of Thoughts explores multiple solution paths,")
print("evaluates them systematically, and selects or combines the best elements.")
print("Trade-off: More LLM calls for potentially better solutions.")
print("=" * 80)
