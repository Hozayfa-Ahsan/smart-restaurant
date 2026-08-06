from chatbot.rag_pipeline import RAGPipeline

rag = RAGPipeline()

question = "How much is the Beef Burger?"

result = rag.ask(question)

print("=" * 60)
print("QUESTION")
print("=" * 60)

print(question)

print()

print("=" * 60)
print("ANSWER")
print("=" * 60)

print(result["answer"])

print()

print("=" * 60)
print("SOURCE CHUNKS")
print("=" * 60)

for i, source in enumerate(result["sources"], start=1):

    print(f"\nSource {i}")
    print("Score:", round(source["score"], 4))
    print(source["text"][:300])