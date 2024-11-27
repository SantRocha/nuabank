from classes.conta import Conta

class Conta_Corrente(Conta):
  def __init__(self, clienteCC, saldoCC, limiteCC):
    super().__init__(clienteCC,saldoCC,limiteCC)
    self._taxaConta    = 2
    self._taxaDeposito = 0.1
    self._somaSubtrai  = -1
    self._taxa         = 0.05
        
  #Metodos
  def atualiza(self, taxa):
    super().atualiza(taxa)
    
  def valor_imposto(self):
    return self._saldo * self._taxa