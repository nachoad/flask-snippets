from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<last_name>/')
def params(name= 'este es un valor por defecto', last_name = 'valor por defecto'):
    return 'El nombre es: {}, last_name es: {}'.format(name, last_name)

# URL de prueba:
# http://url/nacho/alonso
# O una URL sin parámetros,que mostrará los valores por defecto
