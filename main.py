from flask import Flask, render_template, request, Response, jsonify
import messenger
import ptvsd

app = Flask(__name__)

@app.route('/')
def root():
    lang = request.args.get('lang')

    if lang is None:
        messages = messenger.getMessages()
    else:
        messages = messenger.getMessagesTranslated(lang)

    return render_template('root.html',
        messages=messages,
        languages=messenger.getLanguages()
    )

@app.route('/send', methods = ['POST'])
def send():
    messenger.saveMessage(request.get_json()['message'])
    return Response(status=202)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
