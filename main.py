from flask import Flask, render_template, request, Response
from messenger import saveMessage


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('root.html')

@app.route('/send', methods = ['POST'])
def send():
    saveMessage(request.get_json()['message'])
    return Response(status=202)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
