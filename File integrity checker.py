import hashlib
import os

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def check_integrity(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Directory '{directory_path}' does not exist or is not a directory")
        return

    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            calculated_hash = calculate_sha256(filepath)
            print(f"File: {filepath}\nSHA-256 HASH: {calculated_hash}")

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path: ")
    check_integrity(directory_to_check)
