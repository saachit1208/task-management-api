from sqlalchemy import create_engine
import os


# Get database URL from environment
DATABASE_URL = os.getenv('TEST_DATABASE_URL')

try:
    # Try to create engine and connect
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("Successfully connected to the database!")
except Exception as e:
    print("Failed to connect to the database.")
    print(f"Error: {str(e)}")