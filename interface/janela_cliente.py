import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from classes.cliente import Cliente
from classes.banco import Banco

class Janela_Cliente:
  def __init__(self, master, banco, pai):
    #Instancia da Classe banco ----------------------------
    self.banco_Em_Cliente = banco
    self.janelaPai = pai
    
    self.janela_cliente = master
    self.janela_cliente.title("Clientes do Banco NUA BANK")
    self.janela_cliente.configure(bg="#F18A01") 
    self.janela_cliente.resizable(False, False)

    #TreeView
    colunas = ['id_ID','nome_ID', 'cpf_ID', 'endereco_ID','conta_ID']#Lista com as opções
    self.treeView_Cliente = ttk.Treeview(self.janela_cliente, show='headings', columns=colunas, height=5,selectmode="browse")
       
    #cabeçalho
    self.treeView_Cliente.heading('id_ID'      ,text="ID")
    self.treeView_Cliente.heading('nome_ID'    ,text="Nome")
    self.treeView_Cliente.heading('cpf_ID'     ,text="CPF")
    self.treeView_Cliente.heading('endereco_ID',text="Endereco")    
    self.treeView_Cliente.heading('conta_ID'   ,text="Conta")

    self.treeView_Cliente.column('id_ID'      ,minwidth=0, width=45)
    self.treeView_Cliente.column('nome_ID'    ,minwidth=0, width=100)
    self.treeView_Cliente.column('cpf_ID'     ,minwidth=0, width=150)
    self.treeView_Cliente.column('endereco_ID',minwidth=0, width=150)    
    self.treeView_Cliente.column('conta_ID'   ,minwidth=0, width=180)

    for i in self.banco_Em_Cliente.get_clientes:
      self.treeView_Cliente.insert('', 'end', values=(i.get_ID, i.get_Nome, i.get_Cpf, i.get_Endereco, i.get_Conta))

    #Scrollbar
    self.scrollbar_Cliente = ttk.Scrollbar(self.janela_cliente, command=self.treeView_Cliente.yview)
    self.treeView_Cliente.configure(yscroll=self.scrollbar_Cliente.set)

    #Frames
    self.frame_botoes = tk.Frame(self.janela_cliente, background="#F18A01")
    
    #Botões
    self.btn_cadastrar     = tk.Button(self.frame_botoes, text='Cadastrar'    , command=self.tela_cadastrar)
    self.btn_deletar_Lista = tk.Button(self.frame_botoes, text='Deletar '     , command=self.deletar_selecionado)
    self.btn_atualizar     = tk.Button(self.frame_botoes, text='Atualizar'    , command=self.atualizar)
  
    #Sets -------------------------------------------------------------
    self.frame_botoes.pack(side = tk.BOTTOM)
    
    self.treeView_Cliente.pack(side=tk.LEFT, fill=tk.BOTH)
    
    self.scrollbar_Cliente.pack(side=tk.LEFT, fill=tk.BOTH)
    
    self.btn_cadastrar.pack    (side=tk.LEFT, padx=10)
    self.btn_deletar_Lista.pack(side=tk.LEFT, padx=10)
    self.btn_atualizar.pack    (side=tk.LEFT, padx=10)

    # Evento para evitar o redimensionamento das colunas
    self.treeView_Cliente.bind("<Motion>", 'break')

  def tela_cadastrar(self):
    self.top_cadastro_cliente = tk.Toplevel()
    self.top_cadastro_cliente.grab_set()
    self.top_cadastro_cliente.title('Cadastro de um novo cliente :D')

    #Labels
    self.lbl_nome     = tk.Label(self.top_cadastro_cliente, text='Nome:')
    self.lbl_cpf      = tk.Label(self.top_cadastro_cliente, text='CPF:')
    self.lbl_endereco = tk.Label(self.top_cadastro_cliente, text='Endereco:')
    self.lbl_senha    = tk.Label(self.top_cadastro_cliente, text='Senha')

    #Entradas
    self.ent_nome     = tk.Entry(self.top_cadastro_cliente, width=30)
    self.ent_cpf      = tk.Entry(self.top_cadastro_cliente, width=30)
    self.ent_endereco = tk.Entry(self.top_cadastro_cliente, width=30)
    self.ent_senha    = tk.Entry(self.top_cadastro_cliente, width=30)

    #Botões
    self.btn_confirmar = tk.Button(self.top_cadastro_cliente, text='Confirmar', command=self.confirmar_cadastro)

    #Sets
    self.lbl_nome.grid      (row=0, column=0)
    self.lbl_cpf.grid       (row=1, column=0)
    self.lbl_endereco.grid  (row=2, column=0)  
    self.lbl_senha.grid     (row=3, column=0)

    self.ent_nome.grid      (row=0, column=1)
    self.ent_cpf.grid       (row=1, column=1)
    self.ent_endereco.grid  (row=2, column=1)
    self.ent_senha.grid     (row=3, column=1)
    
    self.btn_confirmar.grid (row=4, column=1)

  def confirmar_cadastro(self):
    nome     = self.ent_nome.get()
    cpf      = self.ent_cpf.get()
    endereco = self.ent_endereco.get()
    senha    = self.ent_senha.get()
    
    if nome == '' or cpf == '' or endereco == '' :
      messagebox.showinfo('Aviso', 'Todos campos são obrigatórios')
      self.top_cadastro_cliente.deiconify()

    elif(Banco.validaCpf(cpf) == 'formato incorreto'):
      messagebox.showwarning("Se liga heim!","O CPF digitado não é válido! \n Digite no formato 000.000.000-00 ")
      self.top_cadastro_cliente.deiconify()

    elif(not Banco.validaCpf(cpf)):
      messagebox.showwarning("Se liga heim!", "O CPF digitado não é válido!")
      self.top_cadastro_cliente.deiconify()    
    else:
      #Criando um cliente ------------------------------------
      self.novo_cliente = self.banco_Em_Cliente.criar_cliente(nome,endereco,cpf,senha)

      self.treeView_Cliente.insert('', 'end', values=(self.novo_cliente.get_ID, self.novo_cliente.get_Nome, self.novo_cliente.get_Endereco, self.novo_cliente.get_Cpf, self.novo_cliente.get_Conta))
      self.top_cadastro_cliente.destroy()
      self.janela_cliente.deiconify()  

  def deletar_selecionado(self):
    selecionados = self.treeView_Cliente.selection()
    lista = self.treeView_Cliente.item(selecionados)  # Busca os valores 'values' dentro do selecionado
    if (len(selecionados) == 0):
      messagebox.showwarning("Se liga heim!", "Ta deletando o que? Selecione pelo menos uma célula antes pfv.")
    else:
      conta = (lista['values'][4])
      if(conta != "Nenhuma conta associada"):
        messagebox.showwarning("Se liga heim!","Você não pode deletar um cliente que já está associado a uma conta!")
      else:
        quer = messagebox.askyesno("Deletar Selecionado", "Você tem certeza?")
        if(quer):
          self.Id_Objeto_Atual = (lista['values'][0])

          for x in self.banco_Em_Cliente.get_clientes:
            if x.get_ID == self.Id_Objeto_Atual:
              self.objeto_atual = x

          for l in selecionados:
            self.treeView_Cliente.delete(l)
            self.banco_Em_Cliente.get_clientes.remove(self.objeto_atual)

  def atualizar(self):
    #Pegando informações do Treeview
    selecionados = self.treeView_Cliente.selection()

    #Verifica se so uma linha foi selecionada
    if(len(selecionados) > 1):
      messagebox.showinfo('Aviso', 'Selecione apenas um para editar')
    elif(len(selecionados) == 0):
      messagebox.showwarning("Se liga heim!", "Ta atualizando o que? Selecione pelo menos uma célula antes pfv.")
    else:
      self.lista = self.treeView_Cliente.item(selecionados) #Busca os valores 'values' dentro do selecionado

      self.top_atualiza_cliente = tk.Toplevel()
      self.top_atualiza_cliente.grab_set() #Deixa a janela mãe intangivel
      self.top_atualiza_cliente.title("Atualizar Cadastro")

      #Labels
      self.lbl_endereco = tk.Label(self.top_atualiza_cliente, text='Endereco:')
      self.lbl_senha    = tk.Label(self.top_atualiza_cliente, text='Senha')

      #Entradas
      self.ent_endereco = tk.Entry(self.top_atualiza_cliente, width=30)
      self.ent_senha    = tk.Entry(self.top_atualiza_cliente, width=30)

      #Botões
      self.btn_confirmar = tk.Button(self.top_atualiza_cliente, text='Confirmar', command=self.confirmar_atualizacao)

      #Sets
      self.lbl_endereco.grid  (row=0, column=0)
      self.lbl_senha.grid     (row=1, column=0)

      self.ent_endereco.grid  (row=0, column=1)
      self.ent_senha.grid     (row=1, column=1)

      self.btn_confirmar.grid (row=2, column=1)

      self.Id_Objeto_Atual = (self.lista['values'][0])

      for x in self.banco_Em_Cliente.get_clientes:
        if x.get_ID == self.Id_Objeto_Atual:
          self.objeto_atual = x

      self.ent_endereco.insert(0,self.objeto_atual.get_Endereco)
      self.ent_senha.insert(0,self.objeto_atual.get_Senha)

  def confirmar_atualizacao(self):
    self.selecionado = self.treeView_Cliente.selection()
    endereco = self.ent_endereco.get()
    senha = self.ent_senha.get()

    if endereco == '' or senha == '':
      messagebox.showinfo('Aviso', 'Todos campos são obrigatórios')
      self.top_atualiza_cliente.deiconify()

    else:
      self.index = self.treeView_Cliente.index(self.selecionado)
      #Pegando informações do Treeview
      lista = self.treeView_Cliente.item(self.selecionado) #Busca os valores 'values' dentro do selecionado

      endereco_Original     = self.objeto_atual.get_Endereco
      senha_Original        = self.objeto_atual.get_Senha

    if(senha == senha_Original and endereco == endereco_Original):
      quer = messagebox.askyesno("Se liga heim!","Nenhuma alteração feita, deseja sair?")
      self.top_atualiza_cliente.deiconify()

      if(quer == True):
        self.top_atualiza_cliente.destroy()

    else:
      self.objeto_atual.set_Endereco(endereco)
      self.objeto_atual.set_Senha(senha)

      self.treeView_Cliente.item(self.selecionado, values=(self.objeto_atual.get_ID, self.objeto_atual.get_Nome, self.objeto_atual.get_Cpf, self.objeto_atual.get_Endereco, self.objeto_atual.get_Conta))

      self.top_atualiza_cliente.destroy()
      self.janela_cliente.deiconify()

