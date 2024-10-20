from app import app, db  # Import your Flask app and db from your app module
from models import User, Car, Booking, Payment  # Import your models
from werkzeug.security import generate_password_hash
from datetime import datetime

# Function to seed the database
def seed_data():
    # Drop and recreate all tables (use cautiously in production)
    db.drop_all()
    db.create_all()

    # Seed Users
    user1 = User(username='john_doe', email='john@example.com', password_hash=generate_password_hash('password123'))
    user2 = User(username='jane_smith', email='jane@example.com', password_hash=generate_password_hash('password123'))
    
    # Seed Cars
    car1 = Car(make='Toyota Prius', price_per_day=50, status='available', review=4.5)
    car2 = Car(make='Tesla Model 3', price_per_day=100, status='available', review=4.8)
    car3 = Car(make='BMW X5', price_per_day=80, status='available', review=4.7)
    
    # Seed Bookings
    booking1 = Booking(user_id=1, car_id=1, start_date=datetime(2024, 10, 20), end_date=datetime(2024, 10, 25), total_cost=250, status='active')
    booking2 = Booking(user_id=2, car_id=2, start_date=datetime(2024, 10, 15), end_date=datetime(2024, 10, 18), total_cost=300, status='active')

    # Seed Payments
    payment1 = Payment(booking_id=1, amount_received=250, payment_date=datetime.utcnow(), status='completed')
    payment2 = Payment(booking_id=2, amount_received=300, payment_date=datetime.utcnow(), status='completed')

    # Add all instances to the session
    db.session.add_all([user1, user2, car1, car2, car3, booking1, booking2, payment1, payment2])

    # Commit the transaction
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():  # Ensure we're running inside an application context
        seed_data()
