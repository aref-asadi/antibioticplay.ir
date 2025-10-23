# File: backend/app/__init__.py

from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

# ساخت نمونه‌های پکیج‌ها به صورت گلوبال
mongo = PyMongo()
jwt = JWTManager()

def create_app():
    """
    Application Factory: یک نمونه از اپلیکیشن Flask را می‌سازد و برمی‌گرداند.
    """
    app = Flask(__name__)
    
    # بارگذاری تنظیمات از فایل config.py
    app.config.from_object(Config)

    # فعال‌سازی CORS برای اجازه دسترسی از فرانت‌اند
    CORS(app)
    
    # اتصال پکیج‌ها به اپلیکیشن
    mongo.init_app(app)
    jwt.init_app(app)

    # --- ثبت Blueprintها ---
    
    from .routes import auth_bp, quiz_bp, leaderboard_bp, badge_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(quiz_bp, url_prefix='/api/quizzes')
    app.register_blueprint(leaderboard_bp, url_prefix='/api/leaderboard')
    app.register_blueprint(badge_bp, url_prefix='/api/badges')

    # --- روت‌های تست (اختیاری) ---
    @app.route('/api/ping')
    def ping():
        return "Pong!"
        
    @app.route('/api/db-check')
    def db_check():
        try:
            mongo.db.command('ping')
            return "Database connection successful!"
        except Exception as e:
            return f"Database connection failed: {e}", 500

    return app