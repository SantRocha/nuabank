from classes.conta_investimento import Conta_Investimento

class Conta_Poupanca(Conta_Investimento):
  def __init__(self, clienteCC, saldoCC, limiteCC):
    super().__init__(clienteCC,saldoCC,limiteCC)
    self._taxaConta = 3
    
    #Metodos
    def atualiza(self, taxa):
      super().atualiza() 
    
