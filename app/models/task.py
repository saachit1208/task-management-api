"""
Task Model Module

Defines the Task database model using SQLAlchemy.
Includes the following fields:
- id: Primary key
- description: Task description
- created_at: Timestamp of creation
"""
from datetime import datetime
from ..extensions import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}: {self.description[:20]}...>'