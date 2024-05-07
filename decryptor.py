from cryptography.fernet import Fernet
import os

# Decrypt a file
def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Decrypt all
def decrypt_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            decrypt_directory(dir_path, key)

# Main function
if __name__ == "__main__":
    key = input("Enter the key: ")
    documents_directory = os.path.join(os.path.expanduser("~"), "Documents")
    decrypt_directory(documents_directory, key)
    print("Decryption completed. Your files are now accessible.")
