from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)
    postcode = db.Column(db.String(8), nullable=False)
    order = db.relationship('Orders', backref='products')


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    order = db.relationship('Orders', backref='customers')


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column('customers_id', db.Integer,
                            db.ForeignKey('customers.id'))
    product_id = db.Column('products_id', db.Integer,
                            db.ForeignKey('products.id'))


if __name__ == '__main__':
    app.run(debug == True, host='0.0.0.0')
