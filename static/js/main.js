const messages = document.querySelector('#messages');
const input = document.querySelector('#input_bar input');

function sendMessage() {
    const message = input.value;
    input.value = '';

    const messageBlock = document.createElement('div');
    messageBlock.className = 'message';
    messageBlock.innerHTML = message;

    messages.appendChild(messageBlock);
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
