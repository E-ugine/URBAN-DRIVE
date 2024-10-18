from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# a joint 'association' table between cars and features
car_features = db.Table('car_features',
    db.Column('car_id', db.Integer, db.ForeignKey('cars.id'), primary_key=True),
    db.Column('feature_id', db.Integer, db.ForeignKey('features.id'), primary_key=True)
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String) # email validation
    hashed_password = db.Column(db.String)
    phone_number = db.Column(db.String)
    address = db.Column(db.String)
    dl_number = db.Column(db.String)
    bookings = db.relationship('Booking', backref='user', lazy=True) # one user : many bookings, a one-to-many relationship

    def __repr__(self):
        return f"<Customer {self.id}, {self.first_name}>"
    

class Car(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer) 
    colour = db.Column(db.String)
    license_plate = db.Column(db.String)
    status = db.Column(db.String, default="available") # check on use of default
    price_per_day = db.Column(db.Float)
    bookings = db.relationship('Booking', backref='car', lazy=True) # one car : many bookings, a one-to-many relationship
    features = db.relationship('Feature', secondary=car_features, backref=db.backref('cars', lazy='dynamic')) # many to many relationship

    def __repr__(self):
        return f"<Car {self.id}, {self.make}, {self.model}>"


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id')) # foreign key mapping to customers table
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id')) # foreign key mapping to cars table
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_cost = db.Column(db.Float)
    status = db.Column(db.String, default="pending") # pending or active
    payment = db.relationship('Payment', backref='booking', uselist=False) # one booking : one payment, a one-to-one relationship

    def __repr__(self):
        return f"<Car {self.id}, {self.customer_id}, {self.car_id}>"
    

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'))
    total_cost = db.Column(db.Float)
    payment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String, default="pending") # pending or active
   

class Feature(db.Model):
    __tablename__ = "features"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False) # name of car
    description = db.Column(db.String, nullable=False) # possibly what is not of make or model
    average_rating = db.Column(db.Float) # include a rating mechanism for the cars


