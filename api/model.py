import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup OpenAI API key
def setup_openai():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key:
        return openai_api_key
    else:
        raise ValueError("OpenAI API key ERROR")
