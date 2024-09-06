# Mr. Minglai Yang's project

# ============================= Here I pass these tests ======================================
'''
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
    query = "arizona events in April"
    # RAG
    answer = perform_rag(query, documents, faiss_index)
    print("Generated answer:", answer)
'''
# ==========================================================================================




# Update start from here


from api.rag import perform_rag, create_faiss_index
from api.embedding import get_embeddings
from utils.file_handler import read_html_files_from_rawdata
from utils.qna_manager import save_to_json

if __name__ == "__main__":
    # Directory containing the raw HTML data
    rawdata_directory = "rawdata"
    
    # Read documents from rawdata directory
    documents, filenames = read_html_files_from_rawdata(rawdata_directory)

    # Generate embeddings for documents
    embeddings = get_embeddings(documents)

    # Create FAISS index from embeddings
    faiss_index = create_faiss_index(embeddings)

    print("Ready for Q&A session. Type your questions below:")
    
    while True:
        query = input("\nEnter your question (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Exiting Q&A session.")
            break

        answer = perform_rag(query, documents, faiss_index)

        print(f"Answer: {answer}")
        
        qa_entry = {"question": query, "answer": answer}
        save_to_json(qa_entry)
        print("Question and answer saved to qa_log.json.")
