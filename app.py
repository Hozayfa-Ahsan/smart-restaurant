"""
Restaurant website backend (Flask).

Endpoints:
    GET  /                -> serves the website (index.html)
    GET  /api/menu        -> returns the menu as JSON
    POST /api/order       -> accepts an order, saves it, returns confirmation
    GET  /api/orders      -> lists all saved orders (simple admin view)

Run:
    pip install flask
    python app.py
Then open http://127.0.0.1:5000 in your browser.
"""
import uuid
import json
import os

from datetime import datetime
from chatbot.rag_pipeline import RAGPipeline
from flask import Flask, jsonify, request, send_from_directory
import traceback
from chatbot.conversation_manager import (
    add_message,
    get_history
)

app = Flask(__name__, static_folder="static", static_url_path="/static")
rag = RAGPipeline()

# Where orders are stored (a simple JSON file acting as a tiny database).
ORDERS_FILE = os.path.join(os.path.dirname(__file__), "orders.json")

# The menu. In a real app this would live in a database.
MENU = [
    {"id": 1, "name": "Margherita Pizza", "price": 8.50,
     "category": "Pizza", "description": "Tomato, mozzarella & fresh basil.",
     "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400"},
    {"id": 2, "name": "Pepperoni Pizza", "price": 10.00,
     "category": "Pizza", "description": "Loaded with spicy pepperoni.",
     "image": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=400"},
    {"id": 3, "name": "Classic Burger", "price": 7.00,
     "category": "Burgers", "description": "Beef patty, cheese, lettuce & tomato.",
     "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400"},
    {"id": 4, "name": "Chicken Burger", "price": 6.50,
     "category": "Burgers", "description": "Crispy chicken with garlic mayo.",
     "image": "https://images.unsplash.com/photo-1615297928064-24977384d0da?w=400"},
    {"id": 5, "name": "Caesar Salad", "price": 5.50,
     "category": "Salads", "description": "Romaine, parmesan & croutons.",
     "image": "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=400"},
    {"id": 6, "name": "Pasta Alfredo", "price": 9.00,
     "category": "Pasta", "description": "Creamy alfredo with parmesan.",
     "image": "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=400"},
    {"id": 7, "name": "Fresh Lemonade", "price": 2.50,
     "category": "Drinks", "description": "Freshly squeezed, lightly sweet.",
     "image": "https://images.unsplash.com/photo-1621263764928-df1444c5e859?w=400"},
    {"id": 8, "name": "Chocolate Cake", "price": 4.00,
     "category": "Desserts", "description": "Rich moist chocolate slice.",
     "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400"},
]


def load_orders():
    """Read all saved orders from disk (returns an empty list if none)."""
    if not os.path.exists(ORDERS_FILE):
        return []
    try:
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_orders(orders):
    """Write the full list of orders back to disk."""
    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=2)


@app.route("/")
def index():
    """Serve the main website page."""
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/menu")
def get_menu():
    """Return the menu so the frontend can render it."""
    return jsonify(MENU)


@app.route("/api/order", methods=["POST"])
def place_order():
    """Validate and store an incoming order."""
    data = request.get_json(silent=True) or {}

    name = (data.get("name") or "").strip()
    phone = (data.get("phone") or "").strip()
    address = (data.get("address") or "").strip()
    items = data.get("items") or []

    # Basic validation.
    if not name or not phone or not address:
        return jsonify({"error": "Name, phone and address are required."}), 400
    if not items:
        return jsonify({"error": "Your cart is empty."}), 400

    # Recalculate the total on the server so it can't be faked by the client.
    menu_by_id = {m["id"]: m for m in MENU}
    total = 0.0
    clean_items = []
    for item in items:
        menu_item = menu_by_id.get(item.get("id"))
        qty = int(item.get("qty", 0))
        if not menu_item or qty <= 0:
            continue
        line_total = menu_item["price"] * qty
        total += line_total
        clean_items.append({
            "id": menu_item["id"],
            "name": menu_item["name"],
            "price": menu_item["price"],
            "qty": qty,
            "line_total": round(line_total, 2),
        })

    if not clean_items:
        return jsonify({"error": "No valid items in the order."}), 400

    orders = load_orders()
    order = {
        "order_id": len(orders) + 1,
        "name": name,
        "phone": phone,
        "address": address,
        "items": clean_items,
        "total": round(total, 2),
        "placed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    orders.append(order)
    save_orders(orders)

    return jsonify({
        "message": "Order placed successfully!",
        "order_id": order["order_id"],
        "total": order["total"],
    })


@app.route("/api/orders")
def list_orders():
    """Simple admin endpoint to view all placed orders."""
    return jsonify(load_orders())

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}

    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({
            "error": "Message is required."
        }), 400

    # Get session ID from frontend
    session_id = data.get("session_id")

    # Create a new one if this is a new visitor
    if not session_id:
        session_id = str(uuid.uuid4())

    # Load previous conversation
    history = get_history(session_id)

    try:

        # Ask the RAG system with conversation history
        result = rag.ask(
            message,
            history=history
        )

        # Save the user's message
        add_message(
            session_id,
            "user",
            message
        )

        # Save the AI response
        add_message(
            session_id,
            "assistant",
            result["answer"]
        )

        return jsonify({
            "answer": result["answer"],
            "session_id": session_id
        })

    except Exception as e:

        print("\n========== CHAT ERROR ==========")
        traceback.print_exc()
        print("================================\n")

        return jsonify({
            "error": str(e)
        }), 500




if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False)