"""
Few-Shot Prompting
==================
Providing examples in the prompt to guide the model's response format
and reasoning pattern. This helps the model understand the expected output.
"""

import sys
from pathlib import Path

# Add project root to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils.llm_client import get_completion

print("=" * 80)
print("FEW-SHOT PROMPTING EXAMPLES (NVIDIA API)")
print("=" * 80)

# Example 1: Sentiment with examples
print("\n--- Example 1: Sentiment Classification with Examples ---")
prompt1 = """Classify the sentiment of each text as Positive, Negative, or Neutral.

Text: "The service was terrible and slow."
Sentiment: Negative

Text: "I had an amazing time at the concert!"
Sentiment: Positive

Text: "The package arrived on Tuesday."
Sentiment: Neutral

Text: "The food was okay, nothing special."
Sentiment:"""
response1 = get_completion(prompt1)
print(f"Prompt:\n{prompt1}")
print(f"Response: {response1}")

# Example 2: Named Entity Recognition
print("\n--- Example 2: Named Entity Recognition ---")
prompt2 = """Extract entities and their types from the text.

Text: "Apple CEO Tim Cook announced new products in Cupertino."
Entities: Apple (Organization), Tim Cook (Person), Cupertino (Location)

Text: "Barack Obama was born in Hawaii and served as US President."
Entities: Barack Obama (Person), Hawaii (Location), US (Organization)

Text: "Tesla is building a factory in Berlin, said Elon Musk."
Entities:"""
response2 = get_completion(prompt2)
print(f"Prompt:\n{prompt2}")
print(f"Response: {response2}")

# Example 3: Text transformation (translation style)
print("\n--- Example 3: Casual to Formal Conversion ---")
prompt3 = """Convert casual text to formal business language.

Casual: "Hey, can you send me that report ASAP?"
Formal: "Dear colleague, could you please send me the report at your earliest convenience?"

Casual: "Thanks for the help yesterday!"
Formal: "I appreciate your assistance yesterday."

Casual: "Gotta run, catch you later!"
Formal:"""
response3 = get_completion(prompt3)
print(f"Prompt:\n{prompt3}")
print(f"Response: {response3}")

# Example 4: Pattern Recognition
print("\n--- Example 4: Pattern Recognition ---")
prompt4 = """Given a word, provide a word that rhymes with it.

Word: cat
Rhyme: bat

Word: phone
Rhyme: bone

Word: light
Rhyme: night

Word: green
Rhyme:"""
response4 = get_completion(prompt4)
print(f"Prompt:\n{prompt4}")
print(f"Response: {response4}")

# Example 5: Structured Data Extraction
print("\n--- Example 5: Structured Data Extraction ---")
prompt5 = """Extract contact information in the format: Name | Email | Phone

Text: "Contact John Doe at john.doe@email.com or call 555-1234"
Result: John Doe | john.doe@email.com | 555-1234

Text: "Reach out to Jane Smith (jane.smith@company.org), mobile: 555-5678"
Result: Jane Smith | jane.smith@company.org | 555-5678

Text: "Mike Johnson - mike.j@example.com - office: 555-9999"
Result:"""
response5 = get_completion(prompt5)
print(f"Prompt:\n{prompt5}")
print(f"Response: {response5}")

print("\n" + "=" * 80)
print("Key Takeaway: Few-shot prompting guides the model by showing patterns.")
print("It's especially effective when you need consistent formatting.")
print("=" * 80)
