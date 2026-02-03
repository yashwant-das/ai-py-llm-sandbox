"""
Prompt Chaining
===============
Breaking complex tasks into a sequence of simpler prompts where
the output of one becomes the input of the next.

When to use:
- Complex multi-step tasks
- When intermediate outputs are useful
- Error handling at each step
- Building reusable prompt components

Benefits:
- Easier to debug (see intermediate results)
- Can validate/modify at each step
- Reusable sub-prompts
- Better error isolation

Topic: 06_advanced_prompting
Refer to: ../README.md for more information
"""

import sys
from pathlib import Path

# Add project root to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from shared import get_lmstudio_llm

# Initialize LLM
llm = get_lmstudio_llm(temperature=0.3)

print("=" * 80)
print("PROMPT CHAINING EXAMPLES")
print("=" * 80)

# Example 1: Document Processing Pipeline
print("\n--- Example 1: Document Processing Pipeline ---")

raw_text = """
ACME Corporation Quarterly Report Q3 2024

Revenue increased by 15% compared to Q2, reaching $2.5M.
Expenses were managed well, staying under the $1.8M budget.
The new product line launched in July contributed significantly.
Customer satisfaction scores improved from 7.2 to 8.1.
We hired 12 new employees across engineering and sales.
"""

# Step 1: Extract key facts
print("Step 1: Extracting key facts...")
extraction_prompt = f"""Extract key metrics and facts from this report as bullet points.

Report:
{raw_text}

Key Facts:"""

facts = llm.invoke(extraction_prompt)
print(f"Extracted facts:\n{facts.content}\n")

# Step 2: Analyze sentiment and tone
print("Step 2: Analyzing sentiment...")
sentiment_prompt = f"""Analyze the sentiment and overall tone of these facts:

{facts.content}

Provide sentiment (Positive/Negative/Neutral) and brief reasoning."""

sentiment = llm.invoke(sentiment_prompt)
print(f"Sentiment analysis:\n{sentiment.content}\n")

# Step 3: Generate executive summary
print("Step 3: Generating executive summary...")
summary_prompt = f"""Based on these facts and sentiment, write a 2-sentence 
executive summary for stakeholders.

Facts:
{facts.content}

Sentiment: {sentiment.content}

Executive Summary:"""

summary = llm.invoke(summary_prompt)
print(f"Executive Summary:\n{summary.content}")

# Example 2: Code Generation Pipeline
print("\n--- Example 2: Code Generation Pipeline ---")

user_request = "Create a function that filters products by price range and category"

# Step 1: Generate requirements
print("Step 1: Generating requirements...")
requirements_prompt = f"""Given this request, list the key requirements:
"{user_request}"

Requirements:"""

requirements = llm.invoke(requirements_prompt)
print(f"Requirements:\n{requirements.content}\n")

# Step 2: Design the function signature
print("Step 2: Designing function signature...")
signature_prompt = f"""Based on these requirements, design the function signature 
and parameters in Python.

Requirements:
{requirements.content}

Function Signature:"""

signature = llm.invoke(signature_prompt)
print(f"Function Signature:\n{signature.content}\n")

# Step 3: Generate implementation
print("Step 3: Generating implementation...")
implementation_prompt = f"""Implement this function according to the requirements.
Include docstring and error handling.

Requirements:
{requirements.content}

Signature:
{signature.content}

Implementation:
```python"""

implementation = llm.invoke(implementation_prompt)
print(f"Implementation:\n```python\n{implementation.content}")

# Example 3: Question Answering with Verification
print("\n--- Example 3: Question Answering with Verification ---")

question = "What are the benefits and drawbacks of using microservices?"

# Step 1: Generate initial answer
print("Step 1: Generating initial answer...")
draft_prompt = f"""Answer this question concisely:
{question}

Draft Answer:"""

draft = llm.invoke(draft_prompt)
print(f"Draft Answer:\n{draft.content}\n")

# Step 2: Fact-check the answer
print("Step 2: Fact-checking...")
factcheck_prompt = f"""Review this answer for accuracy and completeness:

Question: {question}
Draft Answer: {draft.content}

Identify any missing points or inaccuracies:
"""

factcheck = llm.invoke(factcheck_prompt)
print(f"Fact Check:\n{factcheck.content}\n")

# Step 3: Refine based on feedback
print("Step 3: Refining answer...")
refine_prompt = f"""Improve this answer based on the feedback:

Draft: {draft.content}

Feedback: {factcheck.content}

Refined Answer:"""

refined = llm.invoke(refine_prompt)
print(f"Refined Answer:\n{refined.content}")

# Example 4: Multi-step Content Creation
print("\n--- Example 4: Multi-step Content Creation ---")

topic = "Introduction to Machine Learning"

# Step 1: Create outline
print("Step 1: Creating outline...")
outline_prompt = f"""Create a 3-point outline for an article about:
"{topic}"

Outline:"""

outline = llm.invoke(outline_prompt)
print(f"Outline:\n{outline.content}\n")

# Step 2: Write introduction based on outline
print("Step 2: Writing introduction...")
intro_prompt = f"""Write an engaging introduction (2-3 sentences) for an article 
with this outline:

{outline.content}

Introduction:"""

introduction = llm.invoke(intro_prompt)
print(f"Introduction:\n{introduction.content}\n")

# Step 3: Write body content
print("Step 3: Writing body content...")
body_prompt = f"""Expand each point in this outline into 1-2 sentences:

{outline.content}

Body Content:"""

body = llm.invoke(body_prompt)
print(f"Body Content:\n{body.content}\n")

# Step 4: Write conclusion
print("Step 4: Writing conclusion...")
conclusion_prompt = f"""Write a conclusion that summarizes these key points:

{body.content}

Conclusion:"""

conclusion = llm.invoke(conclusion_prompt)
print(f"Conclusion:\n{conclusion.content}")

# Example 5: Conditional Branching Chain
print("\n--- Example 5: Conditional Classification Chain ---")

customer_feedback = "The app crashes every time I try to upload a photo. Very frustrating!"

# Step 1: Classify the feedback
print("Step 1: Classifying feedback...")
classify_prompt = f"""Classify this customer feedback into one category:
BUG, FEATURE_REQUEST, or GENERAL_FEEDBACK

Feedback: "{customer_feedback}"

Category:"""

category = llm.invoke(classify_prompt)
print(f"Category: {category.content.strip()}\n")

# Step 2: Route to appropriate handler based on classification
category_clean = category.content.strip().upper()

if "BUG" in category_clean:
    print("Step 2: Bug Report - Generating technical ticket...")
    handler_prompt = f"""Create a bug report ticket from this feedback:
    
Feedback: {customer_feedback}

Format:
- Priority: (High/Medium/Low)
- Component: 
- Steps to reproduce:
- Expected behavior:
- Actual behavior:"""

elif "FEATURE" in category_clean:
    print("Step 2: Feature Request - Analyzing feasibility...")
    handler_prompt = f"""Analyze this feature request:
    
Feedback: {customer_feedback}

Provide:
- Feasibility assessment
- Implementation complexity
- User impact
- Recommendation:"""

else:
    print("Step 2: General Feedback - Generating response...")
    handler_prompt = f"""Draft a thank-you response to this feedback:
    
Feedback: {customer_feedback}

Response:"""

handler_result = llm.invoke(handler_prompt)
print(f"Handler Output:\n{handler_result.content}")

print("\n" + "=" * 80)
print("Key Takeaway: Prompt chaining breaks complexity into manageable steps,")
print("enables validation at each stage, and creates reusable components.")
print("=" * 80)
