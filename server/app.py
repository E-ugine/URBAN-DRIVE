from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Car, Booking, Payment, Feature

app = Flask(__name__)

# Configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "Welcome to the Car Rental API!"


### Routes ###

# GET /users
@app.route('/users', methods=['GET'])
def get_users():
    users = [user.to_dict() for user in User.query.all()]
    return make_response(jsonify(users), 200)


# GET /users/<id>
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return make_response(jsonify(user.to_dict()), 200)
    return make_response(jsonify({"error": "User not found"}), 404)


# POST /users
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        new_user = User(username=data['username'], email=data['email'], password_hash=data['password_hash'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify(new_user.to_dict()), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)


# GET /cars
@app.route('/cars', methods=['GET'])
def get_cars():
    cars = [car.to_dict() for car in Car.query.all()]
    return make_response(jsonify(cars), 200)


# POST /cars
@app.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    try:
        new_car = Car(
            make=data['make'], model=data['model'], year=data['year'], price_per_day=data['price_per_day']
        )
        db.session.add(new_car)
        db.session.commit()
        return make_response(jsonify(new_car.to_dict()), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)


# PATCH /cars/<id>
@app.route('/cars/<int:id>', methods=['PATCH'])
def update_car(id):
    car = Car.query.get(id)
    if not car:
        return make_response(jsonify({"error": "Car not found"}), 404)
    
    data = request.get_json()
    try:
        car.make = data.get('make', car.make)
        car.model = data.get('model', car.model)
        car.year = data.get('year', car.year)
        car.price_per_day = data.get('price_per_day', car.price_per_day)
        db.session.commit()
        return make_response(jsonify(car.to_dict()), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)


# GET /bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = [booking.to_dict() for booking in Booking.query.all()]
    return make_response(jsonify(bookings), 200)


# POST /bookings
@app.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    try:
        new_booking = Booking(
            user_id=data['user_id'],
            car_id=data['car_id'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            total_cost=data['total_cost']
        )
        db.session.add(new_booking)
        db.session.commit()
        return make_response(jsonify(new_booking.to_dict()), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)


# GET /payments
@app.route('/payments', methods=['GET'])
def get_payments():
    payments = [payment.to_dict() for payment in Payment.query.all()]
    return make_response(jsonify(payments), 200)


# POST /payments
@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    try:
        new_payment = Payment(
            amount=data['amount'],
            payment_method=data['payment_method'],
            user_id=data['user_id'],
            booking_id=data['booking_id']
        )
        db.session.add(new_payment)
        db.session.commit()
        return make_response(jsonify(new_payment.to_dict()), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)


# GET /features
@app.route('/features', methods=['GET'])
def get_features():
    features = [feature.to_dict() for feature in Feature.query.all()]
    return make_response(jsonify(features), 200)


# POST /features
@app.route('/features', methods=['POST'])
def create_feature():
    data = request.get_json()
    try:
        new_feature = Feature(name=data['name'], description=data.get('description'))
        db.session.add(new_feature)
        db.session.commit()
        return make_response(jsonify(new_feature.to_dict()), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)


# POST /cars/<car_id>/features
@app.route('/cars/<int:car_id>/features', methods=['POST'])
def add_feature_to_car(car_id):
    car = Car.query.get(car_id)
    if not car:
        return make_response(jsonify({"error": "Car not found"}), 404)

    data = request.get_json()
    feature = Feature.query.get(data['feature_id'])
    if not feature:
        return make_response(jsonify({"error": "Feature not found"}), 404)

    car.features.append(feature)
    db.session.commit()
    return make_response(jsonify({"message": f"Feature {feature.name} added to car {car.make} {car.model}"}), 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
