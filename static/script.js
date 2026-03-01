function send() {
    const input = document.getElementById("userInput");
    const msg = input.value.trim();
    if (!msg) return;

    addMessage("👤 You", msg);
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        addMessage("🤖 Bot", data.answer + "<br>📊 Confidence: " + data.confidence + "%");
    })
    .catch(() => {
        addMessage("🤖 Bot", "❌ Server error");
    });
}

function addMessage(sender, text) {
    const chat = document.getElementById("chat");
    chat.innerHTML += `<p><b>${sender}:</b> ${text}</p>`;
    chat.scrollTop = chat.scrollHeight;
}