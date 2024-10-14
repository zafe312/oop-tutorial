# utils.py
import json

def print_with_borders(message):
    """Prints a message with borders around it."""
    border = '=' * len(message)
    print(f"{border}\n{message}\n{border}")

def read_json(file_path):
    """Reads data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def log_to_file(message, filename='log.txt'):
    """Logs a message to a specified file."""
    with open(filename, 'a') as log_file:
        log_file.write(f"{message}\n")
