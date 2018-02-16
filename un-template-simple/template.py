from flask import Flask
from flask import render_template

# por defecto coge los templates de la carpeta que haya dentro de la que está este archivo
# y que se llama 'templates'
app = Flask(__name__)

# Si quiero yo poner el nombre de una carpeta para los templates, debo hacerlo así:
# app = Flask(__name__, template_folder='carpeta_nueva_de_templates')

@app.route('/')
def hello_world():
    return render_template('index.html')

