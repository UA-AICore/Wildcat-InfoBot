# **Wildcat InfoBot: A Q&A System Using RAG (Retrieval-Augmented Generation)**

**Wildcat InfoBot** is an interactive question-answering (Q&A) system built using **RAG (Retrieval-Augmented Generation)**. It scrapes and reads data from the University of Arizona's website, generates embeddings, retrieves the most relevant documents, and provides answers using OpenAI's GPT-4o model. All questions and answers are saved to a JSON file for future reference.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Folder Structure](#folder-structure)
7. [License](#license)

---

## **Project Overview**

**Wildcat InfoBot** is designed to:
- Scrape the University of Arizona website for relevant content using **Scrapy**.
- Allow users to ask questions interactively via the terminal.
- Parse content from HTML files stored in the `rawdata/` folder.
- Use **Retrieval-Augmented Generation (RAG)** to find relevant documents and generate answers using OpenAI’s GPT-4o model.
- Save all questions and answers to a JSON log for future reference.

---

## **Features**
- **Interactive Q&A**: Type your question in the terminal and get an instant answer based on the data stored in the `rawdata/` folder.
- **Scrapy Integration**: Automatically scrape web pages from the University of Arizona’s website.
- **RAG-Based Document Retrieval**: Uses FAISS to index and retrieve the most relevant documents for a given query.
- **GPT-4o Integration**: Generates answers based on retrieved documents using OpenAI’s powerful GPT-4o model.
- **JSON Logging**: Saves all questions and answers in a JSON file (`qa_log.json`) for easy reference.
- **Automated Data Refresh**: Set up to periodically clean and re-download web pages weekly using the `run.sh` script.

---

## **Requirements**

Before running the project, make sure the following libraries and tools are installed:

- Python 3.8+
- `openai` (for OpenAI API interactions)
- `beautifulsoup4` (for HTML parsing)
- `lxml` (HTML parsing library used with BeautifulSoup)
- `faiss-cpu` (for FAISS similarity search)
- `scrapy` (for web scraping)
- `json` (for saving Q&A data)
- `requests` (if needed for any additional API calls)

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/wildcat-infobot.git
   cd wildcat-infobot
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set OpenAI API Key**:
   - Create a `.env` file in the project root and add your OpenAI API key:
     ```
     OPENAI_API_KEY="your-openai-api-key"
     ```

5. **Prepare Scrapy for Website Scraping**:
   - Ensure `scrapy` is installed.
   - Navigate to the `arizona_edu` folder, which contains the Scrapy project:
     ```bash
     cd arizona_edu
     ```

6. **Running Scrapy to Crawl Data**:
   - Use the following command to start scraping and save all relevant web pages to the `arizona_edu/data/` folder:
     ```bash
     scrapy crawl arizona
     ```

---

## **Usage**

### 1. **Run the Q&A System**:
   - Run the `run.sh` script to update the `rawdata/` folder with the latest web pages from `arizona_edu/data/`:
     ```bash
     ./run.sh
     ```
   - This script will:
     1. Run Scrapy to scrape new data.
     2. Move the data from `arizona_edu/data/` to the `rawdata/` folder.

### 2. **Start the Q&A Session**:
   - Once the data is updated, you can start the Q&A session by running:
     ```bash
     python3 main.py
     ```

   - You will be prompted to type in a question. For example:
     ```bash
     Enter your question (or type 'exit' to quit): What events are happening in Arizona in April?
     ```

   - The system will retrieve the most relevant documents and provide an answer based on the content of the HTML files.

### 3. **Exit the Q&A Session**:
   - Type `exit` to quit the session:
     ```bash
     Enter your question (or type 'exit' to quit): exit
     ```

### 4. **View Logged Q&A**:
   - All questions and answers will be saved in the `qa_log.json` file. You can open this file to view previous interactions.

---

## **Folder Structure**

```bash
.
├── api/                   # API-related code for OpenAI interaction
│   ├── __init__.py
│   ├── embedding.py
│   ├── model.py
│   ├── rag.py
├── utils/                 # Handles file parsing and Q&A management
│   ├── __init__.py
│   ├── file_handler.py    # Extracts text from HTML files
│   ├── qna_manager.py     # Saves Q&A to JSON file
├── arizona_edu/           # Scrapy project folder for crawling UofA site
│   ├── data/              # Folder where scraped web pages (HTML) are saved
├── rawdata/               # Folder containing HTML files moved from Scrapy data
├── .env                   # Environment variables, including API key
├── .gitignore             # Ignoring files and folders (e.g., rawdata)
├── LICENSE                # MIT License
├── README.md              # Project overview and instructions
├── requirements.txt       # List of required Python libraries
├── run.sh                 # Shell script for running the program and updating data
├── main.py                # Main script to execute the program
└── qa_log.json            # Log of all Q&A interactions
```

---

## **License**

This project is licensed under the [**MIT License**](LICENSE). You are free to use, modify, and distribute this software, but you must include the original license and attribution.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
...
