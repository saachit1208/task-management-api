from flask import Flask
from .extensions import db, ma, cors
from .api.tasks import tasks
import os

def create_app(database_url=None):
    app = Flask(__name__)
    
    # Configure Flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app, resources={
        r"/api/*": {
            "origins": [
                "http://localhost:5173",
                "http://127.0.0.1:5173"
            ],
            "methods": ["GET", "POST", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    # Register blueprints
    app.register_blueprint(tasks, url_prefix='/api')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app