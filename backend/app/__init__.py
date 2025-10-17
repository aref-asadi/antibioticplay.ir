# File: backend/app/__init__.py

from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_jwt_extended import JWTManager # <-- ایمپورت جدید
from config import Config

mongo = PyMongo()
jwt = JWTManager() # <-- ساخت نمونه جدید

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    mongo.init_app(app)
    jwt.init_app(app) # <-- مقداردهی اولیه JWT با اپلیکیشن

    from .routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # --- ثبت Blueprint آزمون ---
    from .routes import quiz_bp # <-- ایمپورت جدید
    app.register_blueprint(quiz_bp, url_prefix='/api/quizzes')

    # روت‌های تست را می‌توانیم حذف کنیم یا نگه داریم
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