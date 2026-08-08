(function () {

    "use strict";

    // Prevent the widget from being loaded twice.
    if (document.getElementById("ai-chatbot-widget")) {
        return;
    }

    // =========================================
    // Configuration
    // =========================================

    const script = document.currentScript;

    const API_URL =
        script?.dataset.apiUrl ||
        "http://127.0.0.1:5000";

    const CLIENT_ID =
        script?.dataset.clientId ||
        "foodie";

    // =========================================
    // Load CSS
    // =========================================

    const css = document.createElement("link");

    css.rel = "stylesheet";

    css.href =
        new URL("widget.css", script.src).href;

    document.head.appendChild(css);

    // =========================================
    // Create Widget
    // =========================================

    const container = document.createElement("div");

    container.id = "ai-chatbot-widget";

    container.innerHTML = `

        <button id="ai-chatbot-toggle">
            💬
        </button>

        <div id="ai-chatbot-window">

            <div id="ai-chatbot-header">

                <span id="ai-chatbot-title">
                    Foodie Assistant
                </span>

                <button id="ai-chatbot-close">
                    ×
                </button>

            </div>

            <div id="ai-chatbot-messages">

                <div class="ai-chatbot-message ai-chatbot-bot">
                    Hello! How can I help you today?
                </div>

            </div>

            <div id="ai-chatbot-input-area">

                <input
                    id="ai-chatbot-input"
                    type="text"
                    placeholder="Ask something..."
                />

                <button id="ai-chatbot-send">
                    Send
                </button>

            </div>

        </div>

    `;

    document.body.appendChild(container);

    // =========================================
    // Elements
    // =========================================

    const toggleButton =
        document.getElementById("ai-chatbot-toggle");

    const closeButton =
        document.getElementById("ai-chatbot-close");

    const chatWindow =
        document.getElementById("ai-chatbot-window");

    const sendButton =
        document.getElementById("ai-chatbot-send");

    const input =
        document.getElementById("ai-chatbot-input");

    const messages =
        document.getElementById("ai-chatbot-messages");

    // =========================================
    // Session
    // =========================================

    let sessionId = null;

    // =========================================
    // Open / Close
    // =========================================

    toggleButton.addEventListener("click", function () {

        if (chatWindow.style.display === "flex") {

            chatWindow.style.display = "none";

        } else {

            chatWindow.style.display = "flex";

            input.focus();

        }

    });

    closeButton.addEventListener("click", function () {

        chatWindow.style.display = "none";

    });

    // =========================================
    // Add Message
    // =========================================

    function addMessage(text, type) {

        const message = document.createElement("div");

        message.classList.add(
            "ai-chatbot-message"
        );

        if (type === "user") {

            message.classList.add(
                "ai-chatbot-user"
            );

        } else {

            message.classList.add(
                "ai-chatbot-bot"
            );

        }

        message.textContent = text;

        messages.appendChild(message);

        messages.scrollTop =
            messages.scrollHeight;
    }

    // =========================================
    // Send Message
    // =========================================

    async function sendMessage() {

        const question =
            input.value.trim();

        if (!question) {
            return;
        }

        addMessage(
            question,
            "user"
        );

        input.value = "";

        sendButton.disabled = true;

        try {

            const response =
                await fetch(
                    `${API_URL}/api/chat`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            client_id:
                                CLIENT_ID,

                            message:
                                question,

                            session_id:
                                sessionId

                        })
                    }
                );

            const data =
                await response.json();

            if (!response.ok) {

                throw new Error(
                    data.error ||
                    "Chat request failed."
                );

            }

            sessionId =
                data.session_id ||
                sessionId;

            addMessage(
                data.answer,
                "bot"
            );

        } catch (error) {

            console.error(
                "Chatbot error:",
                error
            );

            addMessage(
                "Sorry, I couldn't connect to the AI assistant.",
                "bot"
            );

        } finally {

            sendButton.disabled = false;

            input.focus();

        }

    }

    // =========================================
    // Send button
    // =========================================

    sendButton.addEventListener(
        "click",
        sendMessage
    );

    // =========================================
    // Enter key
    // =========================================

    input.addEventListener(
        "keypress",
        function (event) {

            if (event.key === "Enter") {

                sendMessage();

            }

        }
    );

})();