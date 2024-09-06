# Mr. Minglai Yang's project

from api.rag import perform_rag, create_faiss_index
from api.embedding import get_embeddings
import os

# Function to read files from rawdata directory
def read_files_from_rawdata(directory):
    documents = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Assuming the files are text files
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                documents.append(file.read())
            filenames.append(filename)
    return documents, filenames

if __name__ == "__main__":
    rawdata_directory = "rawdata"
    documents, filenames = read_files_from_rawdata(rawdata_directory)
    embeddings = get_embeddings(documents)
    faiss_index = create_faiss_index(embeddings)

    
    

    # Testing
    query = "Tell me about Arizona"
    # RAG
    answer = perform_rag(query, documents, faiss_index)
    print("Generated answer:", answer)
