# File: backend/app/models/user.py
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, password=None, email=None, level=1, xp=0, total_score=0, badges=None, correct_streak=0, avatar_id='fleming'):
        self.username = username
        self.email = email
        if password:
            self.password_hash = generate_password_hash(password)
        else:
            self.password_hash = None
            
        self.level = level
        self.xp = xp
        self.total_score = total_score
        self.badges = badges if badges else []
        self.correct_streak = correct_streak
        self.avatar_id = avatar_id

    def to_dict(self):
        """تبدیل اطلاعات کاربر به دیکشنری برای ارسال به فرانت"""
        return {
            "username": self.username,
            "email": self.email,
            "level": self.level,
            "xp": self.xp,
            "total_score": self.total_score,
            "badges": self.badges,
            "correct_streak": self.correct_streak,
            "avatar_id": self.avatar_id,
            "league": User.get_league_info(self.total_score)
        }

    @staticmethod
    def create_user(username, password, email=None, avatar_id='fleming'):
        """ایجاد کاربر جدید در دیتابیس"""
        if User.find_by_username(username):
            return None
        if email and User.find_by_email(email):
            return None
        
        new_user = User(username, password, email=email, avatar_id=avatar_id)
        
        mongo.db.users.insert_one({
            "username": new_user.username,
            "email": new_user.email,
            "password_hash": new_user.password_hash,
            "level": new_user.level,
            "xp": new_user.xp,
            "total_score": new_user.total_score,
            "badges": new_user.badges,
            "correct_streak": new_user.correct_streak,
            "avatar_id": new_user.avatar_id
        })
        return new_user

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({'username': username})

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})

    @staticmethod
    def check_password(user_hash, password):
        return check_password_hash(user_hash, password)
    
    @staticmethod
    def get_league_info(score):
        score = int(score or 0)
        if score <= 500:
            return {"name": "برنز", "icon": "fas fa-medal", "color": "#cd7f32"}
        elif score <= 1000:
            return {"name": "نقره", "icon": "fas fa-medal", "color": "#c0c0c0"}
        elif score <= 2000:
            return {"name": "طلا", "icon": "fas fa-trophy", "color": "#ffd700"}
        else:
            return {"name": "الماس", "icon": "fas fa-gem", "color": "#b9f2ff"}