from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application.models import Todos


class TodoForm(FlaskForm):
    name = StringField('Name')
    description = StringField('Description')
    submit = SubmitField('Add Todo')
