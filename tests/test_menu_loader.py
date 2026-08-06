import json

file_path = "data/menu.json"

with open(file_path, "r", encoding="utf-8") as file:
    menu_data = json.load(file)

print("Menu JSON loaded successfully.")
print("Data type:", type(menu_data).__name__)

if isinstance(menu_data, list):
    print("Number of menu items:", len(menu_data))

    print("\nFirst menu item:")
    print(menu_data[0])

elif isinstance(menu_data, dict):
    print("Top-level keys:")
    print(list(menu_data.keys()))

    print("\nMenu data:")
    print(menu_data)