from chatbot.document_loader import load_menu
from chatbot.document_loader import menu_to_text


menu = load_menu("data/menu.json")

text = menu_to_text(menu)

print(text[:2500])

print("\n")

print("=" * 60)

print("Total Characters")

print(len(text))