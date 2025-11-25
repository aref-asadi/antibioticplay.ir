from flask_restful import Resource
from app import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity

class AllBadges(Resource):
    @jwt_required()
    def get(self):
        try:
            all_badges = list(mongo.db.badges.find({}, {"_id": 0}))
            return all_badges, 200
        except Exception as e:
            return {"message": str(e)}, 500

class EarnedBadges(Resource):
    @jwt_required()
    def get(self):
        current_user_username = get_jwt_identity()
        user = mongo.db.users.find_one({'username': current_user_username})

        if not user:
            return {"message": "User not found"}, 404

        earned_badge_ids = user.get('badges_earned', [])

        earned_badges = list(mongo.db.badges.find(
            {'id': {'$in': earned_badge_ids}},
            {"_id": 0}
        ))

        return earned_badges, 200