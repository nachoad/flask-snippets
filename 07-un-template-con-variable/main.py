from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name='Nacho'):
    return render_template('user.html', nombre=name)

