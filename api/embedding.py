import openai
from .model import setup_openai

# Setup the OpenAI API key
openai.api_key = setup_openai()

# Function to create embeddings for file contents
def get_embeddings(texts, model="text-embedding-3-large"):
    response = openai.Embedding.create(
        model=model,
        input=texts
    )
    return [embedding['embedding'] for embedding in response['data']]
