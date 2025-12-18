from flask import request
from flask_restful import Resource
from app import mongo
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity
import math
import pymongo
from app.quiz_data import QUIZZES, LEARNING_PATH
from app.models.user import User

class QuizList(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.find_by_username(current_user)
        
        if not user:
            return {'message': 'User not found'}, 404
            
        completed_quizzes = user.get('completed_quizzes', [])
        
        # این متغیر تعیین می‌کند که آیا مرحله فعلی باید باز باشد یا خیر.
        # مرحله اول همیشه باز است، پس با True شروع می‌کنیم.
        unlock_next = True 

        path_data = []
        
        for unit in LEARNING_PATH:
            unit_data = {
                "id": unit["id"],
                "title": unit["title"],
                "description": unit["description"],
                "color": unit["color"],
                "levels": []
            }
            
            for quiz_id in unit["levels"]:
                quiz_info = QUIZZES.get(quiz_id)
                if quiz_info:
                    is_completed = quiz_id in completed_quizzes
                    
                    # وضعیت قفل بودن: اگر اجازه باز کردن (unlock_next) نداریم، پس قفل است.
                    is_locked = not unlock_next
                    
                    unit_data["levels"].append({
                        "id": quiz_id,
                        "title": quiz_info["title"],
                        "icon": quiz_info.get("icon", "star"),
                        "is_completed": is_completed,
                        "is_locked": is_locked, # <--- فیلد جدید
                        "total_questions": len(quiz_info["questions"])
                    })
                    
                    # منطق برای مرحله بعد:
                    # اگر مرحله فعلی تکمیل شده باشد، مرحله بعدی باز می‌شود.
                    # اگر تکمیل نشده باشد، مرحله بعدی قفل خواهد ماند.
                    if is_completed:
                        unlock_next = True
                    else:
                        unlock_next = False
            
            path_data.append(unit_data)

        return path_data, 200

class QuizDetail(Resource):
    @jwt_required()
    def get(self, quiz_id):
        try:
            quiz = mongo.db.quizzes.find_one({"id": quiz_id}, {"_id": 0})
            if quiz:
                return quiz, 200
            else:
                return {"message": "آزمون یافت نشد"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

class QuizSubmit(Resource):
    
    # --- متد کمکی: محاسبه امتیاز ---
    def _calculate_score(self, question, user_answer):
        question_type = question.get('type')
        solution = question.get('solution')
        points_per_correct = question.get('points_per_correct', 10)
        
        score_earned = 0
        is_correct = False
        feedback = {}
        
        try:
            if question_type in ["drag-drop-match", "drag-drop-ordering"]:
                all_correct = True
                for item_id, correct_category_id in solution.items():
                    found_in_correct_category = False
                    if isinstance(user_answer, dict) and correct_category_id in user_answer:
                         if isinstance(user_answer[correct_category_id], list):
                             found_in_correct_category = any(isinstance(item, dict) and item.get('id') == item_id for item in user_answer[correct_category_id])
                    
                    if found_in_correct_category:
                        feedback[item_id] = 'correct'
                        score_earned += points_per_correct
                    else:
                        feedback[item_id] = 'incorrect'
                        all_correct = False
                is_correct = all_correct

            elif question_type == "multiple-select":
                 if isinstance(user_answer, list):
                    user_selections = set(user_answer)
                    correct_selections = set(solution)
                    
                    correct_choices = user_selections.intersection(correct_selections)
                    incorrect_choices = user_selections.difference(correct_selections)
                    
                    # نمره منفی برای انتخاب غلط
                    score_earned = (len(correct_choices) * points_per_correct) - (len(incorrect_choices) * points_per_correct)
                    if score_earned < 0: score_earned = 0
                    
                    is_correct = (user_selections == correct_selections and len(incorrect_choices)==0)
                    feedback = {opt: ('correct' if opt in correct_selections else 'incorrect') for opt in question.get('options',[]) if opt in user_selections}
                 else:
                    is_correct = False
                    feedback = {}
                    score_earned = 0

            elif question_type == "true-false":
                all_correct = True
                if isinstance(user_answer, dict):
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
                else:
                    all_correct = False
                    feedback = {}
                    score_earned = 0
                is_correct = all_correct

            elif question_type == "drag-drop-fill":
                all_correct = True
                if isinstance(user_answer, dict):
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
                else:
                    all_correct = False
                    feedback = {}
                    score_earned = 0
                is_correct = all_correct
                
            elif question_type == "image-labeling":
                all_correct = True
                # بررسی می‌کنیم که جواب کاربر دیکشنری باشد
                if isinstance(user_answer, dict):
                    # پیمایش روی جواب صحیح (solution)
                    # در اینجا solution به صورت { zone_id: correct_option_id } است
                    for zone_id, correct_option_id in solution.items():
                        user_selected_option_id = user_answer.get(zone_id)
                        
                        # مقایسه جواب کاربر با جواب صحیح
                        if user_selected_option_id == correct_option_id:
                            feedback[zone_id] = 'correct'
                            score_earned += points_per_correct
                        else:
                            feedback[zone_id] = 'incorrect'
                            all_correct = False
                else:
                    all_correct = False
                    feedback = {}
                    score_earned = 0
                is_correct = all_correct
                
            # منطق خاص برای سوال ceftriaxone
            if question.get('id') == 'ceftriaxone_calcium_admin' and 'solution_reversed' in question:
                 solution_reversed = question.get('solution_reversed')
                 all_correct = True
                 feedback = {}
                 score_earned = 0
                 
                 if isinstance(user_answer, dict):
                    for category_id, correct_item_id in solution_reversed.items():
                        user_item_id = user_answer.get(category_id)
                        if user_item_id == correct_item_id:
                            feedback[category_id] = 'correct'
                            score_earned += points_per_correct
                        else:
                            feedback[category_id] = 'incorrect'
                            all_correct = False
                 else:
                     all_correct = False
                 is_correct = all_correct

        except Exception as e:
            print(f"Error calculating score: {e}")
            return 0, False, {}
            
        score_earned = math.ceil(score_earned) if score_earned > 0 else 0
        return score_earned, is_correct, feedback

    # --- متد کمکی: محاسبه سطح ---
    def _calculate_level(self, score):
        # هر 200 امتیاز یک سطح (با توجه به سیستم جدید امتیازدهی)
        return math.floor(int(score) / 200) + 1

    # --- متد کمکی: بررسی نشان‌ها ---
    def _check_and_award_badges(self, user):
        newly_earned_badges = []
        user_badge_ids = user.get('badges_earned', [])
        
        # دریافت همه نشان‌ها (بدون _id که باعث خطای 500 می‌شود)
        all_badges = list(mongo.db.badges.find({}, {"_id": 0}))
        
        for badge in all_badges:
            badge_id = badge['id']
            if badge_id in user_badge_ids:
                continue
            
            criteria = badge.get('criteria', {})
            criteria_type = criteria.get('type')
            earned = False
            
            if criteria_type == 'reach_score':
                 if int(user.get('score', 0)) >= criteria.get('score', 0): earned = True
            elif criteria_type == 'reach_level':
                 if int(user.get('level', 1)) >= criteria.get('level', 1): earned = True
            elif criteria_type == 'complete_quiz':
                 if int(user.get('quizzes_completed', 0)) >= criteria.get('count', 0): earned = True
            elif criteria_type == 'correct_streak':
                 if int(user.get('correct_streak', 0)) >= criteria.get('count', 0): earned = True

            if earned:
                user_badge_ids.append(badge_id)
                newly_earned_badges.append(badge)
        
        if newly_earned_badges:
            mongo.db.users.update_one(
                {'_id': user['_id']},
                {'$set': {'badges_earned': user_badge_ids}}
            )
            
        return newly_earned_badges

    @jwt_required()
    def post(self):
        data = request.get_json()
        quiz_id = data.get('quizId')
        question_id = data.get('questionId')
        user_answer = data.get('answer')
        is_last_question = data.get('isLastQuestion', False)
        time_taken = data.get('timeTaken', 30)

        if not question_id or user_answer is None or not quiz_id:
            return {"message": "اطلاعات ناقص است"}, 400

        # ۱. پیدا کردن سوال
        quiz = mongo.db.quizzes.find_one({"id": quiz_id})
        if not quiz: return {"message": "آزمون یافت نشد"}, 404
        question = next((q for q in quiz['questions'] if q['id'] == question_id), None)
        if not question: return {"message": "سوال یافت نشد"}, 404

        # ۲. محاسبه امتیاز پایه
        base_score, is_correct, feedback = self._calculate_score(question, user_answer)
        
        # ۳. محاسبه پاداش‌ها
        speed_bonus = 0
        streak_bonus = 0
        
        current_user_username = get_jwt_identity()
        user = mongo.db.users.find_one({'username': current_user_username})
        
        current_streak = user.get('correct_streak', 0)
        new_streak = current_streak + 1 if is_correct else 0

        if is_correct:
            # الف) پاداش سرعت
            if time_taken < 5: speed_bonus = 5
            elif time_taken < 10: speed_bonus = 4
            elif time_taken < 15: speed_bonus = 3
            elif time_taken < 20: speed_bonus = 2
            
            # ب) پاداش استریک (هر ۵ تا یکی)
            if new_streak > 0 and new_streak % 5 == 0:
                streak_bonus = 20

        total_question_score = base_score + speed_bonus + streak_bonus

        # ۴. آپدیت سوابق و پروفایل
        quiz_progress = user.get('quiz_progress', {})
        if quiz_id not in quiz_progress:
            quiz_progress[quiz_id] = {'best_score': 0, 'current_session_score': 0, 'attempts': 0}
        
        user_quiz_data = quiz_progress[quiz_id]
        user_quiz_data['current_session_score'] = user_quiz_data.get('current_session_score', 0) + total_question_score
        
        current_total_score = int(user.get('score', 0))
        xp_gained_this_step = 0
        
        if is_last_question:
            previous_best = user_quiz_data.get('best_score', 0)
            new_session_score = user_quiz_data['current_session_score']
            
            if new_session_score > previous_best:
                xp_gained_this_step = new_session_score - previous_best
                user_quiz_data['best_score'] = new_session_score
            
            user_quiz_data['attempts'] = user_quiz_data.get('attempts', 0) + 1
            user_quiz_data['current_session_score'] = 0 # ریست
            
            mongo.db.users.update_one({'_id': user['_id']}, {'$inc': {'quizzes_completed': 1}})

        quiz_progress[quiz_id] = user_quiz_data
        
        new_total_score = current_total_score + xp_gained_this_step
        new_level = self._calculate_level(new_total_score)
        level_up_occurred = new_level > user.get('level', 1)

        mongo.db.users.update_one(
            {'_id': user['_id']},
            {
                '$set': {
                    'score': new_total_score,
                    'level': new_level,
                    'correct_streak': new_streak,
                    'quiz_progress': quiz_progress
                }
            }
        )

        updated_user = mongo.db.users.find_one({'_id': user['_id']})
        newly_earned_badges = self._check_and_award_badges(updated_user)
        
        # استخراج متن توضیحات
        explanation_text = question.get('explanation', '')

        return {
            "message": "جواب ثبت شد",
            "isCorrect": is_correct,
            "feedback": feedback,
            "scoreEarned": total_question_score,
            "xpGained": xp_gained_this_step,
            "speedBonus": speed_bonus,
            "streakBonus": streak_bonus,
            "newTotalScore": new_total_score,
            "newLevel": new_level,
            "levelUp": level_up_occurred,
            "newlyEarnedBadges": newly_earned_badges,
            "explanation": explanation_text
        }, 200