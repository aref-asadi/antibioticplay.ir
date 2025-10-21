# File: backend/app/routes/auth.py

from flask import request
from flask_restful import Resource
from app.models.user import User
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required, 
    get_jwt_identity
)

class UserRegistration(Resource):
    """
    API برای ثبت نام کاربر جدید
    """
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return {'message': 'فیلدهای الزامی خالی هستند'}, 400

        # بررسی اینکه آیا کاربر از قبل وجود دارد یا نه
        if User.find_by_username(username) or User.find_by_email(email):
            return {'message': 'کاربر با این نام کاربری یا ایمیل قبلاً ثبت‌نام کرده است'}, 409

        # ایجاد کاربر جدید (هش کردن رمز عبور در مدل انجام می‌شود)
        new_user = User(username=username, email=email, password=password)
        new_user.save()

        return {'message': 'کاربر با موفقیت ایجاد شد'}, 201

class UserLogin(Resource):
    """
    API برای ورود کاربر و صدور توکن‌های JWT
    """
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        user_data = User.find_by_username(username)

        # بررسی کاربر و تطابق رمز عبور
        if user_data and User.check_password(user_data['password_hash'], password):
            # ایجاد توکن دسترسی و توکن بازخوانی
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            
            return {
                'message': f'ورود موفقیت آمیز بود. خوش آمدید {username}!',
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        
        return {'message': 'نام کاربری یا رمز عبور نامعتبر است'}, 401

class UserProfile(Resource):
    """
    API محافظت‌شده برای دریافت اطلاعات پروفایل کاربر
    """
    @jwt_required() # این روت نیازمند توکن معتبر است
    def get(self):
        # دریافت هویت کاربر (نام کاربری) از توکن
        current_user_username = get_jwt_identity()
        user_data = User.find_by_username(current_user_username)

        if not user_data:
            return {'message': 'کاربر یافت نشد'}, 404
        
        # --- بخش اصلاح شده ---
        # اطمینان از اینکه امتیاز و سطح همیشه برگردانده می‌شوند
        return {
            'username': user_data['username'],
            'email': user_data['email'],
            'score': user_data.get('score', 0),   # از .get() برای جلوگیری از خطا استفاده می‌کنیم
            'level': user_data.get('level', 1)
        }, 200