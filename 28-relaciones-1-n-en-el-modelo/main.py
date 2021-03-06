from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import session
from flask import flash
import os

import forms
# Importamos el nuevo archivo config.py
from config import DevelopmentConfig

from models import db, User, Comment

app = Flask(__name__)
# Utilizamos el objeto DevelopmentConifg
app.config.from_object(DevelopmentConfig)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
	if 'username' not in session and request.endpoint in ['comment']:
		return redirect(url_for('login'))
	
	elif 'username' in session and request.endpoint in ['login', 'create']:
		return redirect(url_for('index'))

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
        password = login_form.password.data
        
        user = User.query.filter_by(username = username).first()
        if user is not None and user.verify_password(password):
        	success_message = 'Hola {}'.format(username)
        	flash(success_message)
        	session['username'] = username
        	return redirect( url_for('index'))
        else:
        	error_message = "Usuario o password no valida!"
        	flash(error_message)

        #session['username'] = login_form.username.data
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
  
  
@app.route('/comment', methods = ['GET', 'POST'])
def comment():
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		username = session['username']
		user_id = User.query(id).filter_by(username = username).first()
		comment = Comment(user_id = user_id, text = comment_form.comment.data)
							
		db.session.add(comment)
		db.session.commit()
	
		success_message = 'Se ha creado un nuevo comentario.'
		flash (success_message)
	
	return render_template('comment.html', form = comment_form)
     
  


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	db.init_app(app)

	with app.app_context():
		db.create_all()

	app.run(host='0.0.0.0', port=int(port))