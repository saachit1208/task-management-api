from flask import Flask
from .extensions import db, ma, cors
from .api.tasks import tasks
from .core.config import settings

def create_app(database_url=None):
    app = Flask(__name__)
    
    # Configure Flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or settings.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app, resources={
        r"/api/*": {
            "origins": [
                settings.CORS_ORIGINS
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