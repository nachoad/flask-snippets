from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/params')
def params():
    param = request.args.get('nombre', 'no contiene el parametro')
    return 'El parametro es {}'.format(param)
