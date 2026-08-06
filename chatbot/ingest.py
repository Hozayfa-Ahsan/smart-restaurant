import uuid

from chatbot.knowledge_builder import build_knowledge_base
from chatbot.text_splitter import split_text
from chatbot.embeddings import embed_text
from chatbot.vector_store import VectorStore


def ingest_documents():

    print("=" * 60)
    print("Building Knowledge Base...")
    print("=" * 60)

    knowledge = build_knowledge_base(
        "data/instruction.docx",
        "data/menu.json"
    )

    print("Knowledge Base Created.")
    print()

    print("=" * 60)
    print("Splitting Text...")
    print("=" * 60)

    chunks = split_text(knowledge)

    print(f"Total Chunks : {len(chunks)}")
    print()

    store = VectorStore()
    index = store.get_index()

    vectors = []

    print("=" * 60)
    print("Generating Embeddings...")
    print("=" * 60)

    for i, chunk in enumerate(chunks):

        embedding = embed_text(chunk)

        vectors.append(
            {
                "id": str(uuid.uuid4()),
                "values": embedding,
                "metadata": {
                    "text": chunk
                }
            }
        )

        print(f"Embedding {i+1}/{len(chunks)} created.")

    print()

    print("=" * 60)
    print("Uploading to Pinecone...")
    print("=" * 60)

    index.upsert(vectors=vectors)

    print(f"Uploaded {len(vectors)} vectors successfully.")