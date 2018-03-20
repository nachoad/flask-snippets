from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import session
from flask import flash
from flask import g
import os

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
    
    
@app.route('/create', methods = ['GET', 'POST'])
def create():
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
    	user = User(create_form.username.data,
    				create_form.password.data,
    				create_form.email.data)
    
    	db.session.add(user)
    	db.session.commit()
    
        success_message = 'Usuario registrado en la base de datos'
        flash(success_message)

    return render_template('create.html', form = create_form)
    


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	db.init_app(app)

	with app.app_context():
		db.create_all()

	app.run(host='0.0.0.0', port=int(port))