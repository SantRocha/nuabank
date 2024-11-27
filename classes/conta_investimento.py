from classes.conta import Conta

class Conta_Investimento(Conta):
  def __init__(self, clienteCI, saldoCI, limiteCI):
    super().__init__(clienteCI, saldoCI,limiteCI)

  def verifica(self, valor):
    if(valor > 0 and valor < self._limite):
      return 1
    elif(valor <= 0):
      return 2
    else:
      return 3
       
  def atualiza(self, taxa):

    anterior = self._saldo
    AUX_2 = self._saldo * ( ( (taxa/100)* self._taxaConta)  * self._somaSubtrai )
    AUX = self.verifica(self._saldo + AUX_2)
    if(AUX == 1):
      self._saldo = self._saldo + ( (self._saldo * ( (taxa/100)* self._taxaConta) ) * self._somaSubtrai) 
      self._saldo += self._saldo * 0.1
      self._saldo -= 9.99
          
      Conta._transacoesBanco.append (f'{"Conta N°000"} {self.get_Numero} {": Atualização da conta com taxa de"} {taxa} {"%"} {"no valor de"} {round(abs(AUX_2),2)} {"$":<4} {"|":<5} {"Saldo Atual:"} {round(self._saldo, 2):<6} {"$"} {"|"} {"Saldo Anterior:"} {round(anterior,2)} {"$"}')
      
      Conta._saldo_total -= anterior
      Conta._saldo_total += self._saldo
      Conta._saldo_total += self._saldo * 0.1
      Conta._saldo_total -= 9.99

    elif(AUX == 2):
      print(f'Operação invalida: a atualização deixa a conta n° {self.get_Numero} com saldo negativo ou nulo\n')
    elif(AUX == 3):
      print(f'Operação invalida: a atualização da conta n° {self.get_Numero} ultrapassa o limite\n')
    else:
      print("Operação Invalida!")

