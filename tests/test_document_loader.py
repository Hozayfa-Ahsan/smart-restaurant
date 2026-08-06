from docx import Document

file_path = "data/instruction.docx"

document = Document(file_path)

all_text = []

for paragraph in document.paragraphs:
    text = paragraph.text.strip()

    if text:
        all_text.append(text)

print("Document loaded successfully.")
print("Total non-empty paragraphs:", len(all_text))

print("\nFirst 10 extracted paragraphs:\n")

for number, text in enumerate(all_text[:10], start=1):
    print(f"{number}. {text}")