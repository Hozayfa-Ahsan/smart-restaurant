from chatbot.knowledge_builder import build_knowledge_base

knowledge = build_knowledge_base(
    "data/instruction.docx",
    "data/menu.json"
)

print("=" * 70)
print("Knowledge Base Created Successfully")
print("=" * 70)

print()

print("First 2000 characters:\n")

print(knowledge[:2000])

print()

print("=" * 70)

print("Statistics")

print("=" * 70)

print("Characters :", len(knowledge))
print("Words      :", len(knowledge.split()))