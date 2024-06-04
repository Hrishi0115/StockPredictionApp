import os
from dotenv import load_dotenv

# load environment variables from .env file

load_dotenv()

# get API key from environment variables
database = os.getenv('DB_NAME')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST', 'localhost')  # Use 'localhost' as default if not set
port = os.getenv('DB_PORT', '5432')       # Use '5432' as default if not set