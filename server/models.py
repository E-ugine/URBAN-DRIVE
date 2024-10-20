from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)

    # Relationship: One User has many Bookings#
    bookings = db.relationship('Booking', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.id} {self.username} {self.email}>'

class Car(db.Model): 
    __tablename__ = 'cars'  
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String, nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)  
    status = db.Column(db.String, default="available")
    review = db.Column(db.Float, nullable=False)

    # Relationship: One Car has many Bookings#
    bookings = db.relationship('Booking', backref='car', lazy=True)

    def __repr__(self):
        return f'<Car {self.id} {self.make} {self.price_per_day} {self.status} {self.review}>'

class Booking(db.Model):
    __tablename__ = 'bookings'  
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False) 
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default="pending")  # pending or active

    # Relationship: One Booking can have one Payment#
    payment = db.relationship('Payment', backref='booking', uselist=False, lazy=True)

    def __repr__(self):
        return f'<Booking {self.id}, User: {self.user_id}, Car: {self.car_id}, {self.start_date} to {self.end_date}, {self.total_cost} {self.status}>'

class Payment(db.Model):
    __tablename__ = 'payments'  
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False) 
    amount_received = db.Column(db.Float, nullable=False) 
    payment_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String, default="pending")  # pending or completed

    def __repr__(self):
        return f'<Payment {self.id}, Booking: {self.booking_id}, Amount: {self.amount_received}, Status: {self.status}>'
