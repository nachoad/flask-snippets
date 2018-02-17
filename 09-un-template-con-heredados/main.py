from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name='Nacho'):
    age = 19
    my_list = [1, 2, 3, 4]
    return render_template('user.html', nombre=name, age=age, mylist=my_list)
