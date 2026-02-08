"""
Prompt Chaining
===============
Breaking complex tasks into a sequence of simpler prompts where
the output of one becomes the input of the next.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "nvapi-dummy"))
)

def get_completion(prompt, temperature=0.3):
    """Helper to get completion from NVIDIA API"""
    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL_ID", "meta/llama-3.1-405b-instruct"),
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content


print("=" * 80)
print("PROMPT CHAINING EXAMPLES (NVIDIA API)")
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

facts = get_completion(extraction_prompt)
print(f"Extracted facts:\n{facts}\n")

# Step 2: Analyze sentiment and tone
print("Step 2: Analyzing sentiment...")
sentiment_prompt = f"""Analyze the sentiment and overall tone of these facts:

{facts}

Provide sentiment (Positive/Negative/Neutral) and brief reasoning."""

sentiment = get_completion(sentiment_prompt)
print(f"Sentiment analysis:\n{sentiment}\n")

# Step 3: Generate executive summary
print("Step 3: Generating executive summary...")
summary_prompt = f"""Based on these facts and sentiment, write a 2-sentence 
executive summary for stakeholders.

Facts:
{facts}

Sentiment: {sentiment}

Executive Summary:"""

summary = get_completion(summary_prompt)
print(f"Executive Summary:\n{summary}")

# Example 2: Code Generation Pipeline
print("\n--- Example 2: Code Generation Pipeline ---")

user_request = "Create a function that filters products by price range and category"

# Step 1: Generate requirements
print("Step 1: Generating requirements...")
requirements_prompt = f"""Given this request, list the key requirements:
"{user_request}"

Requirements:"""

requirements = get_completion(requirements_prompt)
print(f"Requirements:\n{requirements}\n")

# Step 2: Design the function signature
print("Step 2: Designing function signature...")
signature_prompt = f"""Based on these requirements, design the function signature 
and parameters in Python.

Requirements:
{requirements}

Function Signature:"""

signature = get_completion(signature_prompt)
print(f"Function Signature:\n{signature}\n")

# Step 3: Generate implementation
print("Step 3: Generating implementation...")
implementation_prompt = f"""Implement this function according to the requirements.
Include docstring and error handling.

Requirements:
{requirements}

Signature:
{signature}

Implementation:
```python"""

implementation = get_completion(implementation_prompt)
print(f"Implementation:\n```python\n{implementation}")

# Example 3: Question Answering with Verification
print("\n--- Example 3: Question Answering with Verification ---")

question = "What are the benefits and drawbacks of using microservices?"

# Step 1: Generate initial answer
print("Step 1: Generating initial answer...")
draft_prompt = f"""Answer this question concisely:
{question}

Draft Answer:"""

draft = get_completion(draft_prompt)
print(f"Draft Answer:\n{draft}\n")

# Step 2: Fact-check the answer
print("Step 2: Fact-checking...")
factcheck_prompt = f"""Review this answer for accuracy and completeness:

Question: {question}
Draft Answer: {draft}

Identify any missing points or inaccuracies:
"""

factcheck = get_completion(factcheck_prompt)
print(f"Fact Check:\n{factcheck}\n")

# Step 3: Refine based on feedback
print("Step 3: Refining answer...")
refine_prompt = f"""Improve this answer based on the feedback:

Draft: {draft}

Feedback: {factcheck}

Refined Answer:"""

refined = get_completion(refine_prompt)
print(f"Refined Answer:\n{refined}")

# Example 4: Multi-step Content Creation
print("\n--- Example 4: Multi-step Content Creation ---")

topic = "Introduction to Machine Learning"

# Step 1: Create outline
print("Step 1: Creating outline...")
outline_prompt = f"""Create a 3-point outline for an article about:
"{topic}"

Outline:"""

outline = get_completion(outline_prompt)
print(f"Outline:\n{outline}\n")

# Step 2: Write introduction based on outline
print("Step 2: Writing introduction...")
intro_prompt = f"""Write an engaging introduction (2-3 sentences) for an article 
with this outline:

{outline}

Introduction:"""

introduction = get_completion(intro_prompt)
print(f"Introduction:\n{introduction}\n")

# Step 3: Write body content
print("Step 3: Writing body content...")
body_prompt = f"""Expand each point in this outline into 1-2 sentences:

{outline}

Body Content:"""

body = get_completion(body_prompt)
print(f"Body Content:\n{body}\n")

# Step 4: Write conclusion
print("Step 4: Writing conclusion...")
conclusion_prompt = f"""Write a conclusion that summarizes these key points:

{body}

Conclusion:"""

conclusion = get_completion(conclusion_prompt)
print(f"Conclusion:\n{conclusion}")

# Example 5: Conditional Branching Chain
print("\n--- Example 5: Conditional Classification Chain ---")

customer_feedback = (
    "The app crashes every time I try to upload a photo. Very frustrating!"
)

# Step 1: Classify the feedback
print("Step 1: Classifying feedback...")
classify_prompt = f"""Classify this customer feedback into one category:
BUG, FEATURE_REQUEST, or GENERAL_FEEDBACK

Feedback: "{customer_feedback}"

Category:"""

category = get_completion(classify_prompt)
print(f"Category: {category.strip()}\n")

# Step 2: Route to appropriate handler based on classification
category_clean = category.strip().upper()

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

handler_result = get_completion(handler_prompt)
print(f"Handler Output:\n{handler_result}")

print("\n" + "=" * 80)
print("Key Takeaway: Prompt chaining breaks complexity into manageable steps,")
print("enables validation at each stage, and creates reusable components.")
print("=" * 80)
