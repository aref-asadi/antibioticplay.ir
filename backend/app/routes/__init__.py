# File: backend/app/routes/__init__.py

from flask import Blueprint
from flask_restful import Api

# ایمپورت کلاس‌های API از فایل‌های مربوطه
from .auth import UserRegistration, UserLogin, UserProfile
from .quiz import QuizList, QuizDetail, QuizSubmit
from .leaderboard import Leaderboard # <-- *** ایمپورت جدید ***

# --- Blueprint احراز هویت (Authentication) ---
auth_bp = Blueprint('auth_bp', __name__)
auth_api = Api(auth_bp)
auth_api.add_resource(UserRegistration, '/register')
auth_api.add_resource(UserLogin, '/login')
auth_api.add_resource(UserProfile, '/profile')

# --- Blueprint آزمون (Quiz) ---
quiz_bp = Blueprint('quiz_bp', __name__)
quiz_api = Api(quiz_bp)
quiz_api.add_resource(QuizList, '/')
quiz_api.add_resource(QuizDetail, '/<string:quiz_id>')
quiz_api.add_resource(QuizSubmit, '/submit')

# --- *** Blueprint جدید لیدربورد *** ---
leaderboard_bp = Blueprint('leaderboard_bp', __name__)
leaderboard_api = Api(leaderboard_bp)
leaderboard_api.add_resource(Leaderboard, '/') # مسیر /api/leaderboard/