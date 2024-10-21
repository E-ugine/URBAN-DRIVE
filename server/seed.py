from app import app, db  # Import your Flask app and db from the app module
from models import User, Car, Booking, Payment  # Import the models
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

# Helper function to generate random date ranges for bookings
def random_date_range():
    start_date = datetime.now() + timedelta(days=random.randint(1, 10))
    end_date = start_date + timedelta(days=random.randint(1, 7))
    return start_date, end_date

# Seed function to populate the database
def seed_data():
    # Drop and recreate all tables (use cautiously in production)
    db.drop_all()
    db.create_all()

    # Seed Users
    users = [
        User(username='simba_mufasa', email='simba@gmail.com', password_hash=generate_password_hash('minicraft1')),
        User(username='ray_reddington', email='ray@gmail.com', password_hash=generate_password_hash('silentnait4')),
        User(username='leo_messi', email='leo@gmail.com', password_hash=generate_password_hash('secureME')),
        User(username='bob_boyka', email='bob@gmail.com', password_hash=generate_password_hash('pickinit@1')),
        User(username='charlie_white', email='charlie@gmail.com', password_hash=generate_password_hash('blacklistssn4')),
        User(username='diana_love', email='diana@gmail.com', password_hash=generate_password_hash('the100adventures'))
    ]

    # Seed Cars (10 cars with all fields populated)
    cars = [
        Car(type='Sedan', name='Toyota Camry', description='Comfortable and efficient', price=55.0,
            image_url='https://example.com/camry.jpg', status='available', review=4.2),
        Car(type='Hatchback', name='Honda Fit', description='Compact and reliable', price=40.0,
            image_url='https://example.com/fit.jpg', status='available', review=4.1),
        Car(type='SUV', name='Ford Explorer', description='Spacious and powerful', price=80.0,
            image_url='https://example.com/explorer.jpg', status='available', review=4.5),
        Car(type='Electric', name='Tesla Model 3', description='Modern and electric', price=100.0,
            image_url='https://example.com/model3.jpg', status='available', review=4.8),
        Car(type='Convertible', name='Mazda MX-5', description='Sporty and fun', price=70.0,
            image_url='https://example.com/mx5.jpg', status='available', review=4.7),
        Car(type='Luxury', name='BMW X5', description='Elegant and comfortable', price=120.0,
            image_url='https://example.com/x5.jpg', status='available', review=4.6),
        Car(type='Sedan', name='Mercedes-Benz C-Class', description='Luxury and performance', price=130.0,
            image_url='https://example.com/cclass.jpg', status='available', review=4.9),
        Car(type='SUV', name='Jeep Wrangler', description='Off-road and tough', price=90.0,
            image_url='https://example.com/wrangler.jpg', status='available', review=4.3),
        Car(type='Hybrid', name='Toyota Prius', description='Fuel-efficient and smart', price=50.0,
            image_url='https://example.com/prius.jpg', status='available', review=4.5),
        Car(type='Truck', name='Ford F-150', description='Strong and reliable', price=95.0,
            image_url='https://example.com/f150.jpg', status='available', review=4.4)
    ]

    # Seed Bookings (Random users and cars, valid date ranges, and different statuses)
    bookings = []
    for _ in range(5):  # Create 5 random bookings
        user = random.choice(users)
        car = random.choice(cars)
        start_date, end_date = random_date_range()
        total_cost = (end_date - start_date).days * car.price
        status = random.choice(['pending', 'active', 'completed'])

        booking = Booking(
            user_id=user.id,
            car_id=car.id,
            start_date=start_date,
            end_date=end_date,
            total_cost=total_cost,
            status=status
        )
        bookings.append(booking)

    # Seed Payments (Match with some of the bookings)
    payments = []
    for booking in bookings:
        if booking.status == 'completed':  # Only completed bookings have payments
            payment = Payment(
                booking_id=booking.id,
                amount_received=booking.total_cost,
                payment_date=datetime.utcnow(),
                status='completed'
            )
            payments.append(payment)

    # Add everything to the session
    db.session.add_all(users + cars + bookings + payments)

    # Commit the transaction
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():  # Ensure we're running inside the application context
        seed_data()
