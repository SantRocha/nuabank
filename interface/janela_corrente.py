import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from interface.janela_cliente_read import Janela_Cliente_Read
from mixins_e_interfaces import verifica_digitos

class Janela_Corrente:
    def __init__(self, master, banco, pai, treeViewPai, label_saldo_banco):
        self.cliente_atual = None  # Variável para armazenar o cliente atual
        self.treeViewPai = treeViewPai
        self.banco_Em_Corrente = banco
        self.janelaPai = pai
        self.lbl_saldo_banco = label_saldo_banco

        self.lista_clientes = ["Nenhuma cliente selecionado"]
        self.lista_clientes.extend(self.banco_Em_Corrente.get_ID_clientes_semConta)

        # Janela
        self.janela_corrente = master
        self.janela_corrente.title("Contas Correntes do NUA BANK")
        self.janela_corrente.configure(bg="#F18A01") 
        self.janela_corrente.resizable(False, False)

        # TreeView
        colunas = ['numero_ID', 'nome_ID', 'saldo_ID', 'limite_ID']
        self.treeView_Conta_Cor = ttk.Treeview(self.janela_corrente, show='headings', columns=colunas, height=5)

        # Cabeçalho
        self.treeView_Conta_Cor.heading('numero_ID', text="Numero")
        self.treeView_Conta_Cor.heading('nome_ID', text="Nome")
        self.treeView_Conta_Cor.heading('saldo_ID', text="Saldo")
        self.treeView_Conta_Cor.heading('limite_ID', text="Limite")

        self.treeView_Conta_Cor.column('numero_ID', minwidth=0, width=60)
        self.treeView_Conta_Cor.column('nome_ID', minwidth=0, width=100)
        self.treeView_Conta_Cor.column('saldo_ID', minwidth=0, width=150)
        self.treeView_Conta_Cor.column('limite_ID', minwidth=0, width=150)

        for i in self.banco_Em_Corrente.get_Contas_Cor:
            self.treeView_Conta_Cor.insert('', 'end', values=(i.get_Numero, i.get_Titular, i.get_Saldo, i.get_Limite))

        # Scrollbar
        self.scrollbar_Corrente = ttk.Scrollbar(self.janela_corrente, command=self.treeView_Conta_Cor.yview)
        self.treeView_Conta_Cor.configure(yscroll=self.scrollbar_Corrente.set)

        # Frames
        self.frame_botoes = tk.Frame(self.janela_corrente)

        # Botões
        self.btn_cadastrar = tk.Button(self.frame_botoes, text='Abrir Nova Conta Corrente', command=self.cadastrar_corrente)

        # Sets
        self.frame_botoes.pack(side=tk.BOTTOM)
        self.treeView_Conta_Cor.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar_Corrente.pack(side=tk.LEFT, fill=tk.BOTH)
        self.btn_cadastrar.pack()

        # Evento para evitar o redimensionamento das colunas
        self.treeView_Conta_Cor.bind("<Motion>", 'break')

    def selecionar_cliente(self):
        self.novaJanela = tk.Toplevel(self.top_cadastro_corrente)
        self.novaJanela.grab_set()
        Janela_Cliente_Read(self.novaJanela, self.banco_Em_Corrente, self, self.cliente_atual, self.btn_select_cli)

    def cadastrar_corrente(self):
        self.top_cadastro_corrente = tk.Toplevel()
        self.top_cadastro_corrente.grab_set()
        self.top_cadastro_corrente.title('Nova conta corrente :D')

        # Frames
        self.frm_cliente = tk.Frame(self.top_cadastro_corrente)
        self.frm_deposito = tk.Frame(self.top_cadastro_corrente)
        self.frm_limite = tk.Frame(self.top_cadastro_corrente)

        self.frame_botoes_cadastro = tk.Frame(self.top_cadastro_corrente)

        # Labels
        self.lbl_cliente = tk.Label(self.frm_cliente, text='Selecione um cliente:', width=20, anchor='w')
        self.lbl_deposito = tk.Label(self.frm_deposito, text='Depósito Inicial:', width=20, anchor='w')
        self.lbl_limite = tk.Label(self.frm_limite, text='Limite Inicial:', width=20, anchor='w')

        # Entradas
        self.ent_deposito = tk.Entry(self.frm_deposito, width=30)
        self.ent_limite = tk.Entry(self.frm_limite, width=30)

        # Botões
        self.btn_select_cli = tk.Button(self.frm_cliente, text='Nenhum cliente selecionado', command=self.selecionar_cliente)
        self.btn_confirmar = tk.Button(self.frame_botoes_cadastro, text='Confirmar', command=self.confirmar_cadastro)

        # Sets
        self.lbl_cliente.pack(side=tk.LEFT)
        self.btn_select_cli.pack(side=tk.LEFT, expand=True, fill='both')
        self.lbl_deposito.pack(side=tk.LEFT)
        self.ent_deposito.pack(side=tk.LEFT)
        self.lbl_limite.pack(side=tk.LEFT)
        self.ent_limite.pack(side=tk.LEFT)
        self.btn_confirmar.pack(side=tk.LEFT)

        self.frm_cliente.pack(expand=True, fill='both')
        self.frm_deposito.pack(expand=True, fill='both')
        self.frm_limite.pack(expand=True, fill='both')
        self.frame_botoes_cadastro.pack()

    def confirmar_cadastro(self):
        if self.cliente_atual is None:
            messagebox.showinfo('Aviso', 'Selecione um cliente!')
            return

        deposito = self.ent_deposito.get()
        limite = self.ent_limite.get()

        if deposito == '' or limite == '':
            messagebox.showinfo('Aviso', 'Todos campos são obrigatórios')
        elif not verifica_digitos.Verificar_Digitos(deposito):
            messagebox.showinfo('Aviso', 'O valor de depósito deve conter apenas dígitos!')
        elif not verifica_digitos.Verificar_Digitos(limite):
            messagebox.showinfo('Aviso', 'O valor de limite deve conter apenas dígitos!')
        elif float(deposito) < 0:
            messagebox.showinfo('Aviso', 'O valor do depósito não pode ser negativo!')
        elif float(limite) < 0:
            messagebox.showinfo('Aviso', 'O valor do limite não pode ser negativo!')
        else:
            # Criar a conta corrente
            self.nova_contaCor = self.banco_Em_Corrente.criar_Conta_Corrente(self.cliente_atual, deposito, limite)
            self.lbl_saldo_banco.config(text=f'{self.banco_Em_Corrente.get_saldo_banco}')

            # Atualizar TreeView
            self.treeView_Conta_Cor.insert('', 'end', values=(self.nova_contaCor.get_Numero, self.nova_contaCor.get_Titular, self.nova_contaCor.get_Saldo, self.nova_contaCor.get_Limite))

            self.lista_clientes = ["Nenhuma cliente selecionado"]
            self.lista_clientes.extend(self.banco_Em_Corrente.get_ID_clientes_semConta)

            self.treeViewPai.insert('', 'end', values=(self.nova_contaCor.get_Numero, self.nova_contaCor.get_Titular, self.nova_contaCor.get_Cliente.get_Conta, self.nova_contaCor.get_Saldo, self.nova_contaCor.get_Limite, self.nova_contaCor.get_Status))

            # Fecha a janela de criação de conta
            self.top_cadastro_corrente.destroy()
