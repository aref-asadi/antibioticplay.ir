from flask import Flask, send_from_directory, render_template
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

    from .routes import auth_bp, quiz_bp, leaderboard_bp, badge_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(quiz_bp, url_prefix='/api/quizzes')
    app.register_blueprint(leaderboard_bp, url_prefix='/api/leaderboard')
    app.register_blueprint(badge_bp, url_prefix='/api/badges')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_vue(path):
        if path and os.path.exists(os.path.join(dist_folder, path)):
            return send_from_directory(dist_folder, path)
        return render_template('index.html')

    return app