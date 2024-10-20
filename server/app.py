#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import Feature, db, User, Car, Booking, Payment

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urban_drive.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  
app.json.compact = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(app)

### AUTHENTICATION ROUTES ###

class Signup(Resource):
    def post(self):
        data = request.get_json()
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 201)


class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()

        if user and bcrypt.check_password_hash(user.password_hash, data['password']):
            token = create_access_token(identity=user.id)
            return make_response(jsonify({"token": token}), 200)
        return make_response(jsonify({"error": "Invalid credentials"}), 401)


class Profile(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        return make_response(user.to_dict(), 200)


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Profile, '/profile')


### USERS RESOURCE ###
class Users(Resource):
    @jwt_required()
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)

    @jwt_required()
    def post(self):
        data = request.get_json()
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 201)


api.add_resource(Users, '/users')


## CARS RESOURCE
class Cars(Resource):
    def get(self):
        cars = [car.to_dict() for car in Car.query.all()]
        return make_response(jsonify(cars), 200)

    @jwt_required()
    def post(self):
        data = request.get_json()
        new_car = Car(make=data['make'], model=data['model'], year=data['year'], price_per_day=data['price_per_day'])

        db.session.add(new_car)
        db.session.commit()
        return make_response(new_car.to_dict(), 201)


class CarByID(Resource):
    def get(self, id):
        car = Car.query.filter_by(id=id).first_or_404(description="Car not found")
        return make_response(jsonify(car.to_dict()), 200)

    @jwt_required()
    def patch(self, id):
        data = request.get_json()
        car = Car.query.filter_by(id=id).first_or_404(description="Car not found")

        for key, value in data.items():
            setattr(car, key, value)

        db.session.commit()
        return make_response(car.to_dict(), 200)

    @jwt_required()
    def delete(self, id):
        car = Car.query.filter_by(id=id).first_or_404(description="Car not found")
        db.session.delete(car)
        db.session.commit()
        return make_response('', 204)


api.add_resource(Cars, '/cars')
api.add_resource(CarByID, '/cars/<int:id>')


## BOOKINGS RESOURCE 
class Bookings(Resource):
    @jwt_required()
    def get(self):
        bookings = [booking.to_dict() for booking in Booking.query.all()]
        return make_response(jsonify(bookings), 200)

    @jwt_required()
    def post(self):
        data = request.get_json()
        new_booking = Booking(
            user_id=data['user_id'],
            car_id=data['car_id'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            total_cost=data['total_cost']
        )

        db.session.add(new_booking)
        db.session.commit()
        return make_response(new_booking.to_dict(), 201)


api.add_resource(Bookings, '/bookings')


## PAYMENTS RESOURCE 
class Payments(Resource):
    @jwt_required()
    def get(self):
        payments = [payment.to_dict() for payment in Payment.query.all()]
        return make_response(jsonify(payments), 200)

    @jwt_required()
    def post(self):
        data = request.get_json()
        new_payment = Payment(
            amount=data['amount'],
            payment_method=data['payment_method'],
            user_id=data['user_id'],
            booking_id=data['booking_id']
        )

        db.session.add(new_payment)
        db.session.commit()
        return make_response(new_payment.to_dict(), 201)


api.add_resource(Payments, '/payments')


## FEATURES RESOURCE 
class Features(Resource):
    def get(self):
        features = [feature.to_dict() for feature in Feature.query.all()]
        return make_response(jsonify(features), 200)

    @jwt_required()
    def post(self):
        data = request.get_json()
        new_feature = Feature(name=data['name'], description=data.get('description'))

        db.session.add(new_feature)
        db.session.commit()
        return make_response(new_feature.to_dict(), 201)


class CarFeatures(Resource):
    @jwt_required()
    def post(self, car_id):
        car = Car.query.filter_by(id=car_id).first_or_404(description="Car not found")
        data = request.get_json()
        feature = Feature.query.filter_by(id=data['feature_id']).first_or_404(description="Feature not found")

        car.features.append(feature)
        db.session.commit()
        return make_response(
            {"message": f"Feature '{feature.name}' added to car {car.make} {car.model}"}, 200
        )


api.add_resource(Features, '/features')
api.add_resource(CarFeatures, '/cars/<int:car_id>/features')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
