from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import session
import forms

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

@app.route('/', methods = ['GET', 'POST'])
def index():
    # Leemos la session
    if 'username' in session:
        username = session['username']
        print (username)
    name = 'Nacho'
    return render_template('index.html', name=name)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        # Creamos la session
        session['username'] = login_form.username.data

    return render_template('login.html', form = login_form)


@app.route('/logout')
def logout():
    if 'username' in session:
        # Destruimos la session
        session.pop('username')

    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug = True, port=8000)
