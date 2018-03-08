from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
import forms

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

@app.route('/')
def index():
    custom_cookie = request.cookies.get('customm_cookie', 'Undefined')
    print ('Cookie: '+custom_cookie)

    name = 'Nacho'
    return render_template('index.html', name=name)


@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custom_cookie', 'Nacho')
    return response

@app.route('/login', methods = ['GET', 'POST'])
def login():
        session['username'] = login_form.username.data
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug = True, port=8000)
