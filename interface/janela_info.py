import tkinter as tk
from tkinter import messagebox
from mixins_e_interfaces import verifica_digitos

class Janela_Info:

#Construtor ---------------------------------------------------------------------------------------
  def __init__(self, master, banco, pai):
    self.janelaPai  = pai
    self.janelaInfo = master
    self.janelaInfo.title("Info")
    self.janelaInfo.grab_set()
    self.janelaInfo.resizable(False, False)
    self.janelaInfo.configure(bg='#F18A01')
    #Instancia da Classe banco ----------------------------
    self.banco_em_info = banco

    #Widgets-----------------------------------------------

      #Label Frame
    self.label_frame_1 = tk.LabelFrame(self.janelaInfo, text='Informações do Banco', background="#F18A01")
      #Frames
    self.lbl_numero_1 = tk.Label(self.label_frame_1, text=f'Numero: {self.banco_em_info.get_numero}')
    self.lbl_nome_1   = tk.Label(self.label_frame_1, text=f'Nome: {self.banco_em_info.get_nome}')
    
      #Frame
    self.frame_botoes = tk.Frame(self.label_frame_1)  
    
      #Botões
    self.btn_editar = tk.Button(self.frame_botoes, text='Editar', command= self.tela_editar_info)

    #Sets --------------------------------------------------
    self.frame_botoes.pack(side= tk.BOTTOM)
    
    self.label_frame_1.pack()
    
    self.lbl_nome_1.pack()
    self.lbl_numero_1.pack()
    
    self.btn_editar.pack(side=tk.LEFT)

#Metodos  
  def tela_editar_info(self):
    self.top_editar_info = tk.Toplevel()
    #self.janela.withdraw()
    self.top_editar_info.grab_set()
    self.top_editar_info.title('Editando Info')
    self.top_editar_info.configure(bg='#F18A01')
    
    self.lbl_nome_2   = tk.Label(self.top_editar_info, text='Nome:', background="#F18A01")
    self.lbl_numero_2 = tk.Label(self.top_editar_info, text='Numero:', background="#F18A01")

    self.ent_nome_2   = tk.Entry(self.top_editar_info, width=30)
    self.ent_numero_2 = tk.Entry(self.top_editar_info, width=30)
    
    self.lbl_nome_2.grid(row=0, column=0)
    self.lbl_numero_2.grid(row=1, column=0)
    
    self.ent_nome_2.grid(row=0, column=1)
    self.ent_numero_2.grid(row=1, column=1)
    self.ent_nome_2.insert  (0, self.banco_em_info.get_nome) 
    self.ent_numero_2.insert(0, self.banco_em_info.get_numero) 

  
    self.btn_confirmar = tk.Button(self.top_editar_info, text='Confirmar', command=self.confirmar_edicao)
    self.btn_confirmar.grid(row=3, column=1)   

  def confirmar_edicao(self): 
    self.nome_ent   = self.ent_nome_2.get()
    self.numero_ent = self.ent_numero_2.get()
    self.numero_ent = self.numero_ent.strip()

    if self.nome_ent == '' or self.numero_ent == '':
      messagebox.showinfo('Aviso', 'Todos campos são obrigatórios')
      self.top_editar_info.deiconify()
    
    elif not verifica_digitos.Verificar_Digitos(self.numero_ent) or not verifica_digitos.Verificar_Caractes_Especiais(self.numero_ent):
      messagebox.showinfo('Aviso', 'O número do banco deve conter apenas digitos!')
      self.top_editar_info.deiconify()

    elif not verifica_digitos.Verificar_Espaco(self.numero_ent):
      messagebox.showinfo('Aviso', 'O número do banco não deve conter espaços em branco!')
      self.top_editar_info.deiconify()

    else:
      nome_Original   = self.banco_em_info.get_nome
      numero_Original = self.banco_em_info.get_numero     
      
      if(self.nome_ent == nome_Original and self.numero_ent == numero_Original):
        quer = messagebox.askyesno("Se liga heim!","Nenhuma alteração feita, deseja sair?")
        if(quer == True):
          self.top_editar_info.destroy()
          self.janelaInfo.lift()
        else:
          self.janelaInfo.lift()
          self.top_editar_info.lift()
      else:

        self.banco_em_info.set_nome(self.nome_ent)
        self.banco_em_info.set_numero(self.numero_ent)
        
        self.lbl_nome_1.config( text=f'Nome: {self.banco_em_info.get_nome}')
        self.lbl_numero_1.config( text=f'Numero: {self.banco_em_info.get_numero}')

        self.janelaPai.title(self.banco_em_info.get_nome)

        self.top_editar_info.destroy()
        self.janelaInfo.lift()

      
