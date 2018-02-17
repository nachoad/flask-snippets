from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/params/<name>/')
def params(name):
    return 'El nombre es: {}'.format(name)

# URL de prueba:
# http://url/params/nacho