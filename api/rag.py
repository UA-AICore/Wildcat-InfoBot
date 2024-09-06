import openai
import faiss
import numpy as np
from api.embedding import get_embeddings
from api.model import setup_openai

openai.api_key = setup_openai()

# FAISS index
def create_faiss_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype('float32'))
    return index

# RAG
def perform_rag(query, documents, index, model="gpt-4o"):
    query_embedding = get_embeddings([query], model="text-embedding-3-large")[0]
    
    # top 3
    D, I = index.search(np.array([query_embedding]).astype('float32'), 3)
    relevant_docs = [documents[i] for i in I[0]]

    # relevant documents into a prompt
    combined_prompt = f"Using the following documents, answer this question:\n{relevant_docs}\nQuestion: {query}"

    # response
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": combined_prompt}],
        max_tokens=400
    )
    
    # Return the answer
    return response.choices[0].message['content'].strip()


