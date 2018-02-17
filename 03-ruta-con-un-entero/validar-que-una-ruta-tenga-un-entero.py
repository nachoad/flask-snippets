from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/params/')
# Valida que el parámetro num sea un entero tipo int
@app.route('/params/<int:num>')
def params(num= '0'):
    return 'El número recibido es: {}'.format(num)

# URL de prueba:
# http://url/1234
