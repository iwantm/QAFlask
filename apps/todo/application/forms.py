from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application.models import Todos


class TodoForm(FlaskForm):
    name = StringField(u'Name')
    description = StringField('Description')
    submit = SubmitField('Add Todo')
