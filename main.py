from flask import Flask
import flask_api
from flask import jsonify
from flask import request
from Service import AllMessge, MessageBulk

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(text='Hello, World!')


@app.route('/api/message', methods=['GET'])
def message():
    if request.method == 'GET':
        result = AllMessge.AllMensaje()
        return jsonify(result)


@app.route('/api/message-bulk', methods=['POST'])
def messageBulk():
    if request.method == 'POST':
        content = request.get_json(silent=True)
        if content['origen'] and content['contacto'] and content['mensaje'] and content['procesado'] == 0:
            MessageBulk.messageBulk(content)
            return jsonify({"status": True, "message": "Se inserto correctamente el mensaje"})
        else:
            return jsonify({"status": False, "error": "Falta algun campo para realizar el insert"})


app.run()
