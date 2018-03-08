from flask import Flask
from flask import render_template
from flask import request
import forms

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    name = 'Nacho'
    return render_template('index.html', name=name)

@app.route('/login')
def login():
    login_form = forms.LoginForm()

    return render_template('login.html', form = login_form)


if __name__ == '__main__':
    app.run(debug = True, port=8000)
