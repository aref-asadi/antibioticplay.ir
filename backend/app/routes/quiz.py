# File: backend/app/routes/quiz.py

from flask import request
from flask_restful import Resource
from app import mongo
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity
import math # برای رند کردن امتیاز
import pymongo # برای استفاده از جهت سورت

class QuizList(Resource):
    """
    API برای دریافت لیست تمام ماژول‌های آزمون.
    (این بخش بدون تغییر است)
    """
    @jwt_required()
    def get(self):
        try:
            # فقط فیلدهای مورد نیاز برای لیست را برمی‌گردانیم
            quizzes = list(mongo.db.quizzes.find({}, {"_id": 1, "id": 1, "title": 1}))
            
            for quiz in quizzes:
                quiz["_id"] = str(quiz["_id"]) # تبدیل ObjectId به رشته
                
            return quizzes, 200
        except Exception as e:
            return {"message": str(e)}, 500

class QuizDetail(Resource):
    """
    API برای دریافت جزئیات کامل و سوالات یک ماژول آزمون خاص.
    (این بخش بدون تغییر است)
    """
    @jwt_required()
    def get(self, quiz_id):
        try:
            # بر اساس 'id' که خودمان تعریف کردیم (مثل 'classification-structure') جستجو می‌کنیم
            quiz = mongo.db.quizzes.find_one({"id": quiz_id}, {"_id": 0}) # _id را برنمی‌گردانیم
            
            if quiz:
                return quiz, 200
            else:
                return {"message": "آزمون یافت نشد"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

class QuizSubmit(Resource):
    """
    API برای ثبت پاسخ کاربر، محاسبه امتیاز و آپدیت پروفایل کاربر.
    این API اکنون از انواع مختلف سوالات و سیستم Level Up پشتیبانی می‌کند.
    """
    
    def _calculate_score(self, question, user_answer):
        """
        یک تابع کمکی برای محاسبه امتیاز بر اساس نوع سوال.
        """
        question_type = question.get('type')
        solution = question.get('solution')
        points_per_correct = question.get('points_per_correct', 1)
        
        score_earned = 0
        is_correct = False
        feedback = {}

        try:
            # --- منطق برای سوالات تطبیقی (کشیدن و رها کردن) ---
            if question_type == "drag-drop-match" or question_type == "drag-drop-ordering":
                all_correct = True
                for item_id, correct_category_id in solution.items():
                    found_in_correct_category = False
                    if correct_category_id in user_answer:
                        found_in_correct_category = any(item['id'] == item_id for item in user_answer[correct_category_id])
                    
                    if found_in_correct_category:
                        feedback[item_id] = 'correct'
                        score_earned += points_per_correct
                    else:
                        feedback[item_id] = 'incorrect'
                        all_correct = False
                is_correct = all_correct

            # --- منطق برای سوالات چند انتخابی ---
            elif question_type == "multiple-select":
                user_selections = set(user_answer)
                correct_selections = set(solution)
                
                correct_choices = user_selections.intersection(correct_selections)
                incorrect_choices = user_selections.difference(correct_selections)
                
                score_earned = (len(correct_choices) * points_per_correct) - (len(incorrect_choices) * points_per_correct)
                
                if score_earned < 0:
                    score_earned = 0
                    
                is_correct = (user_selections == correct_selections)
                feedback = {opt: ('correct' if opt in correct_selections else 'incorrect') for opt in user_selections}

            # --- منطق برای سوالات درست/نادرست ---
            elif question_type == "true-false":
                all_correct = True
                for statement in question.get('statements', []):
                    statement_id = statement['id']
                    correct_answer = statement['solution']
                    user_ans = user_answer.get(statement_id)
                    
                    if user_ans == correct_answer:
                        feedback[statement_id] = 'correct'
                        score_earned += points_per_correct
                    else:
                        feedback[statement_id] = 'incorrect'
                        all_correct = False
                is_correct = all_correct
                
            # --- منطق برای سوالات جای خالی ---
            elif question_type == "drag-drop-fill":
                all_correct = True
                for blank in question.get('blanks', []):
                    blank_id = blank['id']
                    correct_option_id = blank['solution_id']
                    user_option_id = user_answer.get(blank_id)
                    
                    if user_option_id == correct_option_id:
                        feedback[blank_id] = 'correct'
                        score_earned += points_per_correct
                    else:
                        feedback[blank_id] = 'incorrect'
                        all_correct = False
                is_correct = all_correct

            # --- منطق خاص برای سوال ceftriaxone_calcium_admin ---
            if question.get('id') == 'ceftriaxone_calcium_admin':
                solution_reversed = question.get('solution_reversed')
                all_correct = True
                feedback = {}
                score_earned = 0
                for category_id, correct_item_id in solution_reversed.items():
                    user_item_id = user_answer.get(category_id)
                    if user_item_id == correct_item_id:
                        feedback[category_id] = 'correct'
                        score_earned += points_per_correct
                    else:
                        feedback[category_id] = 'incorrect'
                        all_correct = False
                is_correct = all_correct

        except Exception as e:
            print(f"Error calculating score: {e}")
            return 0, False, {}

        # امتیاز نهایی را رند می‌کنیم
        score_earned = math.ceil(score_earned)
        
        return score_earned, is_correct, feedback

    def _calculate_level(self, score):
        """
        تابع کمکی برای محاسبه سطح بر اساس امتیاز.
        منطق: سطح ۱ پایه است. به ازای هر ۱۰۰ امتیاز، ۱ سطح اضافه می‌شود.
        """
        return math.floor(score / 100) + 1

    @jwt_required()
    def post(self):
        """
        نقطه ورود اصلی API برای ثبت امتیاز (آپدیت شده با منطق Level Up)
        """
        data = request.get_json()
        quiz_id = data.get('quizId')
        question_id = data.get('questionId')
        user_answer = data.get('answer') 

        if not question_id or user_answer is None or not quiz_id:
            return {"message": "اطلاعات ارسالی ناقص است"}, 400

        # --- ۱. پیدا کردن سوال ---
        quiz = mongo.db.quizzes.find_one({"id": quiz_id})
        if not quiz:
            return {"message": "آزمون یافت نشد"}, 404
        
        question = next((q for q in quiz['questions'] if q['id'] == question_id), None)
        if not question:
            return {"message": "سوال یافت نشد"}, 404
            
        # --- ۲. محاسبه امتیاز (فراخوانی تابع کمکی) ---
        score_earned, is_correct, feedback = self._calculate_score(question, user_answer)

        # --- ۳. آپدیت امتیاز و سطح کاربر ---
        current_user_username = get_jwt_identity()
        user = mongo.db.users.find_one({'username': current_user_username})
        
        if not user:
            return {"message": "کاربر یافت نشد"}, 404
            
        # محاسبه سطح قدیمی
        current_score = user.get('score', 0)
        old_level = self._calculate_level(current_score)
        
        # محاسبه امتیاز و سطح جدید
        new_total_score = current_score + score_earned
        new_level = self._calculate_level(new_total_score)
        
        level_up_occurred = new_level > old_level
        
        # آپدیت دیتابیس با امتیاز و سطح جدید
        mongo.db.users.update_one(
            {'username': current_user_username},
            {
                '$set': {
                    'score': new_total_score,
                    'level': new_level
                }
            }
        )
            
        # --- ۴. برگرداندن بازخورد کامل ---
        return {
            "message": "جواب ثبت شد",
            "isCorrect": is_correct,
            "feedback": feedback,
            "scoreEarned": score_earned,
            "newTotalScore": new_total_score,
            "newLevel": new_level,
            "levelUp": level_up_occurred # <-- پرچم Level Up
        }, 200