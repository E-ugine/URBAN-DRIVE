#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, Car, Booking, Payment, Feature

# Initialize Flask app, database, and migration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urban_drive.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

##RESOURCES

# USERS RESOURCE
class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)

    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'], password_hash=data['password_hash'])

        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 201)


class UserByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first_or_404(description="User not found")
        return make_response(jsonify(user.to_dict()), 200)


api.add_resource(Users, '/users')
api.add_resource(UserByID, '/users/<int:id>')


# CARS RESOURCE
class Cars(Resource):
    def get(self):
        cars = [car.to_dict() for car in Car.query.all()]
        return make_response(jsonify(cars), 200)

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

    def patch(self, id):
        data = request.get_json()
        car = Car.query.filter_by(id=id).first_or_404(description="Car not found")

        for key, value in data.items():
            setattr(car, key, value)

        db.session.commit()
        return make_response(car.to_dict(), 200)

    def delete(self, id):
        car = Car.query.filter_by(id=id).first_or_404(description="Car not found")
        db.session.delete(car)
        db.session.commit()
        return make_response('', 204)


api.add_resource(Cars, '/cars')
api.add_resource(CarByID, '/cars/<int:id>')


# BOOKINGS RESOURCE
class Bookings(Resource):
    def get(self):
        bookings = [booking.to_dict() for booking in Booking.query.all()]
        return make_response(jsonify(bookings), 200)

    def post(self):
        data = request.get_json()
        new_booking = Booking(
            user_id=data['user_id'], car_id=data['car_id'], 
            start_date=data['start_date'], end_date=data['end_date'], 
            total_cost=data['total_cost']
        )

        db.session.add(new_booking)
        db.session.commit()
        return make_response(new_booking.to_dict(), 201)


api.add_resource(Bookings, '/bookings')


# PAYMENTS RESOURCE
class Payments(Resource):
    def get(self):
        payments = [payment.to_dict() for payment in Payment.query.all()]
        return make_response(jsonify(payments), 200)

    def post(self):
        data = request.get_json()
        new_payment = Payment(
            amount=data['amount'], payment_method=data['payment_method'], 
            user_id=data['user_id'], booking_id=data['booking_id']
        )

        db.session.add(new_payment)
        db.session.commit()
        return make_response(new_payment.to_dict(), 201)


api.add_resource(Payments, '/payments')


# FEATURES RESOURCE
class Features(Resource):
    def get(self):
        features = [feature.to_dict() for feature in Feature.query.all()]
        return make_response(jsonify(features), 200)

    def post(self):
        data = request.get_json()
        new_feature = Feature(name=data['name'], description=data.get('description'))

        db.session.add(new_feature)
        db.session.commit()
        return make_response(new_feature.to_dict(), 201)


class CarFeatures(Resource):
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
