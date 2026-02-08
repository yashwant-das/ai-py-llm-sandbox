"""
Self-Consistency / Ensemble Methods
====================================
Generating multiple responses and selecting the best answer through
voting, averaging, or consistency checks. Reduces random errors.
"""

import os
import re
from collections import Counter
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

def get_completion(prompt, temperature=0.7):
    """Helper to get completion from NVIDIA API"""
    response = client.chat.completions.create(
        model="meta/llama-3.1-405b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content


print("=" * 80)
print("SELF-CONSISTENCY / ENSEMBLE METHODS (NVIDIA API)")
print("=" * 80)


def extract_final_answer(text):
    """Simple extraction of numeric or short answers."""
    # Try to find "Answer: X" pattern
    match = re.search(r"[Aa]nswer[:\s]+([\d.]+|[^\n]+)", text)
    if match:
        return match.group(1).strip()
    # Return last number found
    numbers = re.findall(r"\d+", text)
    if numbers:
        return numbers[-1]
    return text.strip()[-50:]  # Last 50 chars


# Example 1: Math Problem with Self-Consistency
print("\n--- Example 1: Math Problem with Majority Voting ---")

math_problem = """Solve this problem step by step:
A store is having a 25% off sale. If an item originally costs $80,
what is the final price after the discount?

Provide your answer clearly at the end as: Answer: $X"""

# Generate multiple solutions
num_samples = 3
responses = []
print(f"Generating {num_samples} solutions...\n")

for i in range(num_samples):
    content = get_completion(math_problem)
    answer = extract_final_answer(content)
    responses.append((answer, content))
    print(f"Attempt {i + 1}:")
    print(f"  Raw answer: {answer}")
    print(f"  Response preview: {content[:100]}...\n")

# Extract just the numeric parts for voting
answers = [r[0] for r in responses]
print(f"All extracted answers: {answers}")

# Simple majority voting (exact match)
vote_counts = Counter(answers)
most_common = vote_counts.most_common(1)[0]
print(f"\nMajority vote result: {most_common[0]} (appears {most_common[1]} times)")

# Example 2: Reasoning Verification
print("\n--- Example 2: Verify Reasoning Consistency ---")

reasoning_problem = """Jack is looking at Anne. Anne is looking at George. 
Jack is married, George is not married. Is a married person looking at 
an unmarried person? Answer Yes, No, or Cannot be determined."""

verification_prompt = f"""Analyze this logic puzzle carefully:

{reasoning_problem}

First, state your reasoning clearly, then provide your final answer.
Answer:"""

# Generate multiple reasonings
print("Generating multiple reasoning paths...\n")
reasonings = []
for i in range(3):
    content = get_completion(verification_prompt)
    # Extract just Yes/No/Cannot
    answer = "Unknown"
    if "yes" in content.lower():
        answer = "Yes"
    elif "no" in content.lower() and "cannot" not in content.lower():
        answer = "No"
    elif "cannot" in content.lower():
        answer = "Cannot be determined"
    reasonings.append(answer)
    print(f"Attempt {i + 1}: {answer}")

# Vote on reasonings
reasoning_votes = Counter(reasonings)
print(f"\nVoting results: {dict(reasoning_votes)}")
final_answer = reasoning_votes.most_common(1)[0][0]
print(f"Most consistent answer: {final_answer}")

# Example 3: Confidence-based Selection
print("\n--- Example 3: Confidence Scoring ---")

confidence_prompt = """Answer the following question and rate your confidence (0-100).
Question: What is the capital of Australia?

Format your response as:
Answer: [your answer]
Confidence: [0-100]
Reasoning: [brief explanation]"""

print("Generating responses with confidence scores...\n")
confident_answers = []
for i in range(3):
    content = get_completion(confidence_prompt)
    print(f"Attempt {i + 1}:")
    print(f"  {content}\n")

    # Parse confidence
    conf_match = re.search(r"[Cc]onfidence[:\s]+(\d+)", content)
    confidence = int(conf_match.group(1)) if conf_match else 50

    # Parse answer
    ans_match = re.search(r"[Aa]nswer[:\s]+([^\n]+)", content)
    answer = ans_match.group(1).strip() if ans_match else "Unknown"

    confident_answers.append((answer, confidence, content))

# Select highest confidence answer
best_answer = max(confident_answers, key=lambda x: x[1])
print(f"Highest confidence answer: {best_answer[0]} (confidence: {best_answer[1]})")

# Example 4: Self-Correction / Reflection
print("\n--- Example 4: Self-Correction (Reflection) ---")

initial_problem = """Calculate: 15 * 8 + 25 * 4"""

# First attempt
print("Initial attempt:")
initial_response = get_completion(initial_problem)
print(f"  Response: {initial_response}")

# Self-correction prompt
reflection_prompt = f"""You previously answered: "{initial_response}"

For the problem: {initial_problem}

Please review your work. Check for any calculation errors.
If you find mistakes, provide the corrected answer.
If your answer was correct, confirm it.

Review:"""

print("\nReflection/Correction:")
reflection_response = get_completion(reflection_prompt)
print(f"  Response: {reflection_response}")

# Example 5: Debate/Simulation Method
print("\n--- Example 5: Simulated Debate for Complex Questions ---")

debate_topic = """Should a company prioritize user privacy or data collection 
for improving their AI products?"""

# Pro side
pro_prompt = f"""You are arguing FOR prioritizing user privacy over data collection.
Topic: {debate_topic}

Provide your strongest arguments:"""

# Con side
con_prompt = f"""You are arguing FOR prioritizing data collection to improve AI products.
Topic: {debate_topic}

Provide your strongest arguments:"""

print("Generating pro arguments...")
pro_response = get_completion(pro_prompt)
print(f"Pro: {pro_response[:200]}...")

print("\nGenerating con arguments...")
con_response = get_completion(con_prompt)
print(f"Con: {con_response[:200]}...")

# Synthesis
synthesis_prompt = f"""Based on these two perspectives:

PRO (Privacy): {pro_response[:300]}

CON (Data Collection): {con_response[:300]}

Provide a balanced synthesis that acknowledges both viewpoints and 
proposes a middle-ground approach.

Synthesis:"""

print("\nSynthesizing balanced view...")
synthesis_response = get_completion(synthesis_prompt)
print(f"Synthesis: {synthesis_response}")

print("\n" + "=" * 80)
print("Key Takeaway: Self-consistency reduces errors by sampling multiple")
print("solutions and selecting the most reliable answer. Trade-off: more API calls.")
print("=" * 80)
