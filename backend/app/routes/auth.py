from flask import request
from flask_restful import Resource
from app.models.user import User
from app import mongo
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required, 
    get_jwt_identity
)

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return {'message': 'فیلدهای الزامی خالی هستند'}, 400

        if User.find_by_username(username) or User.find_by_email(email):
            return {'message': 'کاربر با این نام کاربری یا ایمیل قبلاً ثبت‌نام کرده است'}, 409

        new_user = User(username=username, email=email, password=password)
        new_user.save()

        return {'message': 'کاربر با موفقیت ایجاد شد'}, 201

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        identifier = data.get('username')
        password = data.get('password')
        
        user_data = User.find_by_username(identifier)

        if not user_data:
            user_data = User.find_by_email(identifier)

        if user_data and User.check_password(user_data['password_hash'], password):
            access_token = create_access_token(identity=user_data['username'])
            refresh_token = create_refresh_token(identity=user_data['username'])
            
            return {
                'message': f'ورود موفقیت آمیز بود. خوش آمدید {user_data["username"]}!',
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        
        return {'message': 'نام کاربری/ایمیل یا رمز عبور نامعتبر است'}, 401

class UserProfile(Resource):
    @jwt_required()
    def get(self):
        current_user_username = get_jwt_identity()
        user_data = User.find_by_username(current_user_username)

        if not user_data:
            return {'message': 'کاربر یافت نشد'}, 404
        
        score = user_data.get('score', 0)
        league_info = User.get_league_info(score)

        return {
            'username': user_data['username'],
            'email': user_data['email'],
            'score': score,
            'level': user_data.get('level', 1),
            'correct_streak': user_data.get('correct_streak', 0),
            'league': league_info,
            'avatar_id': user_data.get('avatar_id', 'fleming'),
            # --- موارد زیر اضافه شدند ---
            'badges_earned': user_data.get('badges_earned', []),
            'quizzes_completed': user_data.get('quizzes_completed', 0)
        }, 200
    
class UpdateAvatar(Resource):
    @jwt_required()
    def post(self):
        current_user_username = get_jwt_identity()
        data = request.get_json()
        avatar_id = data.get('avatar_id')

        # لیست آواتارهای مجاز برای امنیت بیشتر
        valid_avatars = ['fleming', 'waksman', 'domagk', 'florey', 'hodgkin', 'bugie', 'youyou']
        
        if avatar_id not in valid_avatars:
            return {'message': 'آواتار نامعتبر است'}, 400

        # آپدیت کردن فیلد avatar_id در دیتابیس
        mongo.db.users.update_one(
            {'username': current_user_username},
            {'$set': {'avatar_id': avatar_id}}
        )

        return {'message': 'آواتار با موفقیت بروزرسانی شد'}, 200