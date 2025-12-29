import os
from dotenv import load_dotenv

load_dotenv("data/.env")
api_key = os.getenv("API_KEY")
