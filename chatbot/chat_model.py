import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found.")

client = genai.Client(
    api_key=GOOGLE_API_KEY
)

SYSTEM_PROMPT = """
You are the official AI Customer Support Assistant for Foodie Restaurant.

Rules:

1. Answer ONLY from the provided restaurant knowledge.

2. If the answer is not found in the restaurant knowledge, say:

"I couldn't find that information in our restaurant knowledge base."

3. Never invent menu items.

4. Never invent prices.

5. Keep answers friendly and concise.

6. Recommend related menu items when appropriate.

7. Use previous conversation history to understand follow-up questions.
"""


def ask_gemini(question: str, context: str, history=None) -> str:

    conversation = ""

    if history:
        for message in history:
            role = message["role"].capitalize()
            conversation += f"{role}: {message['content']}\n"

    prompt = f"""
{SYSTEM_PROMPT}

Previous Conversation:

{conversation}

Restaurant Knowledge:

{context}

Customer Question:

{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text