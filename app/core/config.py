import os

class Settings:
    DATABASE_URL = os.getenv('DATABASE_URL')
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:5173')

settings = Settings()