# File: backend/app/routes/quiz.py

from flask import request
from flask_restful import Resource
from app import mongo
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity
import math # برای رند کردن امتیاز
import pymongo

class QuizList(Resource):
    @jwt_required()
    def get(self):
        try:
            # --- *** Update projection to include 'icon' *** ---
            quizzes = list(mongo.db.quizzes.find(
                {},
                {"_id": 1, "id": 1, "title": 1, "icon": 1} # <-- Add "icon": 1
            ))
            # --- *** End Update *** ---

            for quiz in quizzes:
                quiz["_id"] = str(quiz["_id"])

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
    API برای ثبت پاسخ، محاسبه امتیاز، آپدیت سطح، و اهدای نشان.
    """
    
    # --- تابع محاسبه امتیاز (بدون تغییر) ---
    def _calculate_score(self, question, user_answer):
        # (این تابع که در فاز ۶ ساختیم، بدون تغییر باقی می‌ماند)
        # (منطق کامل محاسبه امتیاز برای انواع سوالات)
        question_type = question.get('type')
        solution = question.get('solution')
        points_per_correct = question.get('points_per_correct', 1)
        score_earned = 0
        is_correct = False
        feedback = {}
        try:
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
            elif question_type == "multiple-select":
                user_selections = set(user_answer)
                correct_selections = set(solution)
                correct_choices = user_selections.intersection(correct_selections)
                incorrect_choices = user_selections.difference(correct_selections)
                score_earned = (len(correct_choices) * points_per_correct) - (len(incorrect_choices) * points_per_correct)
                if score_earned < 0: score_earned = 0
                is_correct = (user_selections == correct_selections)
                feedback = {opt: ('correct' if opt in correct_selections else 'incorrect') for opt in user_selections}
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
        score_earned = math.ceil(score_earned)
        return score_earned, is_correct, feedback

    # --- تابع محاسبه سطح (بدون تغییر) ---
    def _calculate_level(self, score):
        return math.floor(score / 100) + 1

    # --- *** تابع جدید برای بررسی و اهدای نشان *** ---
    def _check_and_award_badges(self, user):
        """
        بررسی می‌کند که آیا کاربر شرایط دریافت نشان‌های جدید را دارد یا خیر.
        """
        newly_earned_badges = []
        user_badge_ids = user.get('badges_earned', [])
        
        # ۱. دریافت تمام نشان‌های ممکن از دیتابیس
        all_badges = list(mongo.db.badges.find({}, {"_id": 0}))
        
        for badge in all_badges:
            badge_id = badge['id']
            
            # اگر کاربر از قبل این نشان را دارد، بررسی نکن
            if badge_id in user_badge_ids:
                continue

            # ۲. بررسی شرایط هر نشان
            criteria = badge.get('criteria', {})
            criteria_type = criteria.get('type')
            
            earned = False
            
            if criteria_type == 'reach_score':
                if user.get('score', 0) >= criteria.get('score', 0):
                    earned = True
            
            elif criteria_type == 'reach_level':
                if user.get('level', 1) >= criteria.get('level', 1):
                    earned = True
                    
            elif criteria_type == 'complete_quiz':
                if user.get('quizzes_completed', 0) >= criteria.get('count', 0):
                    earned = True
                    
            elif criteria_type == 'correct_streak':
                if user.get('correct_streak', 0) >= criteria.get('count', 0):
                    earned = True

            # ۳. اگر شرایط مهیا بود، نشان را به کاربر بده
            if earned:
                user_badge_ids.append(badge_id)
                newly_earned_badges.append(badge) # آبجکت کامل نشان را برمی‌گردانیم
                
        # ۴. آپدیت لیست نشان‌های کاربر در دیتابیس
        if newly_earned_badges:
            mongo.db.users.update_one(
                {'_id': user['_id']},
                {'$set': {'badges_earned': user_badge_ids}}
            )
            
        return newly_earned_badges

    @jwt_required()
    def post(self):
        """
        نقطه ورود اصلی API (آپدیت شده با منطق Badge)
        """
        data = request.get_json()
        quiz_id = data.get('quizId')
        question_id = data.get('questionId')
        user_answer = data.get('answer') 
        is_last_question = data.get('isLastQuestion', False) # فرانت‌اند باید این را بفرستد

        if not question_id or user_answer is None or not quiz_id:
            return {"message": "اطلاعات ارسالی ناقص است"}, 400

        # --- ۱. پیدا کردن سوال ---
        quiz = mongo.db.quizzes.find_one({"id": quiz_id})
        question = next((q for q in quiz['questions'] if q['id'] == question_id), None)
            
        # --- ۲. محاسبه امتیاز ---
        score_earned, is_correct, feedback = self._calculate_score(question, user_answer)

        # --- ۳. آپدیت امتیاز، سطح، و رکوردهای کاربر ---
        current_user_username = get_jwt_identity()
        user = mongo.db.users.find_one({'username': current_user_username})
        
        if not user:
            return {"message": "کاربر یافت نشد"}, 404
            
        # دریافت مقادیر فعلی
        current_score = user.get('score', 0)
        current_streak = user.get('correct_streak', 0)
        current_quizzes_completed = user.get('quizzes_completed', 0)
        
        # محاسبه مقادیر جدید
        new_total_score = current_score + score_earned
        new_level = self._calculate_level(new_total_score)
        
        # آپدیت رکورد (streak)
        if is_correct:
            new_streak = current_streak + 1
        else:
            new_streak = 0 # ریست کردن رکورد
            
        # آپدیت تعداد آزمون‌های کامل شده
        if is_last_question:
            new_quizzes_completed = current_quizzes_completed + 1
        else:
            new_quizzes_completed = current_quizzes_completed
        
        level_up_occurred = new_level > user.get('level', 1)
        
        # آپدیت دیتابیس با تمام مقادیر جدید
        mongo.db.users.update_one(
            {'_id': user['_id']},
            {
                '$set': {
                    'score': new_total_score,
                    'level': new_level,
                    'correct_streak': new_streak,
                    'quizzes_completed': new_quizzes_completed
                }
            }
        )
        
        # --- ۴. بررسی و اهدای نشان‌ها ---
        # ما آبجکت user را دوباره واکشی می‌کنیم تا با داده‌های آپدیت شده کار کنیم
        updated_user = mongo.db.users.find_one({'_id': user['_id']})
        newly_earned_badges = self._check_and_award_badges(updated_user)
            
        # --- ۵. برگرداندن بازخورد کامل ---
        return {
            "message": "جواب ثبت شد",
            "isCorrect": is_correct,
            "feedback": feedback,
            "scoreEarned": score_earned,
            "newTotalScore": new_total_score,
            "newLevel": new_level,
            "levelUp": level_up_occurred,
            "newlyEarnedBadges": newly_earned_badges # <-- *** لیست نشان‌های جدید ***
        }, 200