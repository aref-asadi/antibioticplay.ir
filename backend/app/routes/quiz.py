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
            # ... (کد کامل محاسبه انواع سوالات از نسخه قبلی شما) ...
            # Logic for drag-drop-match, drag-drop-ordering
            if question_type in ["drag-drop-match", "drag-drop-ordering"]:
                all_correct = True
                for item_id, correct_category_id in solution.items():
                    found_in_correct_category = False
                    if isinstance(user_answer, dict) and correct_category_id in user_answer:
                         if isinstance(user_answer[correct_category_id], list):
                             found_in_correct_category = any(isinstance(item, dict) and item.get('id') == item_id for item in user_answer[correct_category_id])
                    if found_in_correct_category: feedback[item_id] = 'correct'; score_earned += points_per_correct
                    else: feedback[item_id] = 'incorrect'; all_correct = False
                is_correct = all_correct
            # Logic for multiple-select
            elif question_type == "multiple-select":
                 if isinstance(user_answer, list):
                    user_selections = set(user_answer)
                    correct_selections = set(solution)
                    correct_choices = user_selections.intersection(correct_selections)
                    incorrect_choices = user_selections.difference(correct_selections)
                    score_earned = (len(correct_choices) * points_per_correct) - (len(incorrect_choices) * points_per_correct)
                    if score_earned < 0: score_earned = 0
                    is_correct = (user_selections == correct_selections and len(incorrect_choices)==0)
                    feedback = {opt: ('correct' if opt in correct_selections else 'incorrect') for opt in question.get('options',[]) if opt in user_selections}
                 else: is_correct = False; feedback = {}; score_earned = 0
            # Logic for true-false
            elif question_type == "true-false":
                all_correct = True
                if isinstance(user_answer, dict):
                    for statement in question.get('statements', []):
                        statement_id = statement['id']; correct_answer = statement['solution']; user_ans = user_answer.get(statement_id)
                        if user_ans == correct_answer: feedback[statement_id] = 'correct'; score_earned += points_per_correct
                        else: feedback[statement_id] = 'incorrect'; all_correct = False
                else: all_correct = False; feedback = {}; score_earned = 0
                is_correct = all_correct
            # Logic for drag-drop-fill
            elif question_type == "drag-drop-fill":
                all_correct = True
                if isinstance(user_answer, dict):
                    for blank in question.get('blanks', []):
                        blank_id = blank['id']; correct_option_id = blank['solution_id']; user_option_id = user_answer.get(blank_id)
                        if user_option_id == correct_option_id: feedback[blank_id] = 'correct'; score_earned += points_per_correct
                        else: feedback[blank_id] = 'incorrect'; all_correct = False
                else: all_correct = False; feedback = {}; score_earned = 0
                is_correct = all_correct
            # Specific logic for ceftriaxone_calcium_admin
            if question.get('id') == 'ceftriaxone_calcium_admin' and 'solution_reversed' in question:
                 solution_reversed = question.get('solution_reversed'); all_correct = True; feedback = {}; score_earned = 0
                 if isinstance(user_answer, dict):
                    for category_id, correct_item_id in solution_reversed.items():
                        user_item_id = user_answer.get(category_id)
                        if user_item_id == correct_item_id: feedback[category_id] = 'correct'; score_earned += points_per_correct
                        else: feedback[category_id] = 'incorrect'; all_correct = False
                 else: all_correct = False; feedback = {}; score_earned = 0
                 is_correct = all_correct
        except Exception as e:
            print(f"Error calculating score for question type {question_type}: {e}")
            return 0, False, {}
        score_earned = math.ceil(score_earned) if score_earned > 0 else 0
        return score_earned, is_correct, feedback

    # --- تابع محاسبه سطح (بدون تغییر) ---
    def _calculate_level(self, score):
        return math.floor(int(score) / 20) + 1 # Ensure score is int

    # --- تابع بررسی و اهدای نشان (بدون تغییر) ---
    def _check_and_award_badges(self, user):
        # ... (کد کامل از مرحله قبل) ...
        newly_earned_badges = []; user_badge_ids = user.get('badges_earned', [])
        all_badges = list(mongo.db.badges.find({}, {"_id": 0}))
        # ... (Loop through badges and check criteria) ...
        for badge in all_badges:
            badge_id = badge['id']
            if badge_id in user_badge_ids: continue
            criteria = badge.get('criteria', {}); criteria_type = criteria.get('type'); earned = False
            # ... (Check criteria types: reach_score, reach_level, etc.) ...
            if criteria_type == 'reach_score':
                 if int(user.get('score', 0)) >= criteria.get('score', 0): earned = True
            elif criteria_type == 'reach_level':
                 if int(user.get('level', 1)) >= criteria.get('level', 1): earned = True
            elif criteria_type == 'complete_quiz':
                 if int(user.get('quizzes_completed', 0)) >= criteria.get('count', 0): earned = True
            elif criteria_type == 'correct_streak':
                 if int(user.get('correct_streak', 0)) >= criteria.get('count', 0): earned = True

            if earned: user_badge_ids.append(badge_id); newly_earned_badges.append(badge)
        if newly_earned_badges:
            mongo.db.users.update_one({'_id': user['_id']},{'$set': {'badges_earned': user_badge_ids}})
        return newly_earned_badges


    @jwt_required()
    def post(self):
        data = request.get_json()
        quiz_id = data.get('quizId')
        question_id = data.get('questionId')
        user_answer = data.get('answer')
        is_last_question = data.get('isLastQuestion', False)

        if not question_id or user_answer is None or not quiz_id:
            return {"message": "اطلاعات ارسالی ناقص است"}, 400

        # --- ۱. پیدا کردن سوال ---
        quiz = mongo.db.quizzes.find_one({"id": quiz_id})
        if not quiz: return {"message": "آزمون یافت نشد"}, 404
        question = next((q for q in quiz['questions'] if q['id'] == question_id), None)
        if not question: return {"message": "سوال یافت نشد"}, 404

        # --- ۲. محاسبه امتیاز این سوال ---
        score_earned, is_correct, feedback = self._calculate_score(question, user_answer)
        print(f"--- Question {question_id} ---") # <-- DEBUG PRINT 1
        print(f"Score earned for this question: {score_earned}, Correct: {is_correct}") # <-- DEBUG PRINT 2

        # --- ۳. آپدیت امتیاز کل، سطح، و رکوردهای کاربر ---
        current_user_username = get_jwt_identity()
        user = mongo.db.users.find_one({'username': current_user_username})
        if not user: return {"message": "کاربر یافت نشد"}, 404

        current_score = int(user.get('score', 0)) # خواندن امتیاز فعلی از دیتابیس
        print(f"Current score BEFORE adding points: {current_score}") # <-- DEBUG PRINT 3
        new_total_score = current_score + score_earned # محاسبه امتیاز کل جدید
        print(f"Calculated newTotalScore: {current_score} + {score_earned} = {new_total_score}") # <-- DEBUG PRINT 4

        current_streak = user.get('correct_streak', 0)
        current_quizzes_completed = user.get('quizzes_completed', 0)

        new_level = self._calculate_level(new_total_score)
        new_streak = current_streak + 1 if is_correct else 0
        new_quizzes_completed = current_quizzes_completed + 1 if is_last_question else current_quizzes_completed
        level_up_occurred = new_level > user.get('level', 1)

        # آپدیت دیتابیس با مقادیر جدید
        print(f"Updating DB for user {current_user_username} with score={new_total_score}, level={new_level}...") # <-- DEBUG PRINT 5
        update_result = mongo.db.users.update_one(
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
        print(f"DB Update Result: Matched={update_result.matched_count}, Modified={update_result.modified_count}") # <-- DEBUG PRINT 6


        # --- ۴. بررسی و اهدای نشان‌ها ---
        updated_user = mongo.db.users.find_one({'_id': user['_id']})
        newly_earned_badges = self._check_and_award_badges(updated_user)
        print(f"Newly earned badges: {newly_earned_badges}") # <-- DEBUG PRINT 7


        # --- ۵. برگرداندن بازخورد کامل ---
        print(f"Returning response with newTotalScore={new_total_score}") # <-- DEBUG PRINT 8
        return {
            "message": "جواب ثبت شد",
            "isCorrect": is_correct,
            "feedback": feedback,
            "scoreEarned": score_earned,
            "newTotalScore": new_total_score,
            "newLevel": new_level,
            "levelUp": level_up_occurred,
            "newlyEarnedBadges": newly_earned_badges
        }, 200