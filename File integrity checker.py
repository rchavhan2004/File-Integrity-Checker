import hashlib
import os

def calculate_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def check_file_integrity(original_file, modified_file):
    original_hash = calculate_hash(original_file)
    modified_hash = calculate_hash(modified_file)

    if original_hash and modified_hash:
        if original_hash == modified_hash:
            print("Files are identical.")
        else:
            print("Files have been modified.")
    else:
        print("Unable to calculate hash for one or both files.")

# Example usage
original_file_path = 'path_to_original_file.txt'
modified_file_path = 'path_to_modified_file.txt'
check_file_integrity(original_file_path, modified_file_path)
