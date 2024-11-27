from collections import Counter
import tkinter as tk
from tkinter import ttk, messagebox
from mixins_e_interfaces import verifica_digitos


class Janela_Transacoes:
    def __init__(self, master, banco, pai, treeViewPai, label_saldo_banco):

        #Referencias da Janela_Banco
        self.janelaPai = pai
        self.banco_em_Transacoes = banco
        self.treeViewPai = treeViewPai
        self.lbl_saldo_banco = label_saldo_banco

        #Criação da janela Transacoes
        self.janela_transacoes = master
        self.janela_transacoes.title("Transações")
        self.janela_transacoes.resizable(False, False)
        self.janela_transacoes.configure(bg="#F18A01")
        self.janela_transacoes.grab_set()

        #Frame de botões
        self.fmr_botoes = tk.Frame(self.janela_transacoes, background="#F18A01")

        self.lista_transacoes = ['Nenhuma transação feita por enquanto']
        self.lista_transacoes.extend(self.banco_em_Transacoes.get_ID_clientes_semConta)

        #Treeview
        colunas = ['numero', 'titular', 'saldo', 'limite', 'status']
        self.treeViewe_Transacoes = ttk.Treeview(self.janela_transacoes, show='headings', columns=colunas, height=5, selectmode='browse')

            #Cabeçalho
        self.treeViewe_Transacoes.heading('numero' , text="Numero")
        self.treeViewe_Transacoes.heading('titular', text="Titular")
        self.treeViewe_Transacoes.heading('saldo'  , text="Saldo")
        self.treeViewe_Transacoes.heading('limite' , text="Limite")
        self.treeViewe_Transacoes.heading('status' , text="Status")


        self.treeViewe_Transacoes.column('numero' , minwidth=0, width=100)
        self.treeViewe_Transacoes.column('titular', minwidth=0, width=150)
        self.treeViewe_Transacoes.column('saldo'  , minwidth=0, width=180)
        self.treeViewe_Transacoes.column('limite' , minwidth=0, width=190)
        self.treeViewe_Transacoes.column('status' , minwidth=0, width=190)


        for i in self.banco_em_Transacoes.get_Contas:
            self.treeViewe_Transacoes.insert('', 'end', values=(i.get_Numero, i.get_Titular, i.get_Saldo, i.get_Limite, i.get_Status))

        #Scrollbar
        self.scrollbar_trans = ttk.Scrollbar(self.janela_transacoes, command=self.treeViewe_Transacoes.yview)
        self.treeViewe_Transacoes.configure(yscroll=self.scrollbar_trans.set)

        #Botões
        self.btn_sacar     = tk.Button(self.fmr_botoes, text="Sacar"    , command=self.janela_sacar)
        self.btn_depositar = tk.Button(self.fmr_botoes, text="Depositar", command=self.janela_depositar)
        self.btn_extrato   = tk.Button(self.fmr_botoes, text="Extrato"  , command=self.janela_extrato)

        #Sets
        self.fmr_botoes.pack(side=tk.BOTTOM)
        self.treeViewe_Transacoes.pack(side=tk.LEFT, fill=tk.BOTH)

        self.btn_sacar.pack(side=tk.LEFT, padx=10)
        self.btn_depositar.pack(side=tk.LEFT, padx=10)
        self.btn_extrato.pack(side=tk.LEFT, padx=10)
        # Evento para evitar o redimensionamento das colunas
        self.treeViewe_Transacoes.bind("<Motion>"   , 'break')

    #Métodos
    def janela_sacar(self):
        #Seleção
        self.selecionados = self.treeViewe_Transacoes.selection()

        # Verifica se so uma linha foi selecionada
        if (len(self.selecionados) > 1):
            messagebox.showinfo('NUA BANK', 'Selecione apenas um para editar')
        elif (len(self.selecionados) == 0):
            messagebox.showwarning("NUA BANK", "Selecione uma conta por favor!")
        else:
            self.lista_selecionados = self.treeViewe_Transacoes.item(self.selecionados)  # Busca os valores 'values' dentro do selecionado
            #Pegando referencia do objeto selecionado
            self.Id_Objeto_Atual = (self.lista_selecionados['values'][0])
            for x in self.banco_em_Transacoes.get_Contas:
                if x.get_Numero == self.Id_Objeto_Atual:
                    self.objeto_atual = x
            if(self.objeto_atual.get_Status == "Encerrada"):
                messagebox.showwarning("NUA BANK", "Você não pode sacar de contas encerradas")
                self.objeto_atual.saca(1)
            else:
                self.top_sacar = tk.Toplevel()
                self.top_sacar.grab_set()
                self.top_sacar.title("Sacar")
                self.top_sacar.resizable(False, False)

                #Label
                self.lbl_sacar = tk.Label(self.top_sacar, text='Digite o valor para sacar:')

                #Botão
                self.btn_sacar_1 = tk.Button(self.top_sacar, text='Sacar', command=self.confirmar_saque)

                #Ent
                self.ent_sacar = tk.Entry(self.top_sacar, width=30)

                #Sets
                self.lbl_sacar.grid(row=0, column=0)
                self.ent_sacar.grid(row=0, column=1)
                self.btn_sacar_1.grid(row=1, column=1)

    def confirmar_saque(self):
        valor_de_saque = (self.ent_sacar.get()).strip()
        valor_de_saque = valor_de_saque.replace(',','.')

        #Get Ent
        if( valor_de_saque == '' ):
            messagebox.showinfo('NUA BANK', 'Todos campos são obrigatórios')
            self.top_sacar.grab_set()
            self.janela_transacoes.lift()
            self.top_sacar.lift()

        elif( not verifica_digitos.Verificar_Digitos(valor_de_saque ) ):
            messagebox.showinfo('NUA BANK', 'O valor a ser sacado deve conter apenas digitos!')
            self.top_sacar.grab_set()
            self.janela_transacoes.lift()
            self.top_sacar.lift()

        elif( not verifica_digitos.Verifica_Apenas_Um_Ponto(valor_de_saque ) ):
            messagebox.showinfo('NUA BANK', 'O valor a ser sacado deve conter apenas uma virgula ou ponto!')

        elif( not verifica_digitos.Verificar_Espaco(valor_de_saque ) ):
            messagebox.showinfo('NUA BANK', 'O valor a ser sacado não deve conter espaços em branco!')
            self.top_sacar.grab_set()
            self.janela_transacoes.lift()
            self.top_sacar.lift()

        elif(float(valor_de_saque) < 0):
            messagebox.showinfo('NUA BANK', 'O valor inserido é negativo!')
            self.top_sacar.grab_set()
            self.janela_transacoes.lift()
            self.top_sacar.lift()

        else:
            valor_de_saque = float(valor_de_saque)
            status = self.objeto_atual.saca(valor_de_saque)
            self.lbl_saldo_banco.config(text=f'{self.banco_em_Transacoes.get_saldo_banco}')

            #Status do saque
            if(status == 1):
                if(valor_de_saque == 1):
                    messagebox.showinfo('NUA BANK', f'Conta {self.objeto_atual.get_Numero}\nSaque de {valor_de_saque}$\nSaldo Atual: {self.objeto_atual.get_Saldo}$\nSaldo Anterior: {round( (self.objeto_atual.get_Saldo + valor_de_saque), 2)}$\nNão gaste tudo em um só lugar!!!')
                else:
                    messagebox.showinfo('NUA BANK', f'Conta {self.objeto_atual.get_Numero}\nSaque de {valor_de_saque}$\nSaldo Atual: {self.objeto_atual.get_Saldo}$\nSaldo Anterior: {round( (self.objeto_atual.get_Saldo + valor_de_saque), 2)}$')

                #Alterando o treeview em transacoes
                self.treeViewe_Transacoes.item(self.selecionados, values=(self.objeto_atual.get_Numero, self.objeto_atual.get_Titular, self.objeto_atual.get_Saldo, self.objeto_atual.get_Limite, self.objeto_atual.get_Status))
                #Alterando o treeview em banco
                self.treeViewPai.item(self.selecionados, values=(self.objeto_atual.get_Numero, self.objeto_atual.get_Titular, self.objeto_atual.get_Cliente.get_Conta, self.objeto_atual.get_Saldo, self.objeto_atual.get_Limite,  self.objeto_atual.get_Status))
                self.top_sacar.destroy()
                self.janela_transacoes.lift()

            elif(status == 2):
                messagebox.showinfo('NUA BANK', f'Conta {self.objeto_atual.get_Numero}: saldo inssuficiente! | Saldo Atual: {self.objeto_atual.get_Saldo}$')
                self.top_sacar.grab_set()
                self.janela_transacoes.lift()
                self.top_sacar.lift()
            elif(status == 3):
                messagebox.showinfo('NUA BANK', "É piada ou o que?")
                self.top_sacar.grab_set()
                self.top_sacar.lift()
            else:
                messagebox.showinfo('Se liga heim!', "Operação invalida: Conta Encerradaa!")
                self.top_sacar.destroy()
                self.janela_transacoes.lift()

    def janela_depositar(self):
        # Seleção
        self.selecionados = self.treeViewe_Transacoes.selection()
        # Verifica se so uma linha foi selecionada
        if (len(self.selecionados) > 1):
            messagebox.showinfo('Aviso', 'Selecione apenas um para editar')
        elif (len(self.selecionados) == 0):
            messagebox.showwarning("Se liga heim!", "Tá querendo depositar dinheiro onde? Selecione uma conta por favor!")
        else:
            self.lista_selecionados = self.treeViewe_Transacoes.item(self.selecionados)  # Busca os valores 'values' dentro do selecionado
            #Pegando referencia do objeto selecionado
            self.Id_Objeto_Atual = (self.lista_selecionados['values'][0])
            for x in self.banco_em_Transacoes.get_Contas:
                if x.get_Numero == self.Id_Objeto_Atual:
                    self.objeto_atual = x

            #Verificando o Status
            if(self.objeto_atual.get_Status == "Encerrada"):
                messagebox.showwarning("Se liga Heim!", "Você não pode sacar de contas encerradas")
                self.objeto_atual.deposita(1)
            else:
                self.top_depositar = tk.Toplevel()
                self.top_depositar.grab_set()
                self.top_depositar.title("Depositar")
                self.top_depositar.resizable(False, False)

                # Label
                self.lbl_dpositar = tk.Label(self.top_depositar, text='Digite o valor de deposito:')

                # Botão
                self.btn_depositar = tk.Button(self.top_depositar, text='Depositar', command=self.confirmar_deposito)

                # Ent
                self.ent_depositar = tk.Entry(self.top_depositar, width=30)

                # Sets
                self.lbl_dpositar.grid(row=0, column=0)
                self.ent_depositar.grid(row=0, column=1)
                self.btn_depositar.grid(row=1, column=1)

                self.Id_Objeto_Atual = (self.lista_selecionados['values'][0])

    def confirmar_deposito(self):
        valor_de_deposito = (self.ent_depositar.get()).strip()
        valor_de_deposito = valor_de_deposito.replace(',','.')

        # Get Ent
        if (valor_de_deposito == ''):
            messagebox.showinfo('Se liga heim!', 'Todos campos são obrigatórios')
            self.top_depositar.grab_set()
            self.janela_transacoes.lift()
            self.top_depositar.lift()

        elif (not verifica_digitos.Verificar_Digitos(valor_de_deposito)):
            messagebox.showinfo('Aviso', 'O valor a ser depositado deve conter apenas digitos!')
            self.top_depositar.grab_set()
            self.janela_transacoes.lift()
            self.top_depositar.lift()

        elif (not verifica_digitos.Verifica_Apenas_Um_Ponto(valor_de_deposito)):
            messagebox.showinfo('Aviso', 'O valor a ser depositado deve conter apenas uma virgula ou ponto!')

        elif (not verifica_digitos.Verificar_Espaco(valor_de_deposito)):
            messagebox.showinfo('Aviso', 'O valor a ser depositado não deve conter espaços em branco!')
            self.top_depositar.grab_set()
            self.janela_transacoes.lift()
            self.top_depositar.lift()

        elif (float(valor_de_deposito) < 0):
            messagebox.showinfo('Se liga heim!', 'O valor inserido é negativo!')
            self.top_depositar.grab_set()
            self.janela_transacoes.lift()
            self.top_depositar.lift()
        else:
            valor_de_deposito = float(valor_de_deposito)
            status = self.objeto_atual.deposita(valor_de_deposito)
            self.lbl_saldo_banco.config(text=f'{self.banco_em_Transacoes.get_saldo_banco}')

            # Status do saque
            if (status == 1):

                if (valor_de_deposito == 1):
                    messagebox.showinfo('Se liga heim!', f'Conta {self.objeto_atual.get_Numero}\nDeposito de {valor_de_deposito}$ | Saldo Atual: {self.objeto_atual.get_Saldo}$ | Saldo Anterior: {round( (self.objeto_atual.get_Saldo - valor_de_deposito), 2)}$ \nNão gaste tudo em um só lugar!!!')
                else:
                    messagebox.showinfo('Se liga heim!', f'Conta {self.objeto_atual.get_Numero}\nDeposito de {valor_de_deposito}$ | Saldo Atual: {self.objeto_atual.get_Saldo}$ | Saldo Anterior: {round( (self.objeto_atual.get_Saldo - valor_de_deposito), 2)}$')

                # Alterando o treeview em transacoes
                self.treeViewe_Transacoes.item(self.selecionados, values=(self.objeto_atual.get_Numero, self.objeto_atual.get_Titular, self.objeto_atual.get_Saldo, self.objeto_atual.get_Limite, self.objeto_atual.get_Status))
                # Alterando o treeview em banco
                self.treeViewPai.item(self.selecionados, values=(self.objeto_atual.get_Numero, self.objeto_atual.get_Titular, self.objeto_atual.get_Cliente.get_Conta, self.objeto_atual.get_Saldo, self.objeto_atual.get_Limite, self.objeto_atual.get_Status))

                self.top_depositar.destroy()
                self.janela_transacoes.grab_set()
                self.janela_transacoes.lift()

            elif (status == 2):
                messagebox.showinfo('Operação invalida!', f'Conta {self.objeto_atual.get_Numero}\n O valor de deposito ultrapassa o Limite!\n Limite: {self.objeto_atual.get_Limite}$\n Saldo Atual: {self.objeto_atual.get_Saldo}$')
                self.top_depositar.grab_set()
                self.janela_transacoes.lift()
                self.top_depositar.lift()

            elif (status == 3):
                messagebox.showinfo('Se liga heim!', "É piada ou o que?")
                self.top_depositar.grab_set()
                self.top_depositar.lift()

            elif (status == 4):
                messagebox.showinfo('Se liga heim!', "Operação invalida: Conta Encerradaa!")
                self.top_depositar.destroy()
                self.janela_transacoes.grab_set()
                self.janela_transacoes.lift()

    def janela_extrato(self):
        # Seleção
        self.selecionados = self.treeViewe_Transacoes.selection()
        # Verifica se so uma linha foi selecionada
        if (len(self.selecionados) > 1):
            messagebox.showinfo('Aviso', 'Selecione apenas um!')
        elif (len(self.selecionados) == 0):
            messagebox.showwarning("Se liga heim!", "Tá querendo ver o extrato de quem? Selecione uma conta por favor!")
        else:
            self.lista_selecionados = self.treeViewe_Transacoes.item(self.selecionados)  # Busca os valores 'values' dentro do selecionado
            # Pegando referencia do objeto selecionado
            self.Id_Objeto_Atual = (self.lista_selecionados['values'][0])
            for x in self.banco_em_Transacoes.get_Contas:
                if x.get_Numero == self.Id_Objeto_Atual:
                    self.objeto_atual = x

            self.top_extrato = tk.Toplevel()
            self.top_extrato.title(f'Extrato da conta numero {self.objeto_atual.get_Numero}')
            self.top_extrato.grab_set()
            self.top_extrato.resizable(False, False)

            # Treeview
            colunas = ['data','hora','operacao']
            self.treeView_extrato = ttk.Treeview(self.top_extrato, show='headings', columns=colunas, height=5, selectmode='browse')

            # Cabeçalho
            self.treeView_extrato.heading('data'    , text="Data da Operação")
            self.treeView_extrato.heading('hora'    , text="Hora")
            self.treeView_extrato.heading('operacao', text="Operação")

            self.treeView_extrato.column ('data'    , minwidth=0, width=150)
            self.treeView_extrato.column ('hora'    , minwidth=0, width=150)
            self.treeView_extrato.column ('operacao', minwidth=0, width=500)

            # Scrollbar
            self.scrollbar_extrato = ttk.Scrollbar(self.top_extrato, command=self.treeView_extrato.yview)
            self.treeView_extrato.configure(yscroll=self.scrollbar_extrato.set)

            self.scrollbar_extrato.pack(side=tk.RIGHT, fill=tk.BOTH)
            self.treeView_extrato.pack(side=tk.LEFT, fill=tk.BOTH)

            # Evento para evitar o redimensionamento das colunas
            self.treeView_extrato.bind("<Motion>", 'break')
            listaOperacoes = self.objeto_atual.get_Extrato

            for i in listaOperacoes:
                self.treeView_extrato.insert('', 'end', values=(i['dataOperacao'], i['horaOperacao'], i['operacao']))
