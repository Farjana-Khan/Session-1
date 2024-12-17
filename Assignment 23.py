#Assignment 23: Create a log file writer that appends log messages to a file with timestamps.

import os
from datetime import datetime

def write_log(message):
    """
    Appends a log message with a timestamp to the log file.
    """
    # Ensure the directory exists
    log_dir = 'data'
    os.makedirs(log_dir, exist_ok=True)  # Create the 'data' directory if it doesn't exist
    
    # Construct the log file path
    log_file_path = os.path.join(log_dir, 'logs.txt')
    
    # Append the log entry
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - {message}\n"
    
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_entry)
    print(f"Log added: {log_entry.strip()}")

# Example usage
write_log("Server started.")
write_log("User login: bob@example.com.")
write_log("Error: Database connection failed.")

