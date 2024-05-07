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

# Decrypt all files in a directory
def decrypt_files_in_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

# Main function
if __name__ == "__main__":
    key = input("Enter the key: ")

    directory_to_decrypt = input("Enter the directory to decrypt: ")
    decrypt_files_in_directory(directory_to_decrypt, key)

    print("Decryption completed. Your files are now accessible.")
