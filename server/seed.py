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
            username="eugine_roy",
            email="eugineroy@gmail.com",
            password_hash=generate_password_hash("password123").decode('utf-8')
        )
        user2 = User(
            username="frankie_onesmus",
            email="frankone@gmail.com",
            password_hash=generate_password_hash("securepass").decode('utf-8')
        )

        db.session.add_all([user1, user2])
        db.session.commit()

        # Seed Cars
        cars = [
    Car(make="Mercedes-Benz", model="S-Class", year=2022, price_per_day=200.00,
        image_url="https://example.com/mercedes_sclass.jpg"),
    Car(make="BMW", model="7 Series", year=2021, price_per_day=180.00,
        image_url="https://example.com/bmw_7series.jpg"),
    Car(make="Audi", model="A8", year=2023, price_per_day=190.00,
        image_url="https://example.com/audi_a8.jpg"),
    Car(make="Lexus", model="LS", year=2022, price_per_day=170.00,
        image_url="https://example.com/lexus_ls.jpg"),
    Car(make="Porsche", model="Panamera", year=2023, price_per_day=250.00,
        image_url="https://example.com/porsche_panamera.jpg"),
    Car(make="Bentley", model="Continental GT", year=2021, price_per_day=350.00,
        image_url="https://example.com/bentley_continental.jpg"),
    Car(make="Rolls-Royce", model="Phantom", year=2022, price_per_day=500.00,
        image_url="https://example.com/rolls_royce_phantom.jpg"),
    Car(make="Lamborghini", model="Huracan", year=2023, price_per_day=450.00,
        image_url="https://example.com/lamborghini_huracan.jpg"),
    Car(make="Ferrari", model="488 Spider", year=2022, price_per_day=470.00,
        image_url="https://example.com/ferrari_488.jpg"),
    Car(make="Maserati", model="Ghibli", year=2021, price_per_day=220.00,
        image_url="https://example.com/maserati_ghibli.jpg"),
    Car(make="Aston Martin", model="DB11", year=2023, price_per_day=320.00,
        image_url="https://example.com/astonmartin_db11.jpg"),
    Car(make="Jaguar", model="XJ", year=2021, price_per_day=210.00,
        image_url="https://example.com/jaguar_xj.jpg"),
    Car(make="Tesla", model="Model S Plaid", year=2023, price_per_day=300.00,
        image_url="https://example.com/tesla_model_s.jpg"),
    Car(make="BMW", model="i8", year=2022, price_per_day=280.00,
        image_url="https://example.com/bmw_i8.jpg"),
    Car(make="Mercedes-Benz", model="EQS", year=2023, price_per_day=290.00,
        image_url="https://example.com/mercedes_eqs.jpg"),
    Car(make="Audi", model="RS7", year=2022, price_per_day=240.00,
        image_url="https://example.com/audi_rs7.jpg"),
    Car(make="Bentley", model="Flying Spur", year=2021, price_per_day=380.00,
        image_url="https://example.com/bentley_flyingspur.jpg"),
    Car(make="Rolls-Royce", model="Ghost", year=2023, price_per_day=480.00,
        image_url="https://example.com/rolls_royce_ghost.jpg"),
    Car(make="Lamborghini", model="Aventador", year=2021, price_per_day=500.00,
        image_url="https://example.com/lamborghini_aventador.jpg"),
    Car(make="Ferrari", model="Roma", year=2022, price_per_day=460.00,
        image_url="https://example.com/ferrari_roma.jpg"),
    Car(make="Porsche", model="911 Turbo S", year=2023, price_per_day=370.00,
        image_url="https://example.com/porsche_911.jpg"),
    Car(make="McLaren", model="720S", year=2022, price_per_day=400.00,
        image_url="https://example.com/mclaren_720s.jpg"),
]
        

        db.session.add_all([cars])
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
            amount=5000.00,
            payment_method="Credit Card",
            user_id=user1.id,
            booking_id=booking1.id
        )
        payment2 = Payment(
            amount=7000.00,
            payment_method="PayPal",
            user_id=user2.id,
            booking_id=booking2.id
        )

        db.session.add_all([payment1, payment2])
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
