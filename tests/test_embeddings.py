from chatbot.embeddings import embed_text

sample_text = """
Foodie delivers food within 30 to 45 minutes.
"""

vector = embed_text(sample_text)

print("Embedding created successfully.\n")

print("Vector Dimension :", len(vector))

print("\nFirst 10 Values:")

for value in vector[:10]:
    print(value)