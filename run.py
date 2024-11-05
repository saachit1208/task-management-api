from dotenv import load_dotenv

# Load environment variables once at startup
load_dotenv()

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)