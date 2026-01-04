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
                    is_locked = not unlock_next
                    
                    unit_data["levels"].append({
                        "id": quiz_id,
                        "title": quiz_info["title"],
                        "icon": quiz_info.get("icon", "star"),
                        "is_completed": is_completed,
                        "is_locked": is_locked,
                        "total_questions": len(quiz_info["questions"])
                    })
                    
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
    
    def _calculate_score(self, question, user_answer):
        question_type = question.get('type')
        solution = question.get('solution')
        points_total = question.get('points_per_correct', 10) 
        
        score_earned = 0
        is_correct = False
        feedback = {}
        
        try:
            # --- FIX: اصلاح منطق درگ اند دراپ ---
            if question_type in ["drag-drop-match", "drag-drop-ordering"]:
                # ۱. محاسبه تعداد کل آیتم‌های موجود در پاسخنامه (نه تعداد دسته‌ها)
                total_items_count = sum(len(items) for items in solution.values())
                points_per_item = points_total / total_items_count if total_items_count > 0 else 0
                
                correct_matches_count = 0
                
                # ۲. پیمایش روی دسته‌بندی‌های پاسخنامه
                # cat_id: شناسه دسته (مثلاً cat_clav)
                # correct_item_ids: لیست آیتم‌های درستی که باید در این دسته باشند
                for cat_id, correct_item_ids in solution.items():
                    
                    # گرفتن لیست آیتم‌هایی که کاربر در این دسته قرار داده
                    # اگر کاربر چیزی نذاشته بود، لیست خالی برگردان
                    user_items_in_cat = user_answer.get(cat_id, []) if isinstance(user_answer, dict) else []
                    
                    # استخراج ID آیتم‌های کاربر (چون فرانت‌اند معمولاً آبجکت کامل می‌فرستد)
                    user_item_ids = []
                    if isinstance(user_items_in_cat, list):
                        for ui in user_items_in_cat:
                            if isinstance(ui, dict):
                                user_item_ids.append(ui.get('id'))
                            else:
                                user_item_ids.append(ui) # اگر فقط ID فرستاده بود
                    
                    # ۳. بررسی صحت آیتم‌ها
                    for c_item_id in correct_item_ids:
                        if c_item_id in user_item_ids:
                            feedback[c_item_id] = 'correct'
                            score_earned += points_per_item
                            correct_matches_count += 1
                        else:
                            feedback[c_item_id] = 'incorrect'
                            
                # اگر همه آیتم‌ها درست جایگذاری شده بودند
                is_correct = (correct_matches_count == total_items_count)

            elif question_type == "multiple-select":
                if isinstance(user_answer, list):
                    user_selections = set(user_answer)
                    correct_selections = set(solution)
                    
                    correct_hits = user_selections.intersection(correct_selections)
                    wrong_hits = user_selections.difference(correct_selections)
                    
                    points_per_option = points_total / len(correct_selections) if len(correct_selections) > 0 else 0
                    
                    current_score = (len(correct_hits) * points_per_option) - (len(wrong_hits) * points_per_option)
                    score_earned = max(0, current_score)
                    
                    is_correct = (user_selections == correct_selections)
                    
                    all_options = [opt['id'] for opt in question.get('options', [])]
                    for opt_id in all_options:
                        if opt_id in correct_selections:
                             feedback[opt_id] = 'correct'
                        else:
                             feedback[opt_id] = 'incorrect'

                else:
                    is_correct = False

            elif question_type == "true-false":
                statements = question.get('statements', [])
                total_stmts = len(statements)
                points_per_stmt = points_total / total_stmts if total_stmts > 0 else 0
                
                correct_count = 0
                if isinstance(user_answer, dict):
                    for stmt in statements:
                        stmt_id = stmt['id']
                        expected = stmt['solution']
                        actual = user_answer.get(stmt_id)
                        
                        if actual == expected:
                            feedback[stmt_id] = 'correct'
                            score_earned += points_per_stmt
                            correct_count += 1
                        else:
                            feedback[stmt_id] = 'incorrect'
                
                is_correct = (correct_count == total_stmts)

            elif question_type == "drag-drop-fill":
                blanks = question.get('blanks', [])
                total_blanks = len(blanks)
                points_per_blank = points_total / total_blanks if total_blanks > 0 else 0
                
                correct_count = 0
                if isinstance(user_answer, dict):
                    for blank in blanks:
                        b_id = blank['id']
                        expected = blank['solution_id']
                        actual = user_answer.get(b_id)
                        
                        if actual == expected:
                            feedback[b_id] = 'correct'
                            score_earned += points_per_blank
                            correct_count += 1
                        else:
                            feedback[b_id] = 'incorrect'
                
                is_correct = (correct_count == total_blanks)

            elif question_type == "image-labeling":
                total_zones = len(solution.keys())
                points_per_zone = points_total / total_zones if total_zones > 0 else 0
                correct_zones_count = 0
                
                if isinstance(user_answer, dict):
                    for zone_id, correct_vals in solution.items():
                        if not isinstance(correct_vals, list):
                            correct_vals = [correct_vals]
                        
                        user_vals = user_answer.get(zone_id, [])
                        if not isinstance(user_vals, list):
                            user_vals = []
                            
                        # استخراج ID ها برای مقایسه دقیق
                        user_val_ids = []
                        for val in user_vals:
                            if isinstance(val, dict): user_val_ids.append(val.get('id'))
                            else: user_val_ids.append(val)

                        if set(user_val_ids) == set(correct_vals):
                            feedback[zone_id] = 'correct'
                            score_earned += points_per_zone
                            correct_zones_count += 1
                        else:
                            feedback[zone_id] = 'incorrect'
                
                is_correct = (correct_zones_count == total_zones)

            # هک خاص برای سوال سفتریاکسون (در صورت وجود)
            if question.get('id') == 'ceftriaxone_calcium_admin' and 'solution_reversed' in question:
                 sol_rev = question.get('solution_reversed')
                 score_earned = 0
                 points_per_cat = points_total / len(sol_rev) if len(sol_rev) > 0 else 0
                 correct_cnt = 0
                 
                 if isinstance(user_answer, dict):
                    for cat_id, correct_item in sol_rev.items():
                        user_item = user_answer.get(cat_id)
                        # هندل کردن اگر آبجکت باشد
                        if isinstance(user_item, dict): user_item = user_item.get('id')
                        
                        if user_item == correct_item:
                            feedback[cat_id] = 'correct'
                            score_earned += points_per_cat
                            correct_cnt += 1
                        else:
                            feedback[cat_id] = 'incorrect'
                    is_correct = (correct_cnt == len(sol_rev))

        except Exception as e:
            print(f"Error calculating score: {e}")
            return 0, False, {}
            
        score_earned = math.ceil(score_earned) if score_earned > 0 else 0
        return score_earned, is_correct, feedback

    def _calculate_level(self, score):
        return math.floor(int(score) / 200) + 1

    def _check_and_award_badges(self, user):
        newly_earned_badges = []
        user_badge_ids = user.get('badges_earned', [])
        all_badges = list(mongo.db.badges.find({}, {"_id": 0}))
        
        for badge in all_badges:
            badge_id = badge['id']
            if badge_id in user_badge_ids: continue
            
            criteria = badge.get('criteria', {})
            ctype = criteria.get('type')
            earned = False
            
            if ctype == 'reach_score' and int(user.get('score', 0)) >= criteria.get('score', 0): earned = True
            elif ctype == 'reach_level' and int(user.get('level', 1)) >= criteria.get('level', 1): earned = True
            elif ctype == 'complete_quiz' and int(user.get('quizzes_completed', 0)) >= criteria.get('count', 0): earned = True
            elif ctype == 'correct_streak' and int(user.get('correct_streak', 0)) >= criteria.get('count', 0): earned = True

            if earned:
                user_badge_ids.append(badge_id)
                newly_earned_badges.append(badge)
        
        if newly_earned_badges:
            mongo.db.users.update_one({'_id': user['_id']}, {'$set': {'badges_earned': user_badge_ids}})
            
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

        quiz = mongo.db.quizzes.find_one({"id": quiz_id})
        if not quiz: return {"message": "آزمون یافت نشد"}, 404
        
        questions_list = quiz['questions']
        question = next((q for q in questions_list if q['id'] == question_id), None)
        if not question: return {"message": "سوال یافت نشد"}, 404
        
        question_index = next((i for i, q in enumerate(questions_list) if q['id'] == question_id), -1)

        base_score, is_correct, feedback = self._calculate_score(question, user_answer)
        
        speed_bonus = 0
        streak_bonus = 0
        
        current_user_username = get_jwt_identity()
        user = mongo.db.users.find_one({'username': current_user_username})
        
        current_streak = user.get('correct_streak', 0)
        new_streak = current_streak + 1 if is_correct else 0

        if is_correct:
            if time_taken < 5: speed_bonus = 5
            elif time_taken < 10: speed_bonus = 4
            elif time_taken < 15: speed_bonus = 3
            elif time_taken < 20: speed_bonus = 2
            
            if new_streak > 0 and new_streak % 5 == 0:
                streak_bonus = 20

        total_question_score = base_score + speed_bonus + streak_bonus

        quiz_progress = user.get('quiz_progress', {})
        if quiz_id not in quiz_progress:
            quiz_progress[quiz_id] = {'best_score': 0, 'current_session_score': 0, 'attempts': 0, 'current_session_correct_count': 0}
        
        user_quiz_data = quiz_progress[quiz_id]
        
        if question_index == 0:
            user_quiz_data['current_session_score'] = 0
            user_quiz_data['current_session_correct_count'] = 0
            user_quiz_data['attempts'] = user_quiz_data.get('attempts', 0) + 1

        user_quiz_data['current_session_score'] = user_quiz_data.get('current_session_score', 0) + total_question_score
        
        if is_correct:
            user_quiz_data['current_session_correct_count'] = user_quiz_data.get('current_session_correct_count', 0) + 1

        current_total_score = int(user.get('score', 0))
        xp_gained_this_step = 0
        stage_completed_perfectly = False
        
        if is_last_question:
            previous_best = user_quiz_data.get('best_score', 0)
            final_session_score = user_quiz_data['current_session_score']
            
            if final_session_score > previous_best:
                xp_gained_this_step = final_session_score - previous_best
                user_quiz_data['best_score'] = final_session_score
            
            total_qs = len(questions_list)
            correct_cnt = user_quiz_data.get('current_session_correct_count', 0)
            
            if correct_cnt == total_qs:
                stage_completed_perfectly = True
            
            if final_session_score > 0:
                 mongo.db.users.update_one({'_id': user['_id']}, {'$addToSet': {'completed_quizzes': quiz_id}, '$inc': {'quizzes_completed': 1}})

            user_quiz_data['current_session_score'] = 0
            user_quiz_data['current_session_correct_count'] = 0

        quiz_progress[quiz_id] = user_quiz_data
        
        new_total_score = current_total_score + xp_gained_this_step
        new_level = self._calculate_level(new_total_score)
        level_up = new_level > user.get('level', 1)

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
            "levelUp": level_up,
            "newlyEarnedBadges": newly_earned_badges,
            "explanation": question.get('explanation', ''),
            "stageCompleted": stage_completed_perfectly
        }, 200