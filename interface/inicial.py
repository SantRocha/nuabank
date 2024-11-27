import tkinter as tk
from tkinter import ttk, messagebox
from interface.janela_banco import Janela_Banco  
from PIL import ImageTk, Image
import sys
import os

class Janela_Inicial:
    def __init__(self, master):
        self.janela_inicial = master
        self.janela_inicial.title("NUA BANK")
        self.janela_inicial.geometry("500x400")
        self.janela_inicial.configure(bg="#F18A01") 

        # Use resource_path para garantir que o arquivo de imagem seja encontrado
        self.logo = Image.open(self.resource_path("interface/nua.jpg"))
        self.logo = self.logo.resize((200, 200))  
        self.logo_tk = ImageTk.PhotoImage(self.logo)

        # Label para a imagem
        self.label_logo = ttk.Label(self.janela_inicial, image=self.logo_tk)
        self.label_logo.pack(pady=10)
        
        # Labels para senha
        self.label_senha = ttk.Label(self.janela_inicial, text="Código de acesso:", font=("Arial", 18, "bold"), foreground="white", background="#F18A01")
        
        # Campo de entrada para senha
        self.entry_senha = ttk.Entry(self.janela_inicial, show="*")
        self.entry_senha.bind('<Return>', self.verificar_login)
        
        # Botão de login
        self.btn_login = ttk.Button(self.janela_inicial, text="Entrar", command=self.verificar_login)
        
        # Layout
        self.label_senha.pack()
        self.entry_senha.pack()
        self.btn_login.pack()

        self.janela_inicial.mainloop()

    def resource_path(self, relative_path):
        """Obtenha o caminho absoluto do recurso, usando PyInstaller"""
        try:
            base_path = sys._MEIPASS  # Caminho temporário do executável PyInstaller
        except AttributeError:
            base_path = os.path.abspath(".")  # Caminho local durante o desenvolvimento
        return os.path.join(base_path, relative_path)

    def verificar_login(self, event=None):
        senha = self.entry_senha.get()

        # Lógica de autenticação
        if senha == "123":
            self.janela_inicial.destroy()  # Destrói a janela de login
            Janela_Banco(self.janela_inicial)  # Passa a janela principal existente para a janela do banco
        else:
            messagebox.showerror("Erro", "Código de acesso inválido.")
