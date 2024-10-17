from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


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
   
