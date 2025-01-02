#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

# Set script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def read_last_entry():
    """
    Read the last entry from the file and extract the timestamp.
    """
    if not os.path.exists('data.txt'):
        return None
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip()
            if last_line.startswith("timestamp:"):
                return last_line.split("timestamp:")[1]
    return None

def append_entry(timestamp):
    """
    Append a new timestamp entry to the file.
    """
    with open('data.txt', 'a') as file:
        file.write(f"timestamp:{timestamp}\n")

def git_commit():
    """
    Stage and commit changes with the current date as the message.
    """
    subprocess.run(['git', 'add', 'data.txt'], check=True)
    commit_message = f"Update timestamp: {datetime.now().strftime('%Y-%m-%d')}"
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)

def main():
    """
    Main function to update the timestamp and commit changes.
    """
    try:
        # Generate the current timestamp
        current_timestamp = datetime.now().isoformat()

        # Append the timestamp to the file
        append_entry(current_timestamp)

        # Commit changes to git
        git_commit()

        print(f"Successfully added timestamp: {current_timestamp}")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
