# File: backend/app/routes/badge_routes.py

from flask_restful import Resource
from app import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity

class AllBadges(Resource):
    """
    API to get the list of all available badges.
    """
    @jwt_required()
    def get(self):
        try:
            # Fetch all badges, excluding the MongoDB '_id'
            all_badges = list(mongo.db.badges.find({}, {"_id": 0}))
            return all_badges, 200
        except Exception as e:
            return {"message": str(e)}, 500

class EarnedBadges(Resource):
    """
    API to get the list of badges earned by the current user.
    """
    @jwt_required()
    def get(self):
        current_user_username = get_jwt_identity()
        user = mongo.db.users.find_one({'username': current_user_username})

        if not user:
            return {"message": "User not found"}, 404

        earned_badge_ids = user.get('badges_earned', [])

        # Find all badge documents whose 'id' is in the user's earned list
        earned_badges = list(mongo.db.badges.find(
            {'id': {'$in': earned_badge_ids}},
            {"_id": 0} # Exclude MongoDB '_id'
        ))

        return earned_badges, 200