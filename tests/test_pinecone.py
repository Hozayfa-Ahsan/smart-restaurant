from chatbot.vector_store import VectorStore

store = VectorStore()

index = store.get_index()

stats = index.describe_index_stats()

print("=" * 60)
print("Pinecone Connected Successfully")
print("=" * 60)

print("\nIndex Statistics:\n")

print(stats)