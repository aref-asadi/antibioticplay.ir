from flask import request
from flask_restful import Resource
from app import mongo
from app.models.user import User
from flask_jwt_extended import jwt_required
import pymongo

class Leaderboard(Resource):
    """
    API برای دریافت لیست کاربران بر اساس لیگ.
    """
    @jwt_required()
    def get(self):
        try:
            league_name = request.args.get('league', 'diamond').lower()
            
            min_score = 0
            max_score = 999999999
            
            if league_name == 'bronze':
                min_score = 0
                max_score = 500
            elif league_name == 'silver':
                min_score = 501
                max_score = 1000
            elif league_name == 'gold':
                min_score = 1001
                max_score = 2000
            elif league_name == 'diamond':
                min_score = 2001
                max_score = 999999999

            cursor = mongo.db.users.find(
                {"score": {"$gte": min_score, "$lte": max_score}},
                {"username": 1, "score": 1, "first_name": 1, "last_name": 1, "avatar_id": 1, "_id": 0}
            ).sort("score", pymongo.DESCENDING).limit(20)

            leaderboard_data = []
            for user in cursor:
                user['league'] = User.get_league_info(user.get('score', 0))
                user['first_name'] = user.get('first_name', '')
                user['last_name'] = user.get('last_name', '')
                user['avatar_id'] = user.get('avatar_id', 'fleming')
                leaderboard_data.append(user)

            return leaderboard_data, 200

        except Exception as e:
            return {"message": str(e)}, 500