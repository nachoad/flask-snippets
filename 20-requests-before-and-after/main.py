from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import session
from flask import flash
import forms

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():

    # 1.- Ejemplo que comprueba si el usuario está en la sesión antes del request:
    if 'username' not in session:
        print("El usuario no se encuentra en la sesión.")

    # 2.- Ejemplo de hacer un simple print:
    # print ("Antes del request se va a mostrar esta línea.")

    # 3.- Por ejemplo para saber qué enpoint (dirección URL) está pidiendo:
    # print request.endpoint


# Esta función necesita como parámetro siempre el último "response" que se envía.
@app.after_request
def after_request(response):
    print ("Esto se verá justo al final.")
    # Siempre es necesario reenviar el response al final
    return (response)




@app.route('/', methods = ['GET', 'POST'])
def index():
    # print ("Ha entrado en Index")
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
    app.run(debug = True, port=8000)
