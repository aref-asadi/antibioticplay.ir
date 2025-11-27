from flask import Flask, send_from_directory, render_template, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
import os

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    dist_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dist'))
    
    app = Flask(__name__, static_folder=f"{dist_folder}/assets", template_folder=dist_folder)
    
    app.config.from_object(Config)
    CORS(app)
    mongo.init_app(app)
    jwt.init_app(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'message': 'The token has expired.',
            'error': 'token_expired'
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'message': 'Signature verification failed.',
            'error': 'invalid_token'
        }), 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            'message': 'Request does not contain an access token.',
            'error': 'authorization_required'
        }), 401

    from .routes import auth_bp, quiz_bp, leaderboard_bp, badge_bp, bookmarks_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(quiz_bp, url_prefix='/api/quizzes')
    app.register_blueprint(leaderboard_bp, url_prefix='/api/leaderboard')
    app.register_blueprint(badge_bp, url_prefix='/api/badges')
    app.register_blueprint(bookmarks_bp, url_prefix='/api/bookmarks')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_vue(path):
        if path and os.path.exists(os.path.join(dist_folder, path)):
            return send_from_directory(dist_folder, path)
        return render_template('index.html')

    return app