import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY not found in .env")

if not INDEX_NAME:
    raise ValueError("PINECONE_INDEX_NAME not found in .env")


class VectorStore:

    def __init__(self):

        self.pc = Pinecone(
            api_key=PINECONE_API_KEY
        )

        existing_indexes = self.pc.list_indexes().names()


        if INDEX_NAME not in existing_indexes:

            print(f"Creating Pinecone index: {INDEX_NAME}")

            self.pc.create_index(
                name=INDEX_NAME,
                dimension=3072,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )

            print("Index created successfully.")

        self.index = self.pc.Index(INDEX_NAME)

    def get_index(self):
        return self.index