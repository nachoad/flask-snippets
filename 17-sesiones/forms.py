from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class CommentForm(Form):
    username = StringField('Username',
                            [
                                validators.Required(message='El username es requerido.'),
                                validators.length(min=2, max=7, message='Introduzca un username válido!')

                            ]
                           )
    email = EmailField('Correo electronico',
                       [
                           validators.Email(message='Introduzca un email válido.')
                       ])
    comment = TextField('Comentario')