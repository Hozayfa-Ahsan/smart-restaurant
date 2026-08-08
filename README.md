# 🍽️ Foodie AI Restaurant Chatbot

> An intelligent restaurant website powered by Retrieval-Augmented Generation (RAG), Google Gemini, Pinecone Vector Database, Flask, and Docker.


[![🚀 Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Visit_Website-success?style=for-the-badge)](https://smart-restaurant-qzvz.onrender.com/)

### 🌐 Restaurant Website

👉 **[Open Foodie Restaurant — Live Demo](https://smart-restaurant-qzvz.onrender.com/)**

The complete restaurant website, ordering system, and AI chatbot are deployed online.

### 🤖 Embeddable AI Chatbot

The chatbot can also be embedded into another website using a single `<script>` tag.

👉 **[View Widget JavaScript](https://hozayfa-ahsan.github.io/smart-restaurant/widget/widget.js)**

---

## 📖 Project Overview

Foodie AI Restaurant Chatbot is a complete restaurant web application that allows visitors to:

- 🍔 Browse restaurant menu items
- 🛒 Add food items and place orders
- 🤖 Chat with an AI customer-support assistant
- 💬 Ask questions about restaurant offerings
- 📚 Receive answers based on the restaurant knowledge base
- 🔄 Maintain conversation history

---

The chatbot uses **Retrieval-Augmented Generation (RAG)** instead of relying only on the language model.

When a customer asks a question:

```text
Customer Question
       ↓
Query Embedding
       ↓
Pinecone Vector Search
       ↓
Relevant Restaurant Knowledge
       ↓
Google Gemini
       ↓
AI Response

---

✨ Key Features
🍔 Restaurant Website
Responsive restaurant interface
Menu browsing
Food categories
Shopping cart
Order placement
Server-side order validation
🤖 AI Chatbot
RAG-based question answering
Google Gemini integration
Pinecone vector search
Conversation history
Context-aware follow-up questions
Restaurant-specific knowledge
Prevents unsupported menu information from being invented


🐳 Deployment
Docker containerization
Render deployment
GitHub repository
GitHub Pages widget hosting
---

## 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Google text-embedding-004 |
| Vector Database | Pinecone |
| AI Framework | LangChain |
| Containerization | Docker |
| Deployment | Render |
| Widget Hosting | GitHub Pages |
| Version Control | Git & GitHub |


---

🧩 Embeddable Widget Architecture

The chatbot can operate independently from the restaurant website.


Client Website
      │
      │ <script>
      ▼
GitHub Pages
widget.js + widget.css
      │
      │ HTTP POST /api/chat
      ▼
Render
Flask API
      │
      ▼
RAG Pipeline
   ┌──┴──┐
   ▼     ▼
Pinecone Gemini


---


smart-restaurant/
│
├── chatbot/
│   ├── embeddings.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   ├── chat_model.py
│   ├── conversation_manager.py
│   └── vector_store.py
│
├── data/
│   ├── instruction.docx
│   └── menu.json
│
├── docs/
│   └── screenshots/
│       ├── homepage.png
│       ├── chatbot.png
│       ├── chatbot-answer.png
│       ├── menu.png
│       └── order.png
│
├── static/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   ├── chatbot.css
│   └── chatbot.js
│
├── widget/
│   ├── widget.js
│   ├── widget.css
│   ├── test.html
│   └── README.md
│
├── tests/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md


```

---

# 🧠 System Architecture

![Architecture](docs/screenshots/architecture.png)

---

# 📷 Screenshots

## Homepage

![Homepage](docs/screenshots/homepage.png)

---

## Menu

![Menu](docs/screenshots/menu.png)

---

## AI Chatbot

![Chatbot](docs/screenshots/chatbot.png)

---

## AI Response

![Answer](docs/screenshots/chatbot-answer.png)

---

## Order System

![Order](docs/screenshots/order.png)

---

## Docker

![Docker](docs/screenshots/docker.png)

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Hozayfa-Ahsan/smart-restaurant.git
```

Go inside

```bash
cd smart-restaurant
```

Install packages

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GOOGLE_API_KEY=YOUR_API_KEY
PINECONE_API_KEY=YOUR_API_KEY
PINECONE_INDEX_NAME=foodie
```

Run

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🐳 Docker

Build

```bash
docker build -t smart-restaurant .
```

Run

```bash
docker run --env-file .env -p 5000:5000 smart-restaurant
```
---




🚀 Run Locally
1. Clone the repository
git clone https://github.com/Hozayfa-Ahsan/smart-restaurant.git
2. Enter the project
cd smart-restaurant
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file:

GOOGLE_API_KEY=YOUR_API_KEY
PINECONE_API_KEY=YOUR_API_KEY
PINECONE_INDEX_NAME=YOUR_INDEX_NAME

Never commit the .env file to GitHub.

5. Run the application
python app.py

Open:

http://127.0.0.1:5000


---
🐳 Docker
Build the image
docker build -t smart-restaurant .
Run the container
docker run --env-file .env -p 5000:5000 smart-restaurant

Open:

http://127.0.0.1:5000


---
🌐 Deployment

The application is deployed using:

Backend

Render

https://smart-restaurant-qzvz.onrender.com
Widget

GitHub Pages

https://hozayfa-ahsan.github.io/smart-restaurant/widget/widget.js
Source Code

GitHub

https://github.com/Hozayfa-Ahsan/smart-restaurant



---
🔐 Security

Sensitive credentials are stored in environment variables rather than source code.

The repository does not contain:

Google API keys
Pinecone API keys
.env
orders.json

The .gitignore file prevents sensitive local files from being committed.



---

# 📌 Future Improvements

- User authentication
- Admin dashboard
- Database integration
- Online payment gateway
- Reservation system
- Voice-enabled chatbot
- Multi-language support
- Multi-tenant chatbot management
- Client dashboard
- Analytics and conversation monitoring

---

# 👨‍💻 Author

**Hozayfa Ahsan**

GitHub:

https://github.com/Hozayfa-Ahsan

---

# 📜 License

This project is released under the MIT License.
