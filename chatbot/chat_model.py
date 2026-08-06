import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found.")


chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2,
)


SYSTEM_PROMPT = """
You are the official AI Customer Support Assistant for Foodie Restaurant.

Rules:

1. Answer ONLY from the provided restaurant knowledge.

2. If the answer is not found inside the restaurant knowledge, say:

"I couldn't find that information in our restaurant knowledge base."

3. Never invent menu items.

4. Never invent prices.

5. Keep answers friendly and concise.

6. If appropriate, recommend related menu items.

7. Use the previous conversation to understand follow-up questions such as:
   - "that one"
   - "the second one"
   - "how much does it cost?"
   - "is it halal?"
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

    response = chat_model.invoke(prompt)

    return response.content