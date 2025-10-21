# File: backend/app/routes/leaderboard.py

from flask_restful import Resource
from app import mongo
from flask_jwt_extended import jwt_required
import pymongo # برای استفاده از جهت سورت

class Leaderboard(Resource):
    """
    API برای دریافت لیست ۱۰ کاربر برتر بر اساس امتیاز.
    """
    @jwt_required()
    def get(self):
        try:
            # ۱. کوئری به کالکشن users
            # ۲. فقط فیلدهای username و score را انتخاب کن (و _id را حذف کن)
            # ۳. بر اساس score به صورت نزولی (descending) مرتب کن
            # ۴. نتایج را به ۱۰ مورد محدود کن
            top_users = mongo.db.users.find(
                {},  # فیلتر: همه‌ی کاربران
                {"username": 1, "score": 1, "_id": 0}  # Projection: فقط این فیلدها
            ).sort(
                "score", pymongo.DESCENDING  # مرتب‌سازی نزولی بر اساس امتیاز
            ).limit(10) # محدود به ۱۰ نفر اول

            return list(top_users), 200

        except Exception as e:
            return {"message": str(e)}, 500