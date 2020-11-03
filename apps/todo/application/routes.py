from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import TodoForm
from application.models import Todos


@app.route('/')
def index():
    all_todos = Todos.query.all()

    return render_template('list.html', todos=all_todos)


@app.route('/add', methods=['GET', 'POST'])
def add():
    error = ""
    form = TodoForm()

    if request.method == 'POST':
        name = form.name.data
        desciption = form.description.data
        todo = Todos(name=name, description=desciption)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)
