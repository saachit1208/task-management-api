# Task Management API

A Flask REST API for managing tasks with PostgreSQL database.

## Project Structure
```
task-management-api/
├── app/
│   ├── __init__.py          # Flask application factory
│   ├── extensions.py        # Flask extensions (SQLAlchemy, Marshmallow, CORS)
│   ├── models/             
│   │   ├── __init__.py
│   │   └── task.py         # Task model
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── task.py         # Task schema
│   ├── api/
│   │   ├── __init__.py
│   │   └── tasks.py        # Task routes
│   └── core/
│       ├── __init__.py
│       └── config.py       # Configuration settings
├── tests/
│   ├── __init__.py
│   ├── conftest.py         # Test configurations and fixtures
│   └── test_tasks.py       # Task tests
├── .env                    # Environment variables
├── requirements.txt        # Project dependencies
└── run.py                 # Application entry point
```

## Setup Instructions

1. **Create Virtual Environment**
```bash
# Create venv
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Database Setup**
```bash
# Access PostgreSQL
psql -U postgres

# Create databases
CREATE DATABASE tasks_db;
CREATE DATABASE tasks_test_db;

# Exit psql
\q
```

4. **Environment Setup**

Create `.env` file:
```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/tasks_db
TEST_DATABASE_URL = postgresql://postgres:your_password@localhost:5432/tasks_test_db
```
## Running The Application

```bash
# Start the server
python run.py
```
Server runs at `http://127.0.0.1:5000`

## API Endpoints

- `GET /api/tasks`: Get all tasks
- `POST /api/tasks`: Create new task
  ```json
  {
    "description": "Task description"
  }
  ```
- `DELETE /api/tasks/{id}`: Delete task

## Testing

1. **Run Tests**
```bash
# Run all tests
pytest

# Run with output
pytest -v -s

# Run specific test file
pytest tests/test_tasks.py

# Run with coverage
pytest --cov=app tests/
```

2. **Test Database**
- Tests automatically use tasks_test_db database
- Database is cleaned up after tests complete
- Each test runs with fresh data

## Development Notes

### Task Schema
```json
{
    "id": 1,
    "description": "Example task",
    "created_at": "2024-01-01T12:00:00Z"
}
```

### Testing Best Practices
- Write tests for all new features
- Ensure test database is separate from development
- Run tests before committing changes
- Keep tests isolated and independent

### Common Issues

1. **Database Connection**
- Verify PostgreSQL is running
- Check database credentials
- Ensure database exists

2. **Test Database**
- Verify test database exists
- Check test database is clean
- Ensure proper database URL in tests

3. **CORS Issues**
- Frontend URL is configured correctly (default: http://localhost:5173)
- CORS headers are properly set
- Methods are allowed (GET, POST, DELETE)
