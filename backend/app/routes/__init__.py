# File: backend/app/routes/__init__.py

from flask import Blueprint
from flask_restful import Api

# ایمپورت کلاس‌های مربوط به احراز هویت
from .auth import UserRegistration, UserLogin, UserProfile

# ایمپورت کلاس‌های مربوط به آزمون
from .quiz import QuizList, QuizDetail

# --- Blueprint احراز هویت ---
auth_bp = Blueprint('auth_bp', __name__)
auth_api = Api(auth_bp)

auth_api.add_resource(UserRegistration, '/register')
auth_api.add_resource(UserLogin, '/login')
auth_api.add_resource(UserProfile, '/profile')

# --- Blueprint آزمون ---
quiz_bp = Blueprint('quiz_bp', __name__)
quiz_api = Api(quiz_bp)

quiz_api.add_resource(QuizList, '/') # مسیر پایه /api/quizzes/
quiz_api.add_resource(QuizDetail, '/<string:quiz_id>') # مسیر /api/quizzes/some-id