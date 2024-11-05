"""
Test Configuration Module with session-level cleanup
"""

import pytest
from app import create_app
from app.extensions import db
from app.models.task import Task

@pytest.fixture(scope='session')
def app():
    """Create and configure Flask application for testing"""
    test_db_url = "postgresql://postgres:postgres@localhost:5432/tasks_test_db"
    app = create_app(database_url=test_db_url)
    app.config['TESTING'] = True
    
    print(f"\n[DEBUG] Test Database URL: {app.config['SQLALCHEMY_DATABASE_URI']}")
    
    # Setup test database
    with app.app_context():
        db.create_all()
        print("\n[DEBUG] Test database tables created")
    
    yield app
    
    # Cleanup after all tests are done
    with app.app_context():
        print("\n[DEBUG] Cleaning up test database...")
        db.session.remove()
        db.drop_all()
        print("[DEBUG] Test database cleaned up")

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def init_database(app):
    """Initialize database with sample data"""
    with app.app_context():
        # Create sample tasks
        task1 = Task(description="Test task 1")
        task2 = Task(description="Test task 2")
        db.session.add_all([task1, task2])
        db.session.commit()
        
        yield db