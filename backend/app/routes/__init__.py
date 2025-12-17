from flask import Blueprint
from flask_restful import Api

# ایمپورت کردن کلاس‌های احراز هویت و آپدیت آواتار
from .auth import UserRegistration, UserLogin, UserProfile, UpdateAvatar

from .quiz import QuizList, QuizDetail, QuizSubmit
from .leaderboard import Leaderboard
from .badge_routes import AllBadges, EarnedBadges
from .bookmarks import BookmarkToggle, BookmarkList

# Auth Blueprint setup
auth_bp = Blueprint('auth_bp', __name__)
auth_api = Api(auth_bp)

# ثبت اندپوینت‌های مربوط به کاربر
auth_api.add_resource(UserRegistration, '/register')
auth_api.add_resource(UserLogin, '/login')
auth_api.add_resource(UserProfile, '/profile')
auth_api.add_resource(UpdateAvatar, '/update-avatar')  # <-- اندپوینت جدید اضافه شد

# Quiz Blueprint setup
quiz_bp = Blueprint('quiz_bp', __name__)
quiz_api = Api(quiz_bp)
quiz_api.add_resource(QuizList, '/')
quiz_api.add_resource(QuizDetail, '/<string:quiz_id>')
quiz_api.add_resource(QuizSubmit, '/submit')

# Leaderboard Blueprint setup
leaderboard_bp = Blueprint('leaderboard_bp', __name__)
leaderboard_api = Api(leaderboard_bp)
leaderboard_api.add_resource(Leaderboard, '/')

# Badge Blueprint setup
badge_bp = Blueprint('badge_bp', __name__)
badge_api = Api(badge_bp)
badge_api.add_resource(AllBadges, '/all')
badge_api.add_resource(EarnedBadges, '/earned')

# Bookmarks Blueprint setup
bookmarks_bp = Blueprint('bookmarks_bp', __name__)
bookmarks_api = Api(bookmarks_bp)
bookmarks_api.add_resource(BookmarkToggle, '/')
bookmarks_api.add_resource(BookmarkList, '/list')