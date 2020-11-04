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
        todo = Todos(name=name)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    form = TodoForm()
    current = Todos.query.get(id)
    if request.method == 'GET':
        form.name.data = current.name
    if request.method == 'POST':
        current.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html', form=form)


@app.route('/complete/<int:id>')
def complete(id):
    current = Todos.query.get(id)
    current.completed = True
    db.session.commit()
    return(redirect(url_for('index')))


@app.route('/incomplete/<int:id>')
def incomplete(id):
    current = Todos.query.get(id)
    current.completed = False
    db.session.commit()
    return(redirect(url_for('index')))


@app.route('/delete/<int:id>')
def delete(id):
    current = Todos.query.get(id)
    db.session.delete(current)
    db.session.commit()
    return(redirect(url_for('index')))
