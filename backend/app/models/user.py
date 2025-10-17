# File: backend/app/models/user.py

from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """
    مدل کاربر برای تعامل با کالکشن users در MongoDB
    """
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        # هرگز رمز عبور را به صورت متن ساده ذخیره نکنید!
        self.password_hash = generate_password_hash(password)

    def save(self):
        """کاربر جدید را در دیتابیس ذخیره می‌کند."""
        mongo.db.users.insert_one({
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            # اطلاعات گیمیفیکیشن در آینده اینجا اضافه می‌شود
            'score': 0,
            'level': 1
        })

    @staticmethod
    def find_by_username(username):
        """کاربر را بر اساس نام کاربری پیدا می‌کند."""
        return mongo.db.users.find_one({'username': username})

    @staticmethod
    def find_by_email(email):
        """کاربر را بر اساس ایمیل پیدا می‌کند."""
        return mongo.db.users.find_one({'email': email})

    @staticmethod
    def check_password(user_hash, password):
        """رمز عبور وارد شده را با هش ذخیره شده مقایسه می‌کند."""
        return check_password_hash(user_hash, password)