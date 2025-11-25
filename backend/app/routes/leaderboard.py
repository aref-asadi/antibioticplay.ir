from flask_restful import Resource
from app import mongo
from flask_jwt_extended import jwt_required
import pymongo

class Leaderboard(Resource):
    @jwt_required()
    def get(self):
        try:
            top_users = mongo.db.users.find(
                {},
                {"username": 1, "score": 1, "_id": 0}
            ).sort(
                "score", pymongo.DESCENDING
            ).limit(10)

            return list(top_users), 200

        except Exception as e:
            return {"message": str(e)}, 500