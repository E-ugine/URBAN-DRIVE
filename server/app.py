#!/usr/bin/env python3
from flask import Flask, jsonify, request, make_response,send_file
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime
from flask_restful import Api, Resource
from models import db, Car, User, Booking
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
import mimetypes
import cloudinary
import cloudinary.uploader
from utils.cloudinaryconfig import cloudconfig




app = Flask(__name__,static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urban_drive.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'driveme'
app.json.compact = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)
CORS(app, resources={r"/*":{"origin":"http://127.0.0.1:4000"}})




@app.route('/')
def home():
    return 'Urban Drive API'


IMAGE_DIRECTORY = '../server/static/image_uploads'


### USERS RESOURCE ###
class Users(Resource):
    # @jwt_required()
    def get(self, id=None):
        if id:  # Get a specific user by ID
            user = User.query.get(id)
            if user is None:
                return {"error": "User not found"}, 404
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }, 200

        # Get all users
        users = [
            {"id": user.id, "username": user.username, "email": user.email}
            for user in User.query.all()
        ]
        return users, 200

    # @jwt_required()
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
        if User.query.filter_by(username=data['username']).first():
            return {"error": "Username already exists"}, 400
        if User.query.filter_by(email=data['email']).first():
            return {"error": "Email already exists"}, 400
        
        # Create new user
        new_user = User(
            username=data['username'],
            email=data['email']
        )
        new_user.set_password(data['password'])
        
        db.session.add(new_user)
        db.session.commit()
        
        # Create access token
        access_token = create_access_token(identity=new_user.id)
        
        return {
            "message": "User created successfully",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email
            },
            "access_token": access_token
        }, 201
    

### CARS RESOURCE ###
class Cars(Resource):
    # @jwt_required()
    def get(self, id=None):
        if id: #get by id
            car = Car.query.get(id)
            if car is None:
                return {"error": "Car not found"}, 404
            return {
                "id": car.id,
                "name": car.name,
                "price": car.price,
                "status": car.status,
                "type":car.type,
                "description": car.description,
                "review": car.review,
                "image_url": f'/static/{car.image_url}'  
            }, 200

        # Get all cars
        cars = [
            {
                "id": car.id,
                "name": car.name,
                "price": car.price,
                "status": car.status,
                "type": car.type,
                "description": car.description,
                "review": car.review,
                "image_url": f'/static/{car.image_url}'  
            }
            for car in Car.query.all()
        ]
        return cars, 200

    # @jwt_required()
    def delete(self, id):
        car = Car.query.get(id)
        if car is None:
            return {"error": "Car not found"}, 404

        db.session.delete(car)
        db.session.commit()
        return {"message": "Car deleted successfully!"}, 200


### BOOKINGS RESOURCE ###
class Bookings(Resource):
    # @jwt_required()
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
                "status": booking.status
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
            "status": booking.status
        } for booking in bookings], 200

    # @jwt_required()
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

        return {"message": "Booking created successfully!"}, 201

    # @jwt_required()
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
    

@app.route('/upload-car-image/<int:car_id>', methods=['POST'])
def upload_car_image(car_id):
    # json , email username password profile picture , get_data (formdata)
    # check if a file is submitted as part of the request 
    if 'file' not in request.files:
        return jsonify({'message' : 'file is not part of the request'}) , 400
    
    file = request.files['file']
    
    # check if file gets uploaded 
    if file.filename == '':
        return jsonify({'message': 'no selected file found'}), 400
    
    # upload process => cloudinary 
    try:
        # resource_type = 'auto' :( image,video,raw) : image : video : raw        
        result = cloudinary.uploader.upload(file, resource_type = "image")
        print(result)
        # secure_url 
        '''
        {
            'secure_url' : 'jkhfkdhfkdhfkdf.jvkdjfkdj'
        }
        '''
        image_url = result['secure_url']
        
        # retrieve the user 
        car = Car.query.get(car_id)
        # update on car image
        car.image = image_url
        db.session.commit()
        return jsonify({'message': 'image updated successfully', "url" : image_url})
        
    except Exception as e:
        return jsonify({'message': f'the error is {str(e)}'}), 500    


# Registering Resources with Routes
api.add_resource(Users, '/users', '/users/<int:id>')
api.add_resource(Cars, '/cars', '/cars/<int:id>')
api.add_resource(Bookings, '/bookings', '/bookings/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
