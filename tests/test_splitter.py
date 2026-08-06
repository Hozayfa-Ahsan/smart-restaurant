from chatbot.knowledge_builder import build_knowledge_base
from chatbot.text_splitter import split_text

knowledge = build_knowledge_base(
    "data/instruction.docx",
    "data/menu.json"
)

chunks = split_text(knowledge)

print("=" * 60)
print("Chunking Successful")
print("=" * 60)

print(f"Total Chunks: {len(chunks)}")

print("\n")

for i, chunk in enumerate(chunks[:3], start=1):
    print("=" * 60)
    print(f"Chunk {i}")
    print("=" * 60)
    print(chunk[:500])
    print("\n")