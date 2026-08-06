from docx import Document
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

instruction_path = os.path.join(
    DATA_DIR,
    "instruction.docx"
)

menu_path = os.path.join(
    DATA_DIR,
    "menu.json"
)


def load_instruction(docx_path: str) -> str:
    """
    Load instruction.docx
    """

    document = Document(docx_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)


def load_menu(json_path: str) -> dict:
    """
    Load menu.json
    """

    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)


def menu_to_text(menu: dict) -> str:
    """
    Convert menu.json into natural language.
    """

    lines = []

    restaurant = menu["restaurant"]

    lines.append(f"Restaurant Name: {restaurant['name']}")
    lines.append(f"Currency: {restaurant['currency']}")
    lines.append("")

    lines.append("MENU")

    for item in menu["items"]:

        lines.append("=" * 50)

        lines.append(f"Name: {item['name']}")
        lines.append(f"Category: {item['category']}")
        lines.append(f"Price: {item['price']}")
        lines.append(f"Description: {item['description']}")
        lines.append(f"Preparation Time: {item['preparation_time']}")

        lines.append(
            "Ingredients: " +
            ", ".join(item["ingredients"])
        )

        lines.append(
            "Allergens: " +
            ", ".join(item["allergens"])
        )

        lines.append(
            f"Spicy Level: {item['spicy_level']}"
        )

        lines.append(
            f"Vegetarian: {item['vegetarian']}"
        )

        lines.append(
            f"Vegan: {item['vegan']}"
        )

        lines.append(
            f"Halal: {item['halal']}"
        )

        lines.append("")

    return "\n".join(lines)