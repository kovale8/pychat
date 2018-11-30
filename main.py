from flask import Flask, render_template, request, Response, jsonify
import messenger
import ptvsd

app = Flask(__name__)

@app.route('/')
def root():
    messages = messenger.getMessages()
    languages = messenger.getLanguages()
    return render_template('root.html',
        messages=messages,
        languages=languages
    )

@app.route('/send', methods = ['POST'])
def send():
    messenger.saveMessage(request.get_json()['message'])
    return Response(status=202)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
