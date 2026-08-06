from chatbot.retriever import Retriever

retriever = Retriever()

question = "What payment methods are accepted?"


results = retriever.search(question)

print("=" * 60)
print("Retrieved Chunks")
print("=" * 60)

print(f"Retrieved {len(results)} chunks\n")

for i, result in enumerate(results, start=1):

    print("=" * 60)
    print(f"Result {i}")
    print("=" * 60)

    print("Similarity Score:", round(result["score"], 4))
    print()

    print(result["text"][:700])

    print("\n")