from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class LoginForm(Form):
    username = StringField('Username',
                            [
                                validators.DataRequired(message='El username es requerido.'),
                                validators.length(min=2, max=7, message='Introduzca un username valido!')

                            ]
                           )
    password = PasswordField('Password',
                       [
                           validators.DataRequired(message='Contrasena requerida.')
                       ])


class CreateForm(Form):
	username = StringField('Username',
                            [
                                validators.DataRequired(message='El username es requerido.'),
                                validators.length(min=4, max=50, message='Introduzca un username valido!')

                            ]
                           )
	email = EmailField('Correo electronico',
    		[validators.Required(message = 'El email es requerido!'),
    		 validators.Email(message = 'Introduce un mail valido'),
    		 validators.length(min=4, max=50, message = 'Introduce un mail valido')])
	
	password = PasswordField('Password',
                       [
                           validators.DataRequired(message='Contrasena requerida.')
                       ])
