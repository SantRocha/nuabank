import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from classes.conta_poupanca import Conta_Poupanca

class Cores:
  def __init__(self, master):
    #Instancia da Classe banco ----------------------------
    self.janelaCores = master
    self.janelaCores.title("Cores")

    #Widgets-----------------------------------------------

    #Labels
    self.cor1 = tk.Label(self.janelaCores, text='#ae6a47', bg='#8ea091')
    self.cor2 = tk.Label(self.janelaCores, text='#caa05a', bg='#caa05a')
    self.cor3 = tk.Label(self.janelaCores, text='#F18A01', bg='#F18A01')
    self.cor4 = tk.Label(self.janelaCores, text='#8b4049', bg='#8b4049')
    self.cor5 = tk.Label(self.janelaCores, text='#543344', bg='#543344')
    self.cor6 = tk.Label(self.janelaCores, text='#515262', bg='#515262')
    self.cor7 = tk.Label(self.janelaCores, text='#63787d', bg='#63787d')
    self.cor8 = tk.Label(self.janelaCores, text='#8ea091', bg='#8ea091')
    
    #Sets --------------------------------------------------
    self.cor1.pack(fill = tk.BOTH)
    self.cor2.pack(fill = tk.BOTH)
    self.cor3.pack(fill = tk.BOTH)
    self.cor4.pack(fill = tk.BOTH)
    self.cor5.pack(fill = tk.BOTH)
    self.cor6.pack(fill = tk.BOTH)
    self.cor7.pack(fill = tk.BOTH)
    self.cor8.pack(fill = tk.BOTH)
