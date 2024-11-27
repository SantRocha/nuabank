import abc 

class TributavelInterface(abc.ABC):
  """Classe que contém operações de um objeto autenticável As
  subclasses concretas devem sobrescrever o método valor_imposto.
  """
  @abc.abstractclassmethod
  def valor_imposto():
    """aplica taxa de imposto sobre um determinado valor do objeto"""
    pass