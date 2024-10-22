from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()



class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    # Fields to serialize
    serialize_only = ('id', 'username', 'email', 'bookings.id', 'bookings.status')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)

    # Relationship: One User has many Bookings
    bookings = db.relationship('Booking', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.id} {self.username} {self.email}>'


class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    # Fields to serialize
    serialize_only = ('id', 'type', 'name', 'price', 'status', 'bookings.user.username')

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default="available")
    review = db.Column(db.Float, nullable=False, default=0.0)

    # Relationship: One Car has many Bookings
    bookings = db.relationship('Booking', backref='car', lazy=True)

    __table_args__ = (
        CheckConstraint('price > 0', name='check_positive_price'),
        CheckConstraint("status IN ('available', 'unavailable')", name='check_valid_status'),
        CheckConstraint('0.0 <= review <= 5.0', name='check_valid_review'),
    )

    def __repr__(self):
        return f'<Car {self.id} {self.type} {self.name} {self.price} {self.status} {self.review}>'


class Booking(db.Model, SerializerMixin):
    __tablename__ = 'bookings'

    # Fields to serialize
    serialize_only = (
        'id', 'user.username', 'car.name', 'start_date', 
        'end_date', 'total_cost', 'status', 'payment.status'
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default="pending")

    # Relationship: One Booking can have one Payment
    payment = db.relationship('Payment', backref='booking', uselist=False, lazy=True)

    __table_args__ = (
        CheckConstraint('total_cost > 0', name='check_positive_cost'),
    )

    @validates('end_date')
    def validate_end_date(self, key, end_date):
        if end_date <= self.start_date:
            raise ValueError("End date must come after start date.")
        return end_date

    def __repr__(self):
        return (
            f'<Booking {self.id}, User: {self.user_id}, Car: {self.car_id}, '
            f'{self.start_date} to {self.end_date}, {self.total_cost} {self.status}>'
        )


class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'

    # Fields to serialize
    serialize_only = ('id', 'booking.id', 'amount_received', 'status')

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False)
    amount_received = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String, default="pending")

    __table_args__ = (
        CheckConstraint('amount_received >= 0', name='check_positive_received'),
        CheckConstraint("status IN ('pending', 'complete', 'failed')", name='check_payment_status'),
    )

    def __repr__(self):
        return (
            f'<Payment {self.id}, Booking: {self.booking_id}, '
            f'Amount: {self.amount_received}, Status: {self.status}>'
        )
