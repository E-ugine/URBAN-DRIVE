from app import app, db
from models import User, Car, Booking, Payment
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
            image_url='https://unsplash.com/photos/green-mercedes-benz-coupe-on-road-during-daytime-q1bBfWG1G1E', status='available', review=4.2),
        Car(type='Hatchback', name='Honda Fit', description='Compact and reliable', price=40.0,
            image_url='https://unsplash.com/photos/a-black-car-parked-on-the-side-of-a-road-Zqkggjuco7o', status='available', review=4.1),
        Car(type='SUV', name='Ford Explorer', description='Spacious and powerful', price=80.0,
            image_url='https://unsplash.com/photos/a-black-car-on-a-road-2yBawNkiAbc', status='available', review=4.5),
        Car(type='Electric', name='Tesla Model 3', description='Modern and electric', price=100.0,
            image_url='https://unsplash.com/photos/silver-porsche-911-parked-on-parking-lot-during-daytime-U-DgtDG6MRo', status='available', review=4.8),
        Car(type='Convertible', name='Mazda MX-5', description='Sporty and fun', price=70.0,
            image_url='https://unsplash.com/photos/white-porsche-911-on-green-grass-field-under-blue-sky-during-daytime-pB7bUdsc0FM', status='available', review=4.7),
        Car(type='Luxury', name='BMW X5', description='Elegant and comfortable', price=120.0,
            image_url='https://unsplash.com/photos/a-black-and-white-photo-of-a-bmw-YdM97Vok33Y', status='available', review=4.6),
        Car(type='Sedan', name='Mercedes-Benz C-Class', description='Luxury and performance', price=130.0,
            image_url='https://unsplash.com/photos/a-blue-car-driving-down-a-street-next-to-a-parking-meter-H7PUik3WE6E', status='available', review=4.9),
        Car(type='SUV', name='Jeep Wrangler', description='Off-road and tough', price=90.0,
            image_url='https://unsplash.com/photos/two-jeeps-are-parked-in-a-grassy-field-Q8hrdqWGQjY', status='available', review=4.3),
        Car(type='Sporty', name='Porche 911', description='Fuel-efficient and smart', price=50.0,
            image_url='https://unsplash.com/photos/a-silver-and-black-sports-car-on-display-at-a-car-show-e4Jg3z0MORk', status='available', review=4.5),
        Car(type='Truck', name='Ford F-150', description='Strong and reliable', price=95.0,
            image_url='https://unsplash.com/photos/a-large-black-truck-parked-in-a-parking-lot-J873IhXuJhE', status='available', review=4.4)
    ]

    # Seed Bookings (Random users and cars, valid date ranges, and different statuses)
    bookings = []
    for _ in range(5):
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
        if booking.status == 'completed':
            payment = Payment(
                booking_id=booking.id,
                amount_received=booking.total_cost,
                payment_date=datetime.utcnow(),
                status='completed'
            )
            payments.append(payment)


    db.session.add_all(users + cars + bookings + payments)
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():
        seed_data()
