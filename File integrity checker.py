# Import libraries

import hashlib
import os

# Function to calculate the SHA-256 hash of a given file
def calculate_sha256(filepath):
    """
    Computes the SHA-256 hash of the file at the given filepath.
    """
    sha256_hash = hashlib.sha256()  # Initialize SHA-256 hash object
    with open(filepath, "rb") as f:  # Open file in binary read mode
        while True:
            data = f.read(65536)  # Read the file in chunks of 64KB
            if not data:  # Stop if the end of the file is reached
                break
            sha256_hash.update(data)  # Update the hash with the chunk
    return sha256_hash.hexdigest()  # Return the computed hash in hexadecimal

# Function to check the integrity of files in a directory
def check_integrity(directory_path):
    """
    Walks through the directory and calculates the SHA-256 hash of each file.
    """
    # Check if the given path exists and is a directory
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Directory '{directory_path}' does not exist or is not a directory")
        return

    # Traverse the directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for filename in files:  # Iterate through all files
            filepath = os.path.join(root, filename)  # Get the full file path
            calculated_hash = calculate_sha256(filepath)  # Calculate SHA-256 hash
            print(f"File: {filepath}\nSHA-256 HASH: {calculated_hash}")

# Main execution
if __name__ == "__main__":
    directory_to_check = input("Enter the directory path: ")  # Get directory path from the user
    check_integrity(directory_to_check)  # Perform integrity check
