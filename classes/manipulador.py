from tributavel import TributavelInterface

class Manipulador(TributavelInterface):
  
  def calcular_impostos(lista_tributaveis):
    total = 0
    for tr in lista_tributaveis:
      total += tr.valor_imposto()
    return total