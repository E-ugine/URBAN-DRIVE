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

        # Seed Users
        user1 = User(
            first_name="Eugine", 
            last_name="Roy",  
            email="eugineroy@gmail.com",
            hashed_password=generate_password_hash("password123").decode('utf-8'),
            phone_number="1234567890",
            address="123 Main St, Nairobi",
            dl_number="DL123456789"
        )
        user2 = User(
            first_name="Frankie",
            last_name="Onesmus",  
            email="frankone@gmail.com",
            hashed_password=generate_password_hash("securepass").decode('utf-8'),
            phone_number="0987654321",
            address="456 Elm St, Mombasa",
            dl_number="DL987654321"
        )

        db.session.add_all([user1, user2])
        db.session.commit()

        # Seed Cars
        cars = [
            Car(make="Mercedes-Benz", model="S-Class", year=2022, price_per_day=200.00, colour="Black", license_plate="KAA123A"),
            Car(make="BMW", model="7 Series", year=2021, price_per_day=180.00, colour="White", license_plate="KBB456B"),
        ]

        db.session.add_all(cars)
        db.session.commit()

        # Seed Features
        features = [
            Feature(name="Adaptive Cruise Control", description="Automatically adjusts speed to maintain safe distance from other vehicles."),
            Feature(name="Premium Sound System", description="High-quality surround sound system for an immersive audio experience."),
        ]

        db.session.add_all(features)
        db.session.commit()

        # Associate Features with Cars (Many-to-Many)
        cars[0].features.extend([features[0], features[1]]) 
        cars[1].features.append(features[0])  
        db.session.commit()

        # Seed Bookings
        booking1 = Booking(
            customer_id=user1.id, 
            car_id=cars[0].id,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=3),
            total_cost=600.00
        )
        booking2 = Booking(
            customer_id=user2.id,
            car_id=cars[1].id,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=2),
            total_cost=360.00
        )

        db.session.add_all([booking1, booking2])
        db.session.commit()

        # Seed Payments
        payment1 = Payment(
            booking_id=booking1.id,
            total_cost=600.00,
            payment_date=datetime.now(),
            status="pending"
        )
        payment2 = Payment(
            booking_id=booking2.id,
            total_cost=360.00,
            payment_date=datetime.now(),
            status="pending"
        )

        db.session.add_all([payment1, payment2])
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
