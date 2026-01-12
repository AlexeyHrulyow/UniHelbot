import os
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("API_KEY")
