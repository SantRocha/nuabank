
class Cliente:

  IDs = 1
  #Variaveis de Objeto:
  def __init__(self, nomeC, cpfC, enderecoC, senha):
      self.ID       = Cliente.IDs
      self.nome     = nomeC
      self.endereco = enderecoC
      self.cpf      = cpfC
      self.senha    = senha
      self.conta    = "Nenhuma conta associada"
      self.transacao = []

      Cliente.IDs +=1

  #Getters -------------------------------------------------------------------------------------------------------------
  @property
  def get_transacao(self):
      return self.transacao
  @property
  def get_ID(self):
      return self.ID
  @property
  def get_Cpf(self):
      return self.cpf
  @property
  def get_Nome(self):
    return self.nome
  @property
  def get_Endereco(self):
      return self.endereco
  @property
  def get_Senha(self):
    return self.senha
  @property
  def get_Conta(self):
    return self.conta

  #Setters -------------------------------------------------------------------------------------------------------------
  def set_Conta(self, conta):
    self.conta = conta
  def set_Endereco(self, newEndereco):
      self.endereco = newEndereco
  def set_Senha(self, newSenha):
    self.senha = newSenha