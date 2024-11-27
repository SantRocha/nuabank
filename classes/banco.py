import re
import time as tm
from classes.conta import Conta
from classes.conta_poupanca import Conta_Poupanca
from classes.conta_corrente import Conta_Corrente
from classes.cliente import Cliente
from classes.emprestimo import Emprestimo

class Banco:
  #Variaveis de Objeto
  def __init__(self, numeroC, nomeC):
      self._numero    = numeroC
      self._nome      = nomeC
      self._contas    = []
      self._contasPop = []
      self._contasCor = []
      self._clientes  = []

      self.transacoesBanco      = Conta.transacoes_Banco()
      self.transacoesEmprestimo = Emprestimo.transacoes_Banco()
    
  #Metodos de Objeto
  def encerrarConta       (self, qualConta):
      if(qualConta.get_Saldo == 0):
        qualConta.set_Limite(0)
        qualConta.set_Status("Encerrada")
        qualConta.get_Cliente.set_Conta("Nenhuma conta associada")
        dicAux = {'dataOperacao': '', 'horaOperacao':'', 'operacao': ''}
        dicAux['dataOperacao']  =  tm.strftime('%D')
        dicAux['horaOperacao'] = tm.strftime('%H:%M:%S %p')
        dicAux['operacao'] = f'Conta Encerrada'
        qualConta.get_Extrato.append(dicAux)
        self.transacoesBanco.append(dicAux)
        return 1
      if(qualConta.get_Saldo < 0):
        dicAux = {'dataOperacao': '', 'horaOperacao':'', 'operacao': ''}
        dicAux['dataOperacao']  =  tm.strftime('%D')
        dicAux['dataTransacao'] = tm.strftime('%H:%M:%S %p')
        dicAux['operacao'] = f'Tentativa de Encerramento de conta | Operação inválida: conta ainda possui dividas!'
        qualConta.get_Extrato.append(dicAux)
        self.transacoesBanco.append(dicAux)
        return 2
      else:
        dicAux = {'dataOperacao': '', 'horaOperacao':'', 'operacao': ''}
        dicAux['dataOperacao']  =  tm.strftime('%D')
        dicAux['dataTransacao'] = tm.strftime('%H:%M:%S %p')
        dicAux['operacao'] = f'Tentativa de Encerramento de conta | Operação inválida: conta ainda possui saldo!'
        self.transacoesBanco.append(dicAux)
        qualConta.get_Extrato.append(dicAux)
        return 3


  def atualizarContas     (self, taxa):
    for i in self._contas:
      i.atualiza(taxa)
      
      
  def criar_cliente       (self,nomeC, enderecoC, cpfC, senha):
    clienteAUX = Cliente(nomeC, enderecoC, cpfC, senha)
    self._clientes.append(clienteAUX)
    return clienteAUX
  
  
  def validaCpf(cpfAnalise):

    if (re.match(r"[\d]{3}.[\d]{3}.[\d]{3}[-][\d]{2}", cpfAnalise)):
        pass
    else:
        return 'formato incorreto'

    cpf_Entrada = list(map(int, re.sub('[.-]', '', cpfAnalise)))
    cpf_Int = cpf_Entrada[:9]
    cpf_Saida = cpf_Entrada

    # Primeira verificação
    soma = 0
    multiplicador = 10

    for i in cpf_Int:
        soma += i * multiplicador
        multiplicador -= 1

    resto = soma % 11
    print(resto)
    if (resto < 2):
        cpf_Int.append(0)
    else:
        cpf_Int.append(11 - resto)

    # Segunda Verificação
    soma = 0
    multiplicador = 11

    for i in cpf_Int:
        soma += i * multiplicador
        multiplicador -= 1

    resto = soma % 11
    if (resto < 2):
        cpf_Int.append(0)
    else:
        cpf_Int.append(11 - resto)

    if (cpf_Int == cpf_Saida):
        return True
    else:
        return False
        
        
  def criar_Conta_Poupanca(self,cliente, saldoInicial, limiteInicial):
    ID_cliente = cliente.get_ID
    for x in self.get_Clientes_SemConta:
        if x.get_ID == ID_cliente:
            nova_conta = Conta_Poupanca(cliente, float(saldoInicial), float(limiteInicial))
            nova_conta.get_Cliente.set_Conta("Conta Poupanca")
            self._contas.append(nova_conta)
            self._contasPop.append(nova_conta)
            return nova_conta
  def criar_Conta_Corrente(self,cliente, saldoInicial, limiteInicial):
    ID_cliente = cliente.get_ID
    for x in self.get_Clientes_SemConta:
        if x.get_ID == ID_cliente:
            nova_conta = Conta_Corrente(cliente, float(saldoInicial), float(limiteInicial))
            nova_conta.get_Cliente.set_Conta("Conta Corrente")
            self._contas.append(nova_conta)
            self._contasCor.append(nova_conta)
            return nova_conta

  #Getters -------------------------------------------------------------------------------------------------------------
  @property
  def get_saldo_banco(self):
      return Conta.get_Total_Saldo_Banco()
  @property
  def get_contas(self):
    return self._contas
  @property
  def get_nome(self):
    return self._nome
  @property
  def get_numero(self):
    return  str(self._numero)
  @property
  def get_clientes(self):
    return self._clientes
  @property
  def get_ID_clientes_semConta(self):
      lista = []
      for i in self._clientes:
          if (i.get_Conta == "Nenhuma conta associada"):
              lista.append(i.get_ID)
      return lista
  @property
  def get_Clientes_SemConta(self):
      lista = []
      for i in self._clientes:
          if (i.get_Conta == "Nenhuma conta associada"):
              lista.append(i)
      return lista
  @property
  def get_Contas_Pop(self):
      return self._contasPop
  @property
  def get_Contas_Cor(self):
      return self._contasCor
  @property
  def get_Contas(self):
      return self._contas
  @property
  def get_Extrato_Banco(self):
      return self.transacoesBanco

  #Setters -------------------------------------------------------------------------------------------------------------
  def set_nome(self, newNome):
    self._nome = newNome
  def set_numero(self, newNumero):
    self._numero = newNumero

