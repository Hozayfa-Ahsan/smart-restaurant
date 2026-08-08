# Foodie AI Chatbot Widget

The Foodie AI Chatbot Widget is a reusable JavaScript chatbot that can be embedded into an existing website.

A client does not need to copy the entire Foodie restaurant website. They can add the widget to their website and connect it to the deployed Foodie AI backend.

---

## 🚀 How It Works

```text
Client Website
      │
      │ chatbot widget
      ▼
  widget.js
      │
      │ HTTP POST
      ▼
Foodie AI Backend
      │
      ├── RAG Pipeline
      ├── Pinecone
      └── Google Gemini
      │
      ▼
   AI Response
      │
      ▼
Client Website