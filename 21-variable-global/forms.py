from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators

class LoginForm(Form):
    username = StringField('Username',
                            [
                                validators.DataRequired(message='El username es requerido.'),
                                validators.length(min=2, max=7, message='Introduzca un username válido!')

                            ]
                           )
    password = PasswordField('Password',
                       [
                           validators.DataRequired(message='Contraseña requerida.')
                       ])
