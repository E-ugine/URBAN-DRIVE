#!/usr/bin/env python3
from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from datetime import datetime
from flask_restful import Api, Resource
from models import db, Car, User, Booking
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import re

# Initialize Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urban_drive.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
app.json.compact = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)
CORS(app, resources={r"/*": {"origin": "http://127.0.0.1:4000"}})


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_password(password):
    if (len(password) < 8 or 
        not any(c.isupper() for c in password) or 
        not any(c.islower() for c in password) or 
        not any(c.isdigit() for c in password)):
        return False
    return True

@app.route("/")
def home():
    return "Urban Drive API"

## AUTH ROUTES ###
@app.route('/api/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['username', 'email', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({
                'error': 'Missing required fields',
                'required': required_fields
            }), 400

        # Validate email format
        if not validate_email(data['email']):
            return jsonify({
                'error': 'Invalid email format'
            }), 400

        # Validate password strength
        if not validate_password(data['password']):
            return jsonify({
                'error': 'Password must be at least 8 characters long and contain uppercase, lowercase, and numbers'
            }), 400

        # Check if user already exists
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({
                'error': 'Email already registered'
            }), 409

        # Create new user
        new_user = User(
            user_name=data['username'],
            email=data['email']
        )
        new_user.set_password(data['password'])

        # Save to database
        db.session.add(new_user)
        db.session.commit()

        # Generate JWT token
        access_token = create_access_token(identity=new_user.id)
        
        return jsonify({
            'message': 'Registration successful',
            'user': {
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email
            },
            'access_token': access_token
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Server error',
            'message': str(e)
        }), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({
                'error': 'Missing email or password'
            }), 400

        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not user.check_password(data['password']):
            return jsonify({
                'error': 'Invalid email or password'
            }), 401

        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
            'access_token': access_token
        }), 200

    except Exception as e:
        return jsonify({
            'error': 'Server error',
            'message': str(e)
        }), 500


### USERS RESOURCE ###
class Users(Resource):
    @jwt_required()
    def get(self, id=None):
        if id:  # Get a specific user by ID
            user = User.query.get(id)
            if user is None:
                return {"error": "User not found"}, 404
            return {"id": user.id, "username": user.username, "email": user.email}, 200

        # Get all users
        users = [
            {"id": user.id, "username": user.username, "email": user.email}
            for user in User.query.all()
        ]
        return users, 200

    @jwt_required()
    def delete(self, id):
        user = User.query.get(id)
        if user is None:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully!"}, 200

    def post(self):
        data = request.get_json()

        # Check if user with the same username or email already exists
        if User.query.filter_by(username=data["username"]).first():
            return {"error": "Username already exists"}, 400
        if User.query.filter_by(email=data["email"]).first():
            return {"error": "Email already exists"}, 400

        # Create new user
        new_user = User(username=data["username"], email=data["email"])
        new_user.set_password(data["password"])

        db.session.add(new_user)
        db.session.commit()

        # Create access token
        access_token = create_access_token(identity=new_user.id)

        return {
            "message": "User created successfully",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email,
            },
            "access_token": access_token,
        }, 201

    # @app.route("/signup", methods=["POST"])
    # def signup():
    #     data = request.get_json()
    #     full_name = data.get("username")
    #     email = data.get("email")
    #     password = data.get("password")
    #     confirm_password = data.get("confirmPassword")

    #     # Validate input
    #     if not full_name or not email or not password or password != confirm_password:
    #         return jsonify({"message": "Invalid input or passwords do not match"}), 400

    #     # Check if user already exists
    #     if User.query.filter_by(email=email).first():
    #         return jsonify({"message": "Email already in use"}), 409

    #     # Create a new user
    #     new_user = User(full_name=full_name, email=email)
    #     new_user.set_password(password)

    #     try:
    #         db.session.add(new_user)
    #         db.session.commit()
    #         return jsonify({"message": "User registered successfully"}), 201
    #     except Exception as e:
    #         return jsonify({"message": "Registration failed", "error": str(e)}), 500


### CARS RESOURCE ###
class Cars(Resource):
    @jwt_required()
    def get(self, id=None):
        if id:  # get by id
            car = Car.query.get(id)
            if car is None:
                return {"error": "Car not found"}, 404
            return {
                "id": car.id,
                "type": car.type,
                "name": car.name,
                "description": car.description,
                "price": car.price,
                "image_url": car.image_url,
                "status": car.status,
                "review": car.review,
            }, 200

        # Get all cars
        cars = [
            {
                "id": car.id,
                "type": car.type,
                "name": car.name,
                "price": car.price,
                "status": car.status,
                "review": car.review,
                "image_url": car.image_url,
            }
            for car in Car.query.all()
        ]
        return cars, 200

    @jwt_required()
    def delete(self, id):
        car = Car.query.get(id)
        if car is None:
            return {"error": "Car not found"}, 404

        db.session.delete(car)
        db.session.commit()
        return {"message": "Car deleted successfully!"}, 200


### BOOKINGS RESOURCE ###
class Bookings(Resource):
    @jwt_required()
    def get(self, id=None):
        current_user_id = get_jwt_identity()
        if id:  # Get a specific booking by ID
            booking = Booking.query.get(id)
            if booking is None or booking.user_id != current_user_id:
                return {"error": "Booking not found or unauthorized"}, 404
            return {
                "id": booking.id,
                "user_id": booking.user_id,
                "car_id": booking.car_id,
                "start_date": booking.start_date,
                "end_date": booking.end_date,
                "total_cost": booking.total_cost,
                "status": booking.status,
            }, 200

        # Get all bookings for the current user
        bookings = Booking.query.filter_by(user_id=current_user_id).all()
        return [
            {
                "id": booking.id,
                "user_id": booking.user_id,
                "car_id": booking.car_id,
                "start_date": booking.start_date,
                "end_date": booking.end_date,
                "total_cost": booking.total_cost,
                "status": booking.status,
            }
            for booking in bookings
        ], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()

        new_booking = Booking(
            user_id=current_user_id,
            car_id=data["car_id"],
            start_date=datetime.strptime(data["start_date"], "%Y-%m-%d"),
            end_date=datetime.strptime(data["end_date"], "%Y-%m-%d"),
            total_cost=data["total_cost"],
            status="pending",
        )

        db.session.add(new_booking)
        db.session.commit()

        return {"message": "Booking created successfully!"}, 201

    @jwt_required()
    def put(self, id):
        current_user_id = get_jwt_identity()
        booking = Booking.query.get(id)

        if booking is None or booking.user_id != current_user_id:
            return jsonify({"error": "Booking not found or unauthorized"}), 404

        data = request.get_json()
        if "status" in data:
            booking.status = data["status"]
        if "total_cost" in data:
            booking.total_cost = data["total_cost"]

        db.session.commit()
        return {"message": "Booking updated successfully!"}, 200

    @jwt_required()
    def delete(self, id):
        current_user_id = get_jwt_identity()
        booking = Booking.query.get(id)

        if booking is None or booking.user_id != current_user_id:
            return {"error": "Booking not found or unauthorized"}, 404

        db.session.delete(booking)
        db.session.commit()
        return {"message": "Booking canceled successfully!"}, 200


# Registering Resources with Routes
api.add_resource(Users, "/api/users", "/api/users/<int:id>")
api.add_resource(Cars, "/api/cars", "/api/cars/<int:id>")
api.add_resource(Bookings, "/api/bookings", "/api/bookings/<int:id>")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
