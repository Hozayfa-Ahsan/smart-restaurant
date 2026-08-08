# Smart Restaurant AI Chatbot Widget

A reusable, embeddable AI chatbot widget powered by a Flask API, RAG, Pinecone, and Google Gemini.

The widget can be embedded into a website using a single `<script>` tag.

---

## Live Demo

**Restaurant Website:**

https://smart-restaurant-qzvz.onrender.com

**Embeddable Widget:**

https://hozayfa-ahsan.github.io/smart-restaurant/widget/widget.js

---

## Quick Installation

Add the following code before the closing `</body>` tag of any website:

```html
<script
    src="https://hozayfa-ahsan.github.io/smart-restaurant/widget/widget.js"
    data-api-url="https://smart-restaurant-qzvz.onrender.com"
    data-client-id="foodie"
    data-title="Foodie Assistant">
</script>