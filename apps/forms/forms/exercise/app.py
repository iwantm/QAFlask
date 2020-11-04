from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from os import getenv

from wtforms.fields.core import DateField, IntegerField, SelectField


app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('TODO_SECRET_KEY')


class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date = DateField('Date')
    age = IntegerField('Age')
    gender = SelectField('Gender', choices=[
                         'male', 'female', 'other', 'prefer not to say'])
    submit = SubmitField('Add Name')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date = form.date.data
        age = form.age.data
        gender = form.gender.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return 'thank_you ' + first_name + ' ' + last_name

    return render_template('home.html', form=form, message=error)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
