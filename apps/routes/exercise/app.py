from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return '<h3> Go to /[number] to see the number squared</h3>'


@app.route('/<int:number>')
def squared(number):
    return '<h1>' + str(number*number) + '</h1>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
