from app import app, db
from models import User, Car, Booking, Payment
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

def random_date_range():
    start_date = datetime.now() + timedelta(days=random.randint(1, 10))
    end_date = start_date + timedelta(days=random.randint(1, 7))
    return start_date, end_date
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

my_images_array = [
    '"https://images.unsplash.com/photo-1624578571415-09e9b1991929?q=80&w=1890&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg"',
    'https://images.unsplash.com/photo-1635702820786-a10548e3732f?q=80&w=2090&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1670069247956-1a6dfee5338e?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1585011664466-b7bbe92f34ef?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1586464836139-86553c751f65?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1635990716619-7710162ea073?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1728236436940-10b097998033?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1641783939273-8e77bc7085c5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1712095315056-beba206d0bcb?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1636882441787-d9ac4ea22637?q=80&w=2072&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
]


cars = [
    Car(type='Sedan', name='Toyota Camry', description='Comfortable and efficient', price=55.0,
        image_url=random.choice(my_images_array), status='available', review=4.2),
    Car(type='Hatchback', name='Honda Fit', description='Compact and reliable', price=40.0,
        image_url=random.choice(my_images_array), status='available', review=4.1),
    Car(type='SUV', name='Ford Explorer', description='Spacious and powerful', price=80.0,
        image_url=random.choice(my_images_array), status='available', review=4.5),
    Car(type='Electric', name='Tesla Model 3', description='Modern and electric', price=100.0,
        image_url=random.choice(my_images_array), status='available', review=4.8),
    Car(type='Convertible', name='Mazda MX-5', description='Sporty and fun', price=70.0,
        image_url=random.choice(my_images_array), status='available', review=4.7),
    Car(type='Luxury', name='BMW X5', description='Elegant and comfortable', price=120.0,
        image_url=random.choice(my_images_array), status='available', review=4.6),
    Car(type='Sedan', name='Mercedes-Benz C-Class', description='Luxury and performance', price=130.0,
        image_url=random.choice(my_images_array), status='available', review=4.9),
    Car(type='SUV', name='Jeep Wrangler', description='Off-road and tough', price=90.0,
        image_url=random.choice(my_images_array), status='available', review=4.3),
    Car(type='Sporty', name='Porche 911', description='Fuel-efficient and smart', price=50.0,
        image_url=random.choice(my_images_array), status='available', review=4.5),
    Car(type='Truck', name='Ford F-150', description='Strong and reliable', price=95.0,
        image_url=random.choice(my_images_array), status='available', review=4.4)
]


db.session.add_all(users)  
db.session.commit()         

db.session.add_all(cars)   
db.session.commit()         


bookings = []
for _ in range(5):
        user = random.choice(users)
        car = random.choice(cars)
        start_date, end_date = random_date_range()
        total_cost = (end_date - start_date).days * car.price
        status = random.choice(['pending', 'active', 'complete'])

        booking = Booking(
            user_id=user.id,
            car_id=car.id,
            start_date=start_date,
            end_date=end_date,
            total_cost=total_cost,
            status=status
        )
        bookings.append(booking)

db.session.add_all(bookings)
db.session.commit()  

payments = []
for booking in bookings:
        if booking.status == 'complete':
            payment = Payment(
                booking_id=booking.id,
                amount_received=booking.total_cost,
                payment_date=datetime.utcnow(),
                status='complete'
            )
            payments.append(payment)


db.session.add_all(payments)
db.session.commit()

print("Database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():
        seed_data()
   

