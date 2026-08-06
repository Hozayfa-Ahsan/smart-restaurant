from chatbot.document_loader import load_instruction, load_menu

instruction = load_instruction("data/instruction.docx")
menu = load_menu("data/menu.json")

print("=" * 60)
print("Instruction Loaded Successfully")
print("=" * 60)

print(instruction[:500])

print("\n")

print("=" * 60)
print("Menu Loaded Successfully")
print("=" * 60)

print("Restaurant:", menu["restaurant"]["name"])
print("Currency :", menu["restaurant"]["currency"])

print("\nCategories:")

for category in menu["categories"]:
    print("-", category["name"])

print("\nFirst Menu Item:")

first_item = menu["items"][0]

print(first_item["name"])
print(first_item["price"])
print(first_item["description"])