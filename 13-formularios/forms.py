from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField


class CommentForm(Form):
    username = StringField('Username')
    email = EmailField('Correo electronico')
    comment = TextField('Comentario')