import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from interface.janela_cliente_read import Janela_Cliente_Read
from mixins_e_interfaces import verifica_digitos

class Janela_Poupanca:
  def __init__(self, master, banco, pai, treeViewPai, label_saldo_banco):
    # Mude aqui de Janela_Poupanca.cliente_atual para self.cliente_atual
    self.cliente_atual = None  
    self.banco_Em_Poupanca = banco
    self.janelaPai = pai
    self.treeViewPai = treeViewPai
    self.lbl_saldo_banco = label_saldo_banco


    self.lista_clientes = ["Nenhuma cliente selecionado"]
    self.lista_clientes.extend(self.banco_Em_Poupanca.get_ID_clientes_semConta)

    #Janela
    self.janela_poupanca = master
    self.janela_poupanca.title("Contas Poupança do Banco NUA BANK")
    self.janela_poupanca.resizable(False, False)
    self.janela_poupanca.configure(bg="#F18A01")

    # TreeView
    colunas = ['numero_ID', 'nome_ID', 'saldo_ID', 'limite_ID']
    self.treeView_Conta_Pop = ttk.Treeview(self.janela_poupanca, show='headings', columns=colunas, height=5)

    # cabeçalho
    self.treeView_Conta_Pop.heading('numero_ID', text="Numero")
    self.treeView_Conta_Pop.heading('nome_ID'  , text="Nome")
    self.treeView_Conta_Pop.heading('saldo_ID' , text="Saldo")
    self.treeView_Conta_Pop.heading('limite_ID', text="Limite")

    self.treeView_Conta_Pop.column('numero_ID' , minwidth=0, width=60)
    self.treeView_Conta_Pop.column('nome_ID'   , minwidth=0, width=100)
    self.treeView_Conta_Pop.column('saldo_ID'  , minwidth=0, width=150)
    self.treeView_Conta_Pop.column('limite_ID' , minwidth=0, width=150)

    for i in self.banco_Em_Poupanca.get_Contas_Pop:
      self.treeView_Conta_Pop.insert('', 'end', values=(i.get_Numero, i.get_Titular, i.get_Saldo, i.get_Limite))

    # Scrollbar
    self.scrollbar_Poupanca = ttk.Scrollbar(self.janela_poupanca, command=self.treeView_Conta_Pop.yview)
    self.treeView_Conta_Pop.configure(yscroll=self.scrollbar_Poupanca.set)

    # Frames
    self.frame_botoes = tk.Frame(self.janela_poupanca)

    # Botões
    self.btn_cadastrar = tk.Button(self.frame_botoes, text='Abrir Nova Conta Poupança', command=self.cadastrar_poupanca)

    # Sets -------------------------------------------------------------
    self.frame_botoes.pack(side=tk.BOTTOM)

    self.treeView_Conta_Pop.pack(side=tk.LEFT, fill=tk.BOTH)

    self.scrollbar_Poupanca.pack(side=tk.LEFT, fill=tk.BOTH)

    self.btn_cadastrar.pack()

    # Evento para evitar o redimensionamento das colunas
    self.treeView_Conta_Pop.bind("<Motion>"   , 'break')


  #Métodos
  def cadastrar_poupanca(self):
    self.ID_Cliente_Atual = '0'

    self.top_cadastro_poupanca = tk.Toplevel()
    self.top_cadastro_poupanca.grab_set()
    self.top_cadastro_poupanca.title('Nova conta poupanca :D')

    #Frames
    self.frm_cliente  = tk.Frame(self.top_cadastro_poupanca)
    self.frm_deposito = tk.Frame(self.top_cadastro_poupanca)
    self.frm_limite   = tk.Frame(self.top_cadastro_poupanca)

    self.frame_botoes_cadastro = tk.Frame(self.top_cadastro_poupanca)

    # Labels
    self.lbl_cliente  = tk.Label(self.frm_cliente , text='Selecione um cliente:', width=20, anchor='w')
    self.lbl_deposito = tk.Label(self.frm_deposito, text='Depósito Inicial:'    , width=20, anchor='w')
    self.lbl_limite   = tk.Label(self.frm_limite  , text='Limite Inicial:'      , width=20, anchor='w')

    # Entradas
    self.ent_deposito = tk.Entry(self.frm_deposito, width=30)
    self.ent_limite   = tk.Entry(self.frm_limite  , width=30)

    # Botões
    self.btn_select_cli = tk.Button(self.frm_cliente, text='Nenhum cliente selecionado', command=self.selecionar_cliente)

    self.btn_confirmar = tk.Button(self.frame_botoes_cadastro, text='Confirmar', command=self.confirmar_cadastro)

    # Sets
    self.lbl_cliente.pack   (side=tk.LEFT)
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
    # Verifique se o cliente está selecionado
    if self.cliente_atual is None:
        messagebox.showwarning('Aviso', 'Selecione um cliente!')
        return

    deposito = self.ent_deposito.get()
    limite = self.ent_limite.get()

    if deposito == '' or limite == '':
        messagebox.showinfo('Aviso', 'Todos os campos são obrigatórios')
        self.top_cadastro_poupanca.grab_set()
        self.janela_poupanca.lift()
        self.top_cadastro_poupanca.lift()

    elif not verifica_digitos.Verificar_Digitos(deposito):
        messagebox.showinfo('Aviso', 'O valor depositado deve conter apenas dígitos!')
        self.top_cadastro_poupanca.grab_set()
        self.janela_poupanca.lift()
        self.top_cadastro_poupanca.lift()

    elif not verifica_digitos.Verificar_Digitos(limite):
        messagebox.showinfo('Aviso', 'O valor do limite deve conter apenas dígitos!')
        self.top_cadastro_poupanca.grab_set()
        self.janela_poupanca.lift()
        self.top_cadastro_poupanca.lift()

    elif not verifica_digitos.Verifica_Apenas_Um_Ponto(deposito):
        messagebox.showinfo('Aviso', 'O valor a ser depositado deve conter apenas uma vírgula ou ponto!')
        self.top_cadastro_poupanca.grab_set()
        self.janela_poupanca.lift()
        self.top_cadastro_poupanca.lift()

    elif not verifica_digitos.Verificar_Espaco(deposito):
        messagebox.showinfo('Aviso', 'O valor a ser depositado não deve conter espaços em branco!')
        self.top_cadastro_poupanca.grab_set()
        self.janela_poupanca.lift()
        self.top_cadastro_poupanca.lift()

    elif not verifica_digitos.Verifica_Apenas_Um_Ponto(limite):
        messagebox.showinfo('Aviso', 'O valor do limite deve conter apenas uma vírgula ou ponto!')
        self.top_cadastro_poupanca.grab_set()
        self.janela_poupanca.lift()
        self.top_cadastro_poupanca.lift()

    elif not verifica_digitos.Verificar_Espaco(limite):
        messagebox.showinfo('Aviso', 'O valor do limite não deve conter espaços em branco!')
        self.top_cadastro_poupanca.grab_set()
        self.janela_poupanca.lift()
        self.top_cadastro_poupanca.lift()

    elif float(deposito) < 0:
        messagebox.showinfo('Aviso', 'O valor do depósito não pode ser negativo!')
        self.top_cadastro_poupanca.grab_set()
        self.janela_poupanca.lift()
        self.top_cadastro_poupanca.lift()

    elif float(limite) < 0:
        messagebox.showinfo('Aviso', 'O valor do limite não pode ser negativo!')
        self.top_cadastro_poupanca.grab_set()
        self.janela_poupanca.lift()
        self.top_cadastro_poupanca.lift()

    else:
        # Criando uma conta ------------------------------------
        self.nova_contaPop = self.banco_Em_Poupanca.criar_Conta_Poupanca(self.cliente_atual, deposito, limite)
        self.lbl_saldo_banco.config(text=f'{self.banco_Em_Poupanca.get_saldo_banco}')

        self.treeView_Conta_Pop.insert('', 'end', values=(self.nova_contaPop.get_Numero, self.nova_contaPop.get_Titular, self.nova_contaPop.get_Saldo, self.nova_contaPop.get_Limite))

        self.lista_clientes = ["Nenhuma cliente selecionado"]
        self.lista_clientes.extend(self.banco_Em_Poupanca.get_ID_clientes_semConta)

        self.treeViewPai.insert('', 'end', values=(self.nova_contaPop.get_Numero, self.nova_contaPop.get_Titular, self.nova_contaPop.get_Cliente.get_Conta, self.nova_contaPop.get_Saldo, self.nova_contaPop.get_Status))
        
        self.top_cadastro_poupanca.destroy()

  def selecionar_cliente(self):
    self.novaJanela = tk.Toplevel(self.top_cadastro_poupanca)
    self.novaJanela.grab_set()

    # Passa a própria instância de Janela_Poupanca como "pai"
    Janela_Cliente_Read(self.novaJanela, self.banco_Em_Poupanca, self, self.ID_Cliente_Atual, self.btn_select_cli)
