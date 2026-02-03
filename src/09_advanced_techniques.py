"""
Advanced Prompt Engineering Techniques
=======================================
Additional sophisticated patterns for complex use cases.

1. Tree of Thoughts (ToT) - Explore multiple reasoning paths
2. Automatic Prompt Engineering (APE) - Let AI write prompts
3. Retrieval-Augmented Generation (RAG) - Add external knowledge
4. System 2 Thinking - Slow, deliberate reasoning
"""

from langchain_openai import ChatOpenAI

# Initialize LLM (LM Studio)
llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    temperature=0.5,
    openai_api_key="lm-studio",
    openai_api_base="http://127.0.0.1:1234/v1",
)

print("=" * 80)
print("ADVANCED TECHNIQUES")
print("=" * 80)

# Example 1: Tree of Thoughts (ToT)
print("\n--- Example 1: Tree of Thoughts ---")
print("Explore multiple solutions and evaluate each.")

tot_problem = """A farmer needs to transport a wolf, a goat, and a cabbage across a river.
The boat can only carry the farmer and one item at a time.
If left alone, the wolf will eat the goat, and the goat will eat the cabbage.
How can the farmer get everything across safely?"""

# Generate multiple solution attempts
print("\nGenerating 3 different solution approaches...\n")
solutions = []
for i in range(3):
    tot_prompt = f"""Solve this river crossing puzzle.
Show your step-by-step solution.

{tot_problem}

Solution {i+1}:"""
    solution = llm.invoke(tot_prompt)
    solutions.append(solution.content)
    print(f"Solution {i+1} preview: {solution.content[:150]}...\n")

# Evaluate solutions
print("Evaluating solutions...")
eval_prompt = f"""Evaluate these three solutions to the river crossing puzzle.
Identify which (if any) are correct and complete.

Solution 1: {solutions[0][:300]}

Solution 2: {solutions[1][:300]}

Solution 3: {solutions[2][:300]}

Which solution is correct? If none are fully correct, describe the correct solution."""

evaluation = llm.invoke(eval_prompt)
print(f"Evaluation:\n{evaluation.content}")

# Example 2: Automatic Prompt Engineering (APE)
print("\n--- Example 2: Automatic Prompt Engineering (APE) ---")
print("Using AI to optimize prompts.")

task_description = "Classify customer support tickets by urgency"

# Step 1: Generate candidate prompts
print("\nGenerating candidate prompts...")
ape_prompt = f"""Given this task: "{task_description}"

Generate 3 different prompts that could be used with an LLM.
Make them clear, specific, and effective.

Candidate 1:"""

candidates = llm.invoke(ape_prompt)
print(f"Candidate Prompts:\n{candidates.content}\n")

# Step 2: Score/evaluate prompts
print("Evaluating candidate prompts...")
score_prompt = f"""Score each of these prompts for clarity and effectiveness 
for the task "{task_description}".
Rate each 1-10 and explain why.

{candidates.content}

Scoring:"""

scoring = llm.invoke(score_prompt)
print(f"Scoring:\n{scoring.content}\n")

# Step 3: Select/improve best prompt
print("Improving the best prompt...")
improve_prompt = f"""Based on the scoring above, take the best prompt and 
refine it to be even more effective. Add any missing details.

Original prompts:
{candidates.content}

Refined best prompt:"""

refined = llm.invoke(improve_prompt)
print(f"Refined Prompt:\n{refined.content}")

# Example 3: System 2 Thinking (Deliberate Reasoning)
print("\n--- Example 3: System 2 Thinking ---")
print("Force slow, deliberate analysis instead of quick intuition.")

system2_problem = """A bat and a ball cost $11 in total.
The bat costs $10 more than the ball.
How much does the ball cost?"""

# Many people's quick intuition says $1, but that's wrong (should be $0.50)

system2_prompt = f"""Solve this carefully. Many people get this wrong on first instinct.

{system2_problem}

DO NOT rush. Verify your answer by substituting back.

Step-by-step solution with verification:"""

system2_response = llm.invoke(system2_prompt)
print(f"Problem: {system2_problem}")
print(f"\nSystem 2 Analysis:\n{system2_response.content}")

# Example 4: Directional Stimulus Prompting
print("\n--- Example 4: Directional Stimulus Prompting ---")
print("Guide the model with hints about what to focus on.")

text_to_summarize = """
Artificial intelligence has made significant strides in recent years. 
Machine learning models can now process natural language, recognize images, 
and even generate creative content. However, challenges remain in areas 
like reasoning, common sense understanding, and ensuring AI safety. 
Researchers are working on alignment problems to ensure AI systems 
benefit humanity.
"""

# Without stimulus
print("Without directional stimulus:")
plain_summary = llm.invoke(f"Summarize this text:\n{text_to_summarize}")
print(f"Summary: {plain_summary.content}\n")

# With directional stimulus (guide focus)
print("With directional stimulus (focus on challenges):")
stimulus_summary = llm.invoke(
    f"Summarize this text, focusing specifically on the challenges and problems mentioned:\n{text_to_summarize}"
)
print(f"Summary: {stimulus_summary.content}")

# Example 5: Generated Knowledge Prompting
print("\n--- Example 5: Generated Knowledge Prompting ---")
print("First generate relevant knowledge, then answer.")

question = "Why is the sky blue during the day but red at sunset?"

# Step 1: Generate relevant knowledge
print("\nStep 1: Generating relevant knowledge...")
knowledge_prompt = f"""Generate facts about light scattering in the atmosphere 
that would help answer: "{question}"

Relevant facts:"""

knowledge = llm.invoke(knowledge_prompt)
print(f"Generated Knowledge:\n{knowledge.content}\n")

# Step 2: Answer using the generated knowledge
print("Step 2: Answering using the knowledge...")
answer_prompt = f"""Based on these facts, answer the question.

Facts: {knowledge.content}

Question: {question}

Answer:"""

answer = llm.invoke(answer_prompt)
print(f"Answer:\n{answer.content}")

# Example 6: Style Transfer / Voice Matching
print("\n--- Example 6: Style Transfer ---")

sample_text = """
The quarterly figures demonstrate robust growth across all sectors. 
Our strategic initiatives have yielded measurable improvements in 
operational efficiency and customer satisfaction metrics.
"""

text_to_rewrite = "The app is really good. People like using it. We made $1M."

style_prompt = f"""Rewrite this text in the same professional style as the example.

Example style:
{sample_text}

Text to rewrite:
{text_to_rewrite}

Rewritten version:"""

styled = llm.invoke(style_prompt)
print(f"Original: {text_to_rewrite}")
print(f"Styled version: {styled.content}")

print("\n" + "=" * 80)
print("Key Takeaway: Advanced techniques combine multiple approaches")
print("to solve complex problems requiring exploration, evaluation, or optimization.")
print("=" * 80)
