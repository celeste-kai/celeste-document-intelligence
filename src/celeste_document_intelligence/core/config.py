import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
