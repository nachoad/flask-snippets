from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import session
from flask import flash
from flask import g

import forms
# Importamos el nuevo archivo config.py
from config import DevelopmentConfig

from models import db, User

app = Flask(__name__)
# Utilizamos el objeto DevelopmentConifg
app.config.from_object(DevelopmentConfig)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    g.test = 'Variable global'


@app.after_request
def after_request(response):
    return(response)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if 'username' in session:
        username = session['username']
        print (username)
    name = 'Nacho'
    return render_template('index.html', name=name)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        # Mostramos un mensaje de bienvenida con Flash
        username = login_form.username.data
        success_message = 'Hola {}'.format(username)
        flash(success_message)

        session['username'] = login_form.username.data
    return render_template('login.html', form = login_form)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')

    return redirect(url_for('login'))


if __name__ == '__main__':
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port=8000)
