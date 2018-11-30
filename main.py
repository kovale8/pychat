from flask import Flask, render_template, request, Response
import messenger
import ptvsd

try:
    ptvsd.enable_attach(address=('0.0.0.0', 5678))
except:
    pass

app = Flask(__name__)

@app.route('/')
def root():
    breakpoint()
    messages = messenger.getMessages()
    print(messages)
    return render_template('root.html', messages=messages)

@app.route('/send', methods = ['POST'])
def send():
    messenger.saveMessage(request.get_json()['message'])
    return Response(status=202)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
