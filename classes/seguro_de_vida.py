class Seguro_De_Vida():
  def __init__(self, numero, valor, titular):
    self._numero  = numero
    self._valor   = valor
    self._titular = titular
    self._taxa    = 0.05
    
  def valor_imposto(self):
    return (self._valor * self._taxa) + 34