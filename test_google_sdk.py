import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("Key starts with:", api_key[:8] if api_key else "None")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Reply with only the word: SUCCESS"
)

print(response.text)