# File: backend/app/routes/auth.py
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User
from app import mongo

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        avatar_id = data.get('avatar_id', 'fleming')

        if not username or not password:
            return {"message": "Username and password are required"}, 400

        user = User.create_user(username, password, email, avatar_id)
        if not user:
            return {"message": "Username or email already exists"}, 400

        access_token = create_access_token(identity=username)
        return {
            "message": "User registered successfully",
            "token": access_token,
            "user": user.to_dict()
        }, 201

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
             return {"message": "Username and password are required"}, 400

        user_data = User.find_by_username(username)
        if not user_data:
             return {"message": "Invalid credentials"}, 401
        
        if not User.check_password(user_data['password_hash'], password):
            return {"message": "Invalid credentials"}, 401

        access_token = create_access_token(identity=username)
        
        # ساخت دیکشنری پاسخ با تمام فیلدها
        response_user = {
            "username": user_data['username'],
            "email": user_data.get('email'),
            "level": user_data.get('level', 1),
            "xp": user_data.get('xp', 0),
            "total_score": user_data.get('total_score', 0),
            "badges": user_data.get('badges', []),
            "correct_streak": user_data.get('correct_streak', 0),
            "avatar_id": user_data.get('avatar_id', 'fleming'),
            "league": User.get_league_info(user_data.get('total_score', 0))
        }

        return {
            "token": access_token,
            "user": response_user
        }, 200

class UserProfile(Resource):
    @jwt_required()
    def get(self):
        current_username = get_jwt_identity()
        user_data = User.find_by_username(current_username)
        
        if not user_data:
            return {"message": "User not found"}, 404
        
        response_user = {
            "username": user_data['username'],
            "email": user_data.get('email'),
            "level": user_data.get('level', 1),
            "xp": user_data.get('xp', 0),
            "total_score": user_data.get('total_score', 0),
            "badges": user_data.get('badges', []),
            "correct_streak": user_data.get('correct_streak', 0),
            "avatar_id": user_data.get('avatar_id', 'fleming'),
            "league": User.get_league_info(user_data.get('total_score', 0))
        }
        return response_user, 200

class AvatarUpdate(Resource):
    @jwt_required()
    def post(self):
        current_username = get_jwt_identity()
        data = request.get_json()
        new_avatar_id = data.get('avatar_id')

        if not new_avatar_id:
            return {"message": "Avatar ID is required"}, 400

        mongo.db.users.update_one(
            {"username": current_username},
            {"$set": {"avatar_id": new_avatar_id}}
        )

        return {"message": "Avatar updated successfully", "avatar_id": new_avatar_id}, 200