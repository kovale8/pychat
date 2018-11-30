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

const langSelect = document.querySelector('#language-select');
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

function setLangSelection() {
    const url = new URL(window.location.href);
    const lang = url.searchParams.get('lang');
    if (lang)
        langSelect.value = lang;
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

langSelect.addEventListener('change', () => {
    const lang = langSelect.value;
    const loc = window.location;
    const origin = loc.origin;

    if (!lang)
        loc.replace(origin);
    else {
        const url = new URL(origin);
        url.searchParams.set('lang', lang);
        loc.replace(url.href);
    }
});

setLangSelection();
