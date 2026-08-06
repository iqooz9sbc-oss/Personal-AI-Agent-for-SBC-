// ================================
// PERSONAL AI AGENT SBC
// script.js
// ================================

document.addEventListener("DOMContentLoaded", function () {

    const sendBtn = document.getElementById("sendBtn");
    const startBtn = document.getElementById("startBtn");
    const message = document.getElementById("message");
    const chatArea = document.getElementById("chatArea");

    // Start Chat Button
    if (startBtn) {
        startBtn.addEventListener("click", function () {
            message.focus();
        });
    }

    // Send Button
    if (sendBtn) {
        sendBtn.addEventListener("click", sendMessage);
    }

    // Press Enter to Send
    if (message) {
        message.addEventListener("keypress", function (event) {
            if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        });
    }

    function sendMessage() {

        const text = message.value.trim();

        if (text === "") {
            alert("Please type a message.");
            return;
        }

        // User Message
        const userMessage = document.createElement("p");
        userMessage.innerHTML = "<strong>You:</strong> " + text;
        chatArea.appendChild(userMessage);

        // Demo AI Response
        const aiMessage = document.createElement("p");
        aiMessage.innerHTML = "<strong>AI:</strong> I received your message: " + text;
        chatArea.appendChild(aiMessage);

        // Scroll Down
        chatArea.scrollTop = chatArea.scrollHeight;

        // Clear Input
        message.value = "";
    }

});
