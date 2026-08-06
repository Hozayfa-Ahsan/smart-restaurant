import os
from dotenv import load_dotenv

load_dotenv()

print("Environment file loaded successfully.")

print("GOOGLE_API_KEY exists:", bool(os.getenv("GOOGLE_API_KEY")))
print("PINECONE_API_KEY exists:", bool(os.getenv("PINECONE_API_KEY")))
print("PINECONE_INDEX_NAME:", os.getenv("PINECONE_INDEX_NAME"))