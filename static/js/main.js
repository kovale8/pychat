const api = {
    sendMessage(text) {
        fetch('/send', {
            method: 'POST',
            body: JSON.stringify({message: text}),
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
};

const messages = document.querySelector('#messages');
const input = document.querySelector('#input_bar input');

function sendMessage() {
    const message = input.value;
    api.sendMessage(message);

    const messageBlock = document.createElement('div');
    messageBlock.className = 'message';
    messageBlock.innerHTML = message;

    messages.appendChild(messageBlock);
    input.value = '';
}


document.addEventListener('keydown', event => {
    switch (event.key) {
        case 'Enter':
            sendMessage();
            break;
        default:
            return;
    }
    event.preventDefault();
});
