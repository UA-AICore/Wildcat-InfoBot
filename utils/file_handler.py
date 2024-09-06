import os
from bs4 import BeautifulSoup

def read_html_files_from_rawdata(directory):
    documents = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".html"):  # read only HTML files
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'lxml')  # take HTML content
                text = soup.get_text()  # HTML -> TXT
                documents.append(text)
                filenames.append(filename)
    return documents, filenames
