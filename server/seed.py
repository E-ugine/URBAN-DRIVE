#!/usr/bin/env python3

from app import app, db
from models import User, Car, Booking, Payment, Feature
from flask_bcrypt import generate_password_hash
from datetime import datetime, timedelta

# Sample data
def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        user1 = User(
            username="john_doe",
            email="john@example.com",
            password_hash=generate_password_hash("password123").decode('utf-8')
        )
        user2 = User(
            username="jane_smith",
            email="jane@example.com",
            password_hash=generate_password_hash("securepass").decode('utf-8')
        )

        db.session.add_all([user1, user2])
        db.session.commit()

        # Seed Cars
        car1 = Car(make="Toyota", model="Camry", year=2021, price_per_day=40.00)
        car2 = Car(make="Honda", model="Civic", year=2022, price_per_day=35.00)
        car3 = Car(make="Tesla", model="Model 3", year=2023, price_per_day=70.00)

        db.session.add_all([car1, car2, car3])
        db.session.commit()

        # Seed Features
        feature1 = Feature(name="Bluetooth", description="Wireless connectivity for audio devices.")
        feature2 = Feature(name="GPS", description="Satellite navigation system.")
        feature3 = Feature(name="Heated Seats", description="Comfortable seating in cold weather.")

        db.session.add_all([feature1, feature2, feature3])
        db.session.commit()

        # Associate Features with Cars (Many-to-Many)
        car1.features.extend([feature1, feature2])
        car2.features.append(feature3)
        db.session.commit()

        # Seed Bookings
        booking1 = Booking(
            user_id=user1.id,
            car_id=car1.id,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=3),
            total_cost=120.00
        )
        booking2 = Booking(
            user_id=user2.id,
            car_id=car2.id,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=2),
            total_cost=70.00
        )

        db.session.add_all([booking1, booking2])
        db.session.commit()

        # Seed Payments
        payment1 = Payment(
            amount=120.00,
            payment_method="Credit Card",
            user_id=user1.id,
            booking_id=booking1.id
        )
        payment2 = Payment(
            amount=70.00,
            payment_method="PayPal",
            user_id=user2.id,
            booking_id=booking2.id
        )

        db.session.add_all([payment1, payment2])
        db.session.commit()

        print("Database seeded successfully!")

# Run the seeding function
if __name__ == '__main__':
    seed_data()
