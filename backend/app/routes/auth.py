# File: backend/app/routes/auth.py
from flask import Blueprint, request, jsonify
from app.models.user import User
from app import mongo
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    avatar_id = data.get('avatar_id', 'fleming')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = User.create_user(username, password, email, avatar_id)
    
    if not user:
        return jsonify({"message": "Username or email already exists"}), 400

    access_token = create_access_token(identity=username)
    
    return jsonify({
        "message": "User registered successfully",
        "token": access_token,
        "user": user.to_dict()
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
         return jsonify({"message": "Username and password are required"}), 400

    user_data = User.find_by_username(username)
    
    if not user_data:
         return jsonify({"message": "Invalid credentials"}), 401
    
    if not User.check_password(user_data['password_hash'], password):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    response_user = {
        "username": user_data['username'],
        "email": user_data.get('email'),
        "level": user_data.get('level', 1),
        "xp": user_data.get('xp', 0),
        "total_score": user_data.get('total_score', 0),
        "badges": user_data.get('badges', []),
        "correct_streak": user_data.get('correct_streak', 0),
        "avatar_id": user_data.get('avatar_id', 'fleming'),
        "league": User.get_league_info(user_data.get('total_score', 0))
    }

    return jsonify({
        "token": access_token,
        "user": response_user
    }), 200

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_username = get_jwt_identity()
    user_data = User.find_by_username(current_username)
    
    if not user_data:
        return jsonify({"message": "User not found"}), 404
    
    response_user = {
        "username": user_data['username'],
        "email": user_data.get('email'),
        "level": user_data.get('level', 1),
        "xp": user_data.get('xp', 0),
        "total_score": user_data.get('total_score', 0),
        "badges": user_data.get('badges', []),
        "correct_streak": user_data.get('correct_streak', 0),
        "avatar_id": user_data.get('avatar_id', 'fleming'),
        "league": User.get_league_info(user_data.get('total_score', 0))
    }
    return jsonify(response_user), 200

@auth_bp.route('/update-avatar', methods=['POST'])
@jwt_required()
def update_avatar():
    current_username = get_jwt_identity()
    data = request.get_json()
    new_avatar_id = data.get('avatar_id')

    if not new_avatar_id:
        return jsonify({"message": "Avatar ID is required"}), 400

    mongo.db.users.update_one(
        {"username": current_username},
        {"$set": {"avatar_id": new_avatar_id}}
    )

    return jsonify({"message": "Avatar updated successfully", "avatar_id": new_avatar_id}), 200