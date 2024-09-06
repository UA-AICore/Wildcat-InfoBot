import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# OpenAI API key
def setup_openai():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key:
        return openai_api_key
    else:
        raise ValueError("OpenAI API key not found. Please set it in the .env file.")
