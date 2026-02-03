"""
Structured Output / JSON Mode
=============================
Guiding the model to produce output in a specific format (JSON, XML, YAML, etc.)
This is crucial for integrating LLMs with applications and APIs.

When to use:
- API responses that need parsing
- Database insertion
- Structured data extraction
- Multi-field responses

Techniques:
1. Explicit formatting instructions
2. Few-shot with format examples
3. JSON schema specification
4. Using LangChain's output parsers
"""

import json
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

# Initialize LLM (LM Studio)
llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    temperature=0.1,
    openai_api_key="lm-studio",
    openai_api_base="http://127.0.0.1:1234/v1",
)

print("=" * 80)
print("STRUCTURED OUTPUT EXAMPLES")
print("=" * 80)

# Example 1: Simple JSON with explicit instructions
print("\n--- Example 1: Explicit JSON Format ---")
prompt1 = """Extract the following information from the text and output as JSON:
- name (string)
- age (integer)
- city (string)
- hobbies (array of strings)

Text: "Sarah Johnson is 28 years old and lives in Seattle. 
She enjoys hiking, photography, and playing guitar."

Output ONLY valid JSON with no additional text:
{"""
response1 = llm.invoke(prompt1)
print(f"Prompt:\n{prompt1}")
print(f"Response:\n{{{response1.content}")
try:
    parsed = json.loads("{" + response1.content)
    print(f"\nParsed JSON: {json.dumps(parsed, indent=2)}")
except:
    print("(Note: Parsing may need cleanup)")

# Example 2: Few-shot JSON examples
print("\n--- Example 2: Few-shot JSON Examples ---")
prompt2 = """Extract product information from text. Output as JSON.

Example 1:
Text: "iPhone 15 Pro costs $999 and is in stock"
Output: {"product": "iPhone 15 Pro", "price": 999, "currency": "USD", "in_stock": true}

Example 2:
Text: "Samsung Galaxy S24 priced at €899, currently out of stock"
Output: {"product": "Samsung Galaxy S24", "price": 899, "currency": "EUR", "in_stock": false}

Now extract:
Text: "MacBook Pro M3 starts at $1999 and available now"
Output:"""
response2 = llm.invoke(prompt2)
print(f"Prompt:\n{prompt2}")
print(f"Response:\n{response2.content}")

# Example 3: Using Pydantic schema with LangChain
print("\n--- Example 3: Pydantic Schema with LangChain ---")

class MovieReview(BaseModel):
    movie_title: str = Field(description="The title of the movie")
    rating: int = Field(description="Rating from 1-10")
    pros: list = Field(description="List of positive aspects")
    cons: list = Field(description="List of negative aspects")
    summary: str = Field(description="Brief summary of the review")

parser = JsonOutputParser(pydantic_object=MovieReview)

prompt3 = f"""Analyze this movie review and extract structured information.

Review: "Dune: Part Two is an absolute masterpiece. The visuals are stunning,
the soundtrack by Hans Zimmer is breathtaking, and the performances by 
Timothee Chalamet and Zendaya are incredible. However, the pacing in the 
middle act feels a bit slow, and some plot points from the book were cut. 
Overall, this is a must-watch for sci-fi fans. Rating: 9/10"

{parser.get_format_instructions()}"""

response3 = llm.invoke(prompt3)
print(f"Prompt:\n{prompt3}")
print(f"\nResponse:\n{response3.content}")
try:
    parsed = parser.parse(response3.content)
    print(f"\nParsed Output: {json.dumps(parsed, indent=2)}")
except Exception as e:
    print(f"Parsing note: {e}")

# Example 4: Multi-item extraction
print("\n--- Example 4: List of Objects ---")
prompt4 = """Extract all people mentioned and their details.
Output as a JSON array of objects.

Text: "The team consists of Alice (Engineer, 5 years experience), 
Bob (Designer, 3 years), and Carol (Manager, 10 years). 
They all work at TechCorp in San Francisco."

Output format:
[
  {"name": "...", "role": "...", "experience_years": ...},
  ...
]

Output:"""
response4 = llm.invoke(prompt4)
print(f"Prompt:\n{prompt4}")
print(f"Response:\n{response4.content}")

# Example 5: Classification with confidence scores
print("\n--- Example 5: Classification with Confidence ---")
prompt5 = """Classify the sentiment of these texts with confidence scores.
Output as JSON array.

Texts:
1. "This product exceeded my expectations!"
2. "It's okay, not great but not terrible"
3. "Worst purchase I've ever made"

Output format:
[
  {"text_id": 1, "sentiment": "positive/negative/neutral", "confidence": 0.95},
  ...
]

Output:"""
response5 = llm.invoke(prompt5)
print(f"Prompt:\n{prompt5}")
print(f"Response:\n{response5.content}")

# Example 6: Hierarchical JSON structure
print("\n--- Example 6: Hierarchical Structure ---")
prompt6 = """Extract meeting information as structured JSON.

Meeting notes: "Project Alpha Weekly Sync - March 15, 2024.
Attendees: John (PM), Sarah (Dev), Mike (Dev).
Action items: John will send requirements by Friday. 
Sarah and Mike will review the API documentation.
Next meeting: March 22, 2024."

Output format:
{
  "meeting_title": "...",
  "date": "...",
  "attendees": [{"name": "...", "role": "..."}],
  "action_items": [{"assignee": "...", "task": "...", "due": "..."}],
  "next_meeting": "..."
}

Output:"""
response6 = llm.invoke(prompt6)
print(f"Prompt:\n{prompt6}")
print(f"Response:\n{response6.content}")

# Example 7: XML format (alternative to JSON)
print("\n--- Example 7: XML Output Format ---")
prompt7 = """Extract book information and output as XML.

Text: "The Great Gatsby by F. Scott Fitzgerald, published in 1925. 
Genre: Classic Fiction. 180 pages."

Output format:
<book>
  <title>...</title>
  <author>...</author>
  <year>...</year>
  <genre>...</genre>
  <pages>...</pages>
</book>

Output:"""
response7 = llm.invoke(prompt7)
print(f"Prompt:\n{prompt7}")
print(f"Response:\n{response7.content}")

print("\n" + "=" * 80)
print("Key Takeaway: Structured output is essential for production systems.")
print("Use clear examples, schemas, and parsers to ensure reliability.")
print("=" * 80)
