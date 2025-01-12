function sendMessage() {
    const user_input = document.getElementById('user-input').value;

    if (user_input) {
        // Display user message in chat
        const user_message = document.createElement('div');
        user_message.className = 'message user-message';
        user_message.innerText = user_input;
        document.getElementById('chat-log').appendChild(user_message);

        // Send message to Flask backend
        fetch('/get', {
            method: 'POST',
            body: new URLSearchParams({
                'user_input': user_input
            }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
        .then(response => response.text())
        .then(data => {
            // Display bot response
            const bot_message = document.createElement('div');
            bot_message.className = 'message bot-message';
            bot_message.innerText = data;
            document.getElementById('chat-log').appendChild(bot_message);
        });

        // Clear the input field
        document.getElementById('user-input').value = '';
    }
}
