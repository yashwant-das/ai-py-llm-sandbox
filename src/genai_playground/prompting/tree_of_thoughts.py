"""
Tree of Thoughts (ToT) Prompting
================================
Explore multiple reasoning paths and evaluate them to find the best solution.

Key Idea: Instead of linear reasoning (CoT), branch out and explore multiple
solution paths, then evaluate and select the best one.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "nvapi-dummy"))
)

def get_completion(prompt, temperature=0.5):
    """Helper to get completion from NVIDIA API"""
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL_ID", "meta/llama-3.1-405b-instruct"),
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content


print("=" * 80)
print("TREE OF THOUGHTS (ToT) [NVIDIA API]")
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

Solution {i + 1} (provide detailed steps):"""

    solution = get_completion(tot_prompt)
    solutions.append(solution)
    print(f"\n--- Solution {i + 1} ---")
    print(solution[:400] + "..." if len(solution) > 400 else solution)

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

evaluation = get_completion(eval_prompt)
print(f"\n{evaluation}")

# Example 2: Creative Writing with Multiple Paths
print("\n" + "=" * 80)
print("--- Example 2: Creative Writing Exploration ---")
print("=" * 80)

story_prompt = (
    "Write an opening paragraph for a mystery novel about a missing painting."
)

# Generate diverse approaches
approaches = [
    "atmospheric and gothic",
    "fast-paced and action-oriented",
    "character-driven and introspective",
]

stories = []
for style in approaches:
    prompt = f"{story_prompt}\n\nStyle: {style}\n\nOpening paragraph:"
    story = get_completion(prompt)
    stories.append((style, story))
    print(f"\n--- {style.title()} ---")
    print(story[:300] + "...")

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

selection = get_completion(selection_prompt)
print(selection)

print("\n" + "=" * 80)
print("Key Takeaway: Tree of Thoughts explores multiple solution paths,")
print("evaluates them systematically, and selects or combines the best elements.")
print("Trade-off: More LLM calls for potentially better solutions.")
print("=" * 80)
