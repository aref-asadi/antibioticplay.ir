from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, email, password, first_name, last_name):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        mongo.db.users.insert_one({
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'score': 0,
            'level': 1,
            'badges_earned': [], 
            'quizzes_completed': 0, 
            'correct_streak': 0,
            'quiz_progress': {},
            'avatar_id': 'fleming'
        })

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