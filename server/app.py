#!/usr/bin/env python3
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from datetime import datetime
from flask_restful import Api, Resource
from models import db, Car, User, Booking
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

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

@app.route('/')
def home():
    return 'Urban Drive API'

class Users(Resource):
    @jwt_required()
    def get(self):
        users = []
        for user in User.query.all():
            user_dict = {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
            users.append(user_dict)
        return make_response(jsonify(users), 200)
    
    @jwt_required()
    def delete(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if user is None:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Account deleted successfully!"}), 200

class Cars(Resource):
    @jwt_required()
    def get(self):
        cars = []
        for car in Car.query.all():
            car_dict = {
                "id": car.id,
                "make": car.make,
                "price_per_day": car.price_per_day,
                "status": car.status,
                "review": car.review
            }
            cars.append(car_dict)
        return make_response(jsonify(cars), 200)

class Bookings(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        bookings = Booking.query.filter_by(user_id=current_user_id).all()
        return make_response(jsonify([{
            "id": booking.id,
            "user_id": booking.user_id,
            "car_id": booking.car_id,
            "start_date": booking.start_date,
            "end_date": booking.end_date,
            "total_cost": booking.total_cost,
            "status": booking.status
        } for booking in bookings]), 200)

    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        
        new_booking = Booking(
            user_id=current_user_id,
            car_id=data['car_id'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            total_cost=data['total_cost'],
            status="pending"
        )
        
        db.session.add(new_booking)
        db.session.commit()
        
        return jsonify({"message": "Booking created successfully!"}), 201 
    
    @jwt_required()
    def put(self, id):
        current_user_id = get_jwt_identity()
        booking = Booking.query.get(id)

        if booking is None or booking.user_id != current_user_id:
            return jsonify({"error": "Booking not found or unauthorized"}), 404

        data = request.get_json()
        if 'status' in data:
            booking.status = data['status']
        if 'total_cost' in data:
            booking.total_cost = data['total_cost']
        
        db.session.commit()
        return jsonify({"message": "Booking updated successfully!"}), 200 

    @jwt_required()
    def delete(self, id):
        current_user_id = get_jwt_identity()
        booking = Booking.query.get(id)

        if booking is None or booking.user_id != current_user_id:
            return jsonify({"error": "Booking not found or unauthorized"}), 404

        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": "Booking canceled successfully!"}), 200  

api.add_resource(Users, '/users')
api.add_resource(Cars, '/cars')
api.add_resource(Bookings, '/bookings')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
