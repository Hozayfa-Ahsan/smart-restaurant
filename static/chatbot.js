let sessionId = null;
const toggleButton = document.getElementById("chat-toggle");
const chatWindow = document.getElementById("chat-window");

const sendButton = document.getElementById("send-btn");
const inputBox = document.getElementById("chat-input");
const messages = document.getElementById("chat-messages");

// Open / Close Chat
toggleButton.addEventListener("click", () => {

    if (chatWindow.style.display === "flex") {
        chatWindow.style.display = "none";
    } else {
        chatWindow.style.display = "flex";
    }

});

// Add Message Bubble
function addMessage(text, className) {

    const div = document.createElement("div");

    div.className = className;

    div.innerText = text;

    messages.appendChild(div);

    messages.scrollTop = messages.scrollHeight;

}

// Send Message
async function sendMessage() {

    const question = inputBox.value.trim();

    if (question === "") return;

    addMessage(question, "user");

    inputBox.value = "";

    try {

        const response = await fetch(
            "/api/chat",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: question,
                    session_id: sessionId
                })
            }
        );

        const data = await response.json();

        console.log("Server Response:", data);

        sessionId = data.session_id;

        if (data.answer) {
            addMessage(data.answer, "bot");
        } else if (data.error) {
            addMessage("ERROR: " + data.error, "bot");
        } else {
            addMessage("Unexpected response from server.", "bot");
        }

    } catch (error) {

        addMessage(
            "Unable to connect to AI server.",
            "bot"
        );

    }

}

sendButton.addEventListener("click", sendMessage);

inputBox.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});