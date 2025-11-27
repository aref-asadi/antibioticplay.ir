from flask_restful import Resource
from app import mongo
from app.models.user import User
from flask_jwt_extended import jwt_required
import pymongo

class Leaderboard(Resource):
    @jwt_required()
    def get(self):
        try:
            top_users_cursor = mongo.db.users.find(
                {},
                {"username": 1, "score": 1, "_id": 0}
            ).sort("score", pymongo.DESCENDING).limit(10)

            top_users = []
            for user in top_users_cursor:
                user['league'] = User.get_league_info(user.get('score', 0))
                top_users.append(user)

            return top_users, 200

        except Exception as e:
            return {"message": str(e)}, 500