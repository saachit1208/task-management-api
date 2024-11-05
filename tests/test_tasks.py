"""
Task API Tests

Tests for task-related API endpoints including:
- GET /tasks
- POST /tasks
- DELETE /tasks/{id}
"""

import json
from http import HTTPStatus

def test_get_tasks_empty(client):
    """Test getting tasks when database is empty"""
    response = client.get('/api/tasks')
    assert response.status_code == HTTPStatus.OK
    assert json.loads(response.data) == []

def test_get_tasks(client, init_database):
    """Test getting tasks with pre-populated data"""
    response = client.get('/api/tasks')
    data = json.loads(response.data)
    print(data)
    assert response.status_code == HTTPStatus.OK
    assert len(data) == 2
    

def test_create_task_valid(client):
    """Test creating a task with valid data"""
    response = client.post(
        '/api/tasks',
        json={'description': 'New test task'}
    )
    
    data = json.loads(response.data)
    print(data)
    assert response.status_code == HTTPStatus.CREATED
    assert data['description'] == 'New test task'
    assert 'id' in data
    assert 'created_at' in data

def test_create_task_invalid(client):
    """Test creating a task with invalid data"""
    # Empty description
    response = client.post(
        '/api/tasks',
        json={'description': ''}
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    
    # Missing description
    response = client.post(
        '/api/tasks',
        json={}
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    
    # Description too long (over 500 characters)
    response = client.post(
        '/api/tasks',
        json={'description': 'a' * 501}
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_delete_task_success(client, init_database):
    """Test successful task deletion"""
    # Get first task
    response = client.get('/api/tasks')
    tasks = json.loads(response.data)
    task_id = tasks[0]['id']
    
    # Delete the task
    response = client.delete(f'/api/tasks/{task_id}')
    assert response.status_code == HTTPStatus.OK
    
    data = json.loads(response.data)
    assert data['message'] == 'Task deleted successfully'
   
    
 

def test_delete_task_not_found(client):
    """Test deleting a non-existent task"""
    response = client.delete('/api/tasks/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    
    data = json.loads(response.data)
    assert data['error'] == 'Task not found'