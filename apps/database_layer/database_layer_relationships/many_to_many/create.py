from app import db, Products, Customers, Orders
db.create_all()

customer_1 = Customers(
    name='Iwan Moreton',
    email='me@iwanmoreton.com',
    house_number=2,
    postcode='BB5 5BU')
customer_2 = Customers(
    name='First Last',
    email='me@iwanmoreton.com',
    house_number=2,
    postcode='BB5 5BU')

db.session.add(customer_1)
db.session.add(customer_2)
db.session.commit()

product_1 = Products(
    title='Game 1',
    price=32.50,
    stock=1
)
product_2 = Products(
    title='Game 2',
    price=35,
    stock=2
)
db.session.add(product_1)
db.session.add(product_2)
db.session.commit()

order_1 = Orders(
    customer_id=Customers.query.filter_by(name='Iwan Moreton').first().id,
    product_id=Products.query.filter_by(title='Game 1').first().id
)

order_2 = Orders(
    customer_id=Customers.query.filter_by(name='Iwan Moreton').first().id,
    product_id=Products.query.filter_by(title='Game 2').first().id
)

order_3 = Orders(
    customer_id=Customers.query.filter_by(name='First Last').first().id,
    product_id=Products.query.filter_by(title='Game 1').first().id
)

db.session.add(order_1)
db.session.add(order_2)

db.session.add(order_3)

db.session.commit()
