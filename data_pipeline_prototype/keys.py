import os
from dotenv import load_dotenv

# load environment variables from .env file

load_dotenv()

# get API key from environment variables

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')