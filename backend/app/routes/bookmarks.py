from flask import request
from flask_restful import Resource
from app import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity

class BookmarkToggle(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        data = request.get_json()
        quiz_id = data.get('quizId')
        question_id = data.get('questionId')

        if not quiz_id or not question_id:
            return {"message": "Invalid data"}, 400

        user = mongo.db.users.find_one({'username': current_user})
        if not user:
            return {"message": "User not found"}, 404

        bookmarks = user.get('bookmarks', [])
        
        existing = next((item for item in bookmarks if item['quiz_id'] == quiz_id and item['question_id'] == question_id), None)

        if existing:
            bookmarks.remove(existing)
            action = 'removed'
        else:
            bookmarks.append({'quiz_id': quiz_id, 'question_id': question_id})
            action = 'added'

        mongo.db.users.update_one(
            {'_id': user['_id']},
            {'$set': {'bookmarks': bookmarks}}
        )

        return {"message": "Success", "action": action, "bookmarks": bookmarks}, 200

class BookmarkList(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = mongo.db.users.find_one({'username': current_user})
        if not user:
            return {"message": "User not found"}, 404

        bookmarks = user.get('bookmarks', [])
        bookmarked_questions = []

        for item in bookmarks:
            quiz = mongo.db.quizzes.find_one({'id': item['quiz_id']})
            if quiz:
                question = next((q for q in quiz['questions'] if q['id'] == item['question_id']), None)
                if question:
                    question['quiz_title'] = quiz['title']
                    question['quiz_id'] = quiz['id']
                    bookmarked_questions.append(question)

        return bookmarked_questions, 200