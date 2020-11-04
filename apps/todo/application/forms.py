from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from application.models import Todos


class CheckIfExists:
    def __init__(self, message=None):
        self.todos = Todos.query.all()
        if not message:
            message = 'Already Exists'
        self.message = message

    def __call__(self, form, field):
        for todo in self.todos:
            if field.data.lower() == todo.name.lower():
                raise ValidationError(self.message)


class TodoForm(FlaskForm):
    name = StringField(u'Name', validators=[
        DataRequired(),
        CheckIfExists(),
        Length(min=5, max=15)
    ])
    submit = SubmitField('Add Todo')
