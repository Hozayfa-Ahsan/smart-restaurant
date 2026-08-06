from chatbot.document_loader import (
    load_instruction,
    load_menu,
    menu_to_text
)


def build_knowledge_base(
    instruction_path: str,
    menu_path: str
) -> str:
    """
    Combine every knowledge source into one text.
    """

    instruction = load_instruction(instruction_path)

    menu = load_menu(menu_path)

    menu_text = menu_to_text(menu)

    knowledge = f"""
=============================
RESTAURANT SYSTEM INSTRUCTION
=============================

{instruction}


=============================
RESTAURANT MENU
=============================

{menu_text}
"""

    return knowledge.strip()