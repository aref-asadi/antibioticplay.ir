# File: backend/app/routes/quiz.py

from flask_restful import Resource
from app import mongo
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required

class QuizList(Resource):
    @jwt_required()
    def get(self):
        """لیست تمام ماژول‌های آزمون را برمی‌گرداند."""
        try:
            quizzes = list(mongo.db.quizzes.find({}, {"_id": 1, "id": 1, "title": 1}))

            # تبدیل ObjectId به رشته برای سازگاری با JSON
            for quiz in quizzes:
                quiz["_id"] = str(quiz["_id"])

            return quizzes, 200
        except Exception as e:
            return {"message": str(e)}, 500

class QuizDetail(Resource):
    @jwt_required()
    def get(self, quiz_id):
        """سوالات یک ماژول آزمون خاص را برمی‌گرداند."""
        try:
            # ما بر اساس فیلد 'id' که خودمان تعریف کردیم (مثلاً 'classification-structure') جستجو می‌کنیم
            quiz = mongo.db.quizzes.find_one({"id": quiz_id}, {"_id": 0}) # _id را برنمی‌گردانیم

            if quiz:
                return quiz, 200
            else:
                return {"message": "آزمون یافت نشد"}, 404
        except Exception as e:
            return {"message": str(e)}, 500