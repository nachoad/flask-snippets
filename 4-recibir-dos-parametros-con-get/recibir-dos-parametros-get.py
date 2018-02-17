from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/params')
def params():
    param = request.args.get('nombre', 'no contiene el nombre')
    param2 = request.args.get('sueldo', 'no contiene sueldo')
    return 'El nombre es: {} y su sueldo es: {}'.format(param, param2)

# URL de prueba:
# http://nachoad.pythonanywhere.com/params?nombre=nacho&sueldo=3000