import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from classes.cliente import Cliente
from classes.banco import Banco

class Janela_Cliente_Read:
    def __init__(self, master, banco, pai, ID_Cliente_Atual, btn_select_cli):
        
        self.banco_Em_Cliente = banco
        self.janelaPai = pai
        self.cliente_atual = ID_Cliente_Atual
        self.btn_select_cli = btn_select_cli

        self.janela_cliente = master
        self.janela_cliente.title("Clientes do Banco NUA BANK")

        # TreeView
        colunas = ['id_ID', 'nome_ID', 'cpf_ID', 'endereco_ID', 'conta_ID']
        self.treeView_Cliente = ttk.Treeview(self.janela_cliente, show='headings', columns=colunas, height=5, selectmode="browse")

        # Cabeçalho
        self.treeView_Cliente.heading('id_ID', text="ID")
        self.treeView_Cliente.heading('nome_ID', text="Nome")
        self.treeView_Cliente.heading('cpf_ID', text="CPF")
        self.treeView_Cliente.heading('endereco_ID', text="Endereço")
        self.treeView_Cliente.heading('conta_ID', text="Conta")

        self.treeView_Cliente.column('id_ID', minwidth=0, width=45)
        self.treeView_Cliente.column('nome_ID', minwidth=0, width=100)
        self.treeView_Cliente.column('cpf_ID', minwidth=0, width=150)
        self.treeView_Cliente.column('endereco_ID', minwidth=0, width=150)
        self.treeView_Cliente.column('conta_ID', minwidth=0, width=180)

        # Inserir os clientes na TreeView
        for i in self.banco_Em_Cliente.get_Clientes_SemConta:
            self.treeView_Cliente.insert('', 'end', values=(i.get_ID, i.get_Nome, i.get_Cpf, i.get_Endereco, i.get_Conta))

        # Scrollbar
        self.scrollbar_Cliente = ttk.Scrollbar(self.janela_cliente, command=self.treeView_Cliente.yview)
        self.treeView_Cliente.configure(yscroll=self.scrollbar_Cliente.set)

        # Sets
        self.treeView_Cliente.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar_Cliente.pack(side=tk.LEFT, fill=tk.BOTH)

        # Binds
        self.treeView_Cliente.bind('<Double-1>', self.clique_duplo)
        self.treeView_Cliente.bind("<Motion>", 'break')
    

    def clique_duplo(self, event):
        selecionado = self.treeView_Cliente.selection()
        lista = self.treeView_Cliente.item(selecionado)

        if 'values' not in lista or len(lista['values']) == 0:
            messagebox.showwarning("Aviso", "Nenhum cliente foi selecionado.")
            return

        self.Id_Objeto_Atual = lista['values'][0]

        clientes = self.banco_Em_Cliente.get_clientes
        cliente_selecionado = None
        for cliente in clientes:
            if cliente.get_ID == self.Id_Objeto_Atual:
                cliente_selecionado = cliente
                break

        if cliente_selecionado:
            # Atualiza o cliente atual na janela de poupança
            self.janelaPai.cliente_atual = cliente_selecionado

            # Atualiza o botão com o nome do cliente selecionado
            self.btn_select_cli.config(text=f"Cliente: {cliente_selecionado.get_Nome}")

            # Fecha a janela de seleção de cliente
            self.janela_cliente.destroy()
        else:
            messagebox.showwarning("Aviso", "Cliente não encontrado.")
