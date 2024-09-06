import json

# Function to save questions and answers to a JSON file
def save_to_json(data, json_file="qa_log.json"):
    try:
        with open(json_file, 'r') as file:
            qa_log = json.load(file)
    except FileNotFoundError:
        qa_log = []  # Create new file

    qa_log.append(data)

    with open(json_file, 'w') as file:
        json.dump(qa_log, file, indent=4)  # save log
