import datetime as dt
import time as tm
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from classes.banco import Banco
from interface.janela_corrente import Janela_Corrente
from interface.janela_poupanca import Janela_Poupanca
from interface.janela_info     import Janela_Info
from interface.janela_cliente  import Janela_Cliente
from interface.janela_transacoes import Janela_Transacoes
from PIL import ImageTk, Image
import sys
import os
            
class Janela_Banco:
  def __init__(self, master):
    #Instancia da Classe banco ----------------------------
    self.banco = Banco(666666, "NUA BANK")
    #Clientes padrões para testes
    self.banco.criar_cliente("Maria Eduarda Silva"  , "999.999.999-99", "Rua Pó de Osso"     , "265")
    self.banco.criar_cliente("João Pedro Santos"    , "999.999.999-99", "Rua Limoeiro"       , "956")
    self.banco.criar_cliente("Ana Clara Oliveira", "999.999.999-99", "Rua Coluna Torta"   , "7412")
    self.banco.criar_cliente("Sofia Vitória Rodrigues"  , "999.999.999-99", "Rua Limão Rosa"     , "896")
    self.banco.criar_cliente("Gabriel Henrique Souza"  , "999.999.999-99", "Rua Sorvete Aviador", "8454")

    self.banco.criar_Conta_Poupanca(self.banco.get_Clientes_SemConta[0], 100, 500)
    self.banco.criar_Conta_Poupanca(self.banco.get_Clientes_SemConta[0], 500, 1000)
    self.banco.criar_Conta_Corrente(self.banco.get_Clientes_SemConta[0], 1000, 2000)
    self.banco.criar_Conta_Poupanca(self.banco.get_Clientes_SemConta[0], 2000, 5000)
    self.banco.criar_Conta_Corrente(self.banco.get_Clientes_SemConta[0], 5000, 10000)

    #Transacoes de teste -----------------------------------------------------------------------------------------------
    teste = self.banco.get_Contas
    for i in teste:
        i.saca(100)
    for j in teste:
        j.deposita(25)

    #Janela
    
    self.master = master
    self.janela_banco = tk.Tk()
    self.janela_banco.title(self.banco.get_nome)
    self.janela_banco.configure(bg="#F18A01") 
    self.janela_banco.resizable(False, False)
    self.frm_botoes = tk.Frame(self.janela_banco)
    self.frm_botoes.pack(side=tk.BOTTOM)
    
    # Definir um estilo para todos os widgets
    style = ttk.Style()
    style.theme_use('default')  
    
    #Metodos -----------------------------------------------

    #Abrir novas Janelas
    def abrirNovaJanelaCorrente():
      self.novaJanela = tk.Toplevel(self.janela_banco)
      self.novaJanela.grab_set()
      Janela_Corrente(self.novaJanela, self.banco, self.janela_banco, self.treeView_Contas, self.lbl_saldo_banco)

    def abrirNovaJanelaPoupanca():
      self.novaJanela = tk.Toplevel(self.janela_banco)
      self.novaJanela.grab_set()
      Janela_Poupanca(self.novaJanela, self.banco, self.janela_banco, self.treeView_Contas, self.lbl_saldo_banco)
      
    def abrirNovaJanelaInfo():
      self.novaJanela = tk.Toplevel(self.janela_banco)
      self.novaJanela.grab_set()
      Janela_Info(self.novaJanela, self.banco, self.janela_banco)

    def abrirNovaJanelaClientes():
      self.novaJanela = tk.Toplevel(self.janela_banco)
      self.novaJanela.grab_set()
      Janela_Cliente(self.novaJanela, self.banco, self.janela_banco)

    def abrirNovaJanelaTransacoes():
      self.novaJanela = tk.Toplevel(self.janela_banco)
      self.novaJanela.grab_set()
      Janela_Transacoes(self.novaJanela, self.banco, self.janela_banco, self.treeView_Contas, self.lbl_saldo_banco)

    #Criando Menus --------------------------------------

    #Barra do Menu
    self.barra_do_menu = tk.Menu(self.janela_banco)
    self.janela_banco.config(menu=self.barra_do_menu)

    #Menus
    self.info     = tk.Menu(self.barra_do_menu, tearoff=False)
    self.corrente = tk.Menu(self.barra_do_menu, tearoff=False)
    self.poupanca = tk.Menu(self.barra_do_menu, tearoff=False)
    self.clientes = tk.Menu(self.barra_do_menu, tearoff=False)
    self.transacoes = tk.Menu(self.barra_do_menu, tearoff=False)

    #Sub-Menus 
    self.info.add_command      (label='Abrir', command=abrirNovaJanelaInfo)
    self.corrente.add_command  (label='Abrir', command=abrirNovaJanelaCorrente)
    self.poupanca.add_command  (label='Abrir', command=abrirNovaJanelaPoupanca)
    self.clientes.add_command  (label='Abrir', command=abrirNovaJanelaClientes)
    self.transacoes.add_command(label='Abrir', command=abrirNovaJanelaTransacoes)

    #Adicionando Menus a Barra
    self.barra_do_menu.add_cascade(label="Info"    , menu=self.info)
    self.barra_do_menu.add_cascade(label="Corrente", menu=self.corrente)
    self.barra_do_menu.add_cascade(label="Poupança", menu=self.poupanca)
    self.barra_do_menu.add_cascade(label="Clientes", menu=self.clientes)
    self.barra_do_menu.add_cascade(label='Transações', menu=self.transacoes)

    #Frame -------------------------------------------------------------
    self.fr_infos  = tk.Frame(self.janela_banco, background="#F18A01")
    self.fr_botões = tk.Frame(self.janela_banco)

    #Label Frame ---------------------------------------------------------
    self.lbf_data_atual   = tk.LabelFrame(self.fr_infos    , text=f'Data atual', background="#F18A01")
    self.lbf_sessao_atual = tk.LabelFrame(self.fr_infos    , text=f'Seção atual', background="#F18A01")
    self.lbf_saldo_banco  = tk.LabelFrame(self.fr_infos    , text=f'Saldo do Banco', background="#F18A01")
    self.lbf_contas       = tk.LabelFrame(self.janela_banco, text=f'Todas as contas do Banco {self.banco.get_nome}', background="#F18A01")

    self.logo = Image.open(self.resource_path("interface/nua.jpg"))
    self.logo = self.logo.resize((59, 59))  
    self.logo_tk = ImageTk.PhotoImage(self.logo)

    # Label para a imagem
    self.label_logo = ttk.Label(self.fr_infos, image=self.logo_tk, background="#F18A01")
    self.label_logo.pack(side=tk.LEFT, padx=10)
    
    #Label da Data Atual
    date = dt.datetime.now()
    self.lbl_Data = tk.Label(self.lbf_data_atual, text=f"{date:%A, %B %d, %Y}", background="#F18A01")

    #Label da Hora Atual
    self.lbl_tempo_Atual = tk.Label(self.fr_infos, background="#F18A01")

    #Label da sessão atual
    self.lbl_sessao_Atual = tk.Label(self.lbf_sessao_atual,text='00:00:00', background="#F18A01")
    self.hours   = 0
    self.minutes = 0
    self.seconds = 0

    #Label do saldo
    self.lbl_saldo_banco = tk.Label(self.lbf_saldo_banco, text=f'{self.banco.get_saldo_banco}$', background="#F18A01")

    # TreeView
    colunas = ['numero_ID', 'titular_ID', 'tipo_ID', 'saldo_ID', 'limite_ID', 'status_ID']  # Lista com as opções
    self.treeView_Contas = ttk.Treeview(self.lbf_contas, show='headings', columns=colunas, height=10,selectmode="browse")
    # cabeçalho
    self.treeView_Contas.heading('numero_ID' , text="Numero")
    self.treeView_Contas.heading('titular_ID', text="Titular")
    self.treeView_Contas.heading('tipo_ID'   , text="Tipo")
    self.treeView_Contas.heading('saldo_ID'  , text="Saldo")
    self.treeView_Contas.heading('limite_ID' , text="Limite")
    self.treeView_Contas.heading('status_ID' , text="Status")

    self.treeView_Contas.column('numero_ID' , minwidth=0, width=60)
    self.treeView_Contas.column('titular_ID', minwidth=0, width=100)
    self.treeView_Contas.column('tipo_ID'   , minwidth=0, width=150)
    self.treeView_Contas.column('saldo_ID'  , minwidth=0, width=150)
    self.treeView_Contas.column('limite_ID' , minwidth=0, width=180)
    self.treeView_Contas.column('status_ID' , minwidth=0, width=60)


    for i in self.banco.get_Contas:
        self.treeView_Contas.insert('', 'end', values=(i.get_Numero, i.get_Titular, i.get_Cliente.get_Conta, i.get_Saldo, i.get_Limite, i.get_Status))

    # Scrollbar
    self.scrollbar_Banco = ttk.Scrollbar(self.lbf_contas, command=self.treeView_Contas.yview)
    self.treeView_Contas.configure(yscroll=self.scrollbar_Banco.set)
    #Botões
    self.btn_encerrar_conta = tk.Button(self.fr_botões, text='Encerrar Conta'  , command=self.encerrar_conta)
    self.btn_extrato_banco  = tk.Button(self.fr_botões, text='Extrato do Banco', command=self.janela_extrato)
    

    #Sets
    self.scrollbar_Banco.pack(side=tk.RIGHT, fill=tk.BOTH)
    self.treeView_Contas.pack(side=tk.LEFT, fill=tk.BOTH)

    self.lbl_Data.pack()
    self.lbl_tempo_Atual.pack()
    self.lbl_sessao_Atual.pack()
    self.lbl_saldo_banco.pack()

    self.lbf_data_atual.pack  (side=tk.LEFT)
    self.lbf_sessao_atual.pack(side=tk.LEFT)
    self.lbf_saldo_banco.pack (anchor=tk.E)

    self.fr_botões.pack(side=tk.BOTTOM)
    self.fr_infos.pack(fill=tk.X)
    self.lbf_contas.pack()

    self.btn_encerrar_conta.pack(side=tk.LEFT)
    self.btn_extrato_banco.pack(side=tk.LEFT)

    # Evento para evitar o redimensionamento das colunas
    self.treeView_Contas.bind("<Motion>"   , 'break')

    #Main Loop
    #self.mostrar_Hora_Atual()
    self.start()
    self.janela_banco.mainloop()
    
    
  def resource_path(self, relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
  

  def encerrar_conta(self):
   selecionados = self.treeView_Contas.selection()
   lista = self.treeView_Contas.item(selecionados)  # Busca os valores 'values' dentro do selecionado

   if (len(selecionados) == 0):
     messagebox.showwarning("Por favor, selecione pelo menos uma célula antes de deletar.")
   else:
       self.Id_Objeto_Atual = (lista['values'][0])
       for x in self.banco.get_Contas:
           if x.get_Numero == self.Id_Objeto_Atual:
               self.objeto_atual = x

       if(self.objeto_atual.get_Saldo > 0):
         messagebox.showwarning('Aviso', 'Você não pode encerrar uma conta que ainda possui saldo!')
         self.banco.encerrarConta(self.objeto_atual)

       elif(self.objeto_atual.get_Saldo < 0):
         messagebox.showwarning('Aviso', 'Você não pode encerrar uma conta que ainda possui dividas!')
         self.banco.encerrarConta(self.objeto_atual)

       else:
         quer = messagebox.askyesno("Deletar Selecionado", "Você tem certeza?")
         if (quer):
           self.banco.encerrarConta(self.objeto_atual)
           self.treeView_Contas.item(selecionados, values=(self.objeto_atual.get_Numero, self.objeto_atual.get_Titular, self.objeto_atual.get_Cliente.get_Conta, self.objeto_atual.get_Saldo, 0, self.objeto_atual.get_Status))


  def janela_extrato(self):
        self.top_extrato_banco = tk.Toplevel()
        self.top_extrato_banco.title(f'Extrato do banco {self.banco.get_nome}')
        self.top_extrato_banco.grab_set()
        self.top_extrato_banco.resizable(False, False)

        # Treeview
        colunas = ['data','hora','operacao']
        self.treeView_extrato_banco = ttk.Treeview(self.top_extrato_banco, show='headings', columns=colunas, height=5, selectmode='browse')

        # Cabeçalho
        self.treeView_extrato_banco.heading('data', text="Data da Operação")
        self.treeView_extrato_banco.heading('hora', text="Hora")
        self.treeView_extrato_banco.heading('operacao', text="Operação")

        self.treeView_extrato_banco.column ('data'    , minwidth=0, width=150)
        self.treeView_extrato_banco.column ('hora'    , minwidth=0, width=150)
        self.treeView_extrato_banco.column ('operacao', minwidth=0, width=500)

        # Scrollbar
        self.scrollbar_extrato = ttk.Scrollbar(self.top_extrato_banco, command=self.treeView_extrato_banco.yview)
        self.treeView_extrato_banco.configure(yscroll=self.scrollbar_extrato.set)

        self.scrollbar_extrato.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.treeView_extrato_banco.pack(side=tk.LEFT, fill=tk.BOTH)

        # Evento para evitar o redimensionamento das colunas
        self.treeView_extrato_banco.bind("<Motion>", 'break')
        listaOperacoes = self.banco.get_Extrato_Banco

        for i in listaOperacoes:
            self.treeView_extrato_banco.insert('', 'end', values=(i['dataOperacao'], i['horaOperacao'], i['operacao']))

    
    
  def start(self):
    self.lbl_sessao_Atual.after(1000)
    self.update()
    self.running = True
    
    
  def update(self):
    self.seconds += 1
    if self.seconds == 60:
        self.minutes += 1
        self.seconds = 0
    if self.minutes == 60:
        self.hours += 1
        self.minutes = 0
    hours_string = f'{self.hours}' if self.hours > 9 else f'0{self.hours}'
    minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
    seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
    self.lbl_sessao_Atual.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    self.update_time = self.lbl_sessao_Atual.after(1000, self.update)

