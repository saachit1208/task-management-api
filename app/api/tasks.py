"""
Task API Routes Module

This module contains the API endpoints for task operations:
- GET /tasks: Retrieve all tasks
- POST /tasks: Create a new task
- DELETE /tasks/{id}: Delete a specific task

Each endpoint includes error handling and proper HTTP status codes.
"""

from flask import Blueprint, request, jsonify
from http import HTTPStatus
from marshmallow import ValidationError
from ..extensions import db
from ..models.task import Task
from ..schemas.task import task_schema, tasks_schema

tasks = Blueprint('tasks', __name__)

@tasks.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        all_tasks = Task.query.order_by(Task.created_at.desc()).all()
        # Use marshmallow schema to serialize
        result = tasks_schema.dump(all_tasks)
        return result, HTTPStatus.OK
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@tasks.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    try:
        # Use marshmallow schema to deserialize and validate
        task = task_schema.load(request.json)
        
        # Save to database
        db.session.add(task)
        db.session.commit()
        
        # Return serialized task
        return task_schema.dump(task), HTTPStatus.CREATED
        
    except ValidationError as err:
        return jsonify({'error': err.messages}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@tasks.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    try:
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'error': 'Task not found'}), HTTPStatus.NOT_FOUND
            
        db.session.delete(task)
        db.session.commit()
        
        return  jsonify({'message': 'Task deleted successfully'}), HTTPStatus.OK
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR