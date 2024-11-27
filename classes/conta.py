import abc
import time as tm

class Conta(abc.ABC):
    #Atributos de Classe:
    numero_Conta     = 1
    _transacoesBanco = []
    _saldo_total     = 0

    @classmethod
    def transacoes_Banco(cls):
        return cls._transacoesBanco

    @classmethod
    def get_Total_Contas(cls):
        return cls.numero_Conta

    @classmethod
    def get_Total_Saldo_Banco(cls):
        return cls._saldo_total
  
    #Atributos de Objeto
    def __init__(self,clienteC,saldoC,limiteC,):
        self._numero          = Conta.numero_Conta
        self._cliente         = clienteC
        self._saldo           = saldoC
        self._limite          = limiteC
        self._extrato_pessoal = []
        self._status          = "Ativa"
        self._taxaConta       = 1
        self._taxaDeposito    = 0 
        self._somaSubtrai     = 1

        Conta.numero_Conta   += 1
        Conta._saldo_total   += self._saldo

    #Str
    def __str__(self):
      return f'{"Conta N°: "}{self.get_Numero:<2} {"|"} {self.get_Titular:<10} {"|"} {self.get_Saldo} {"$":<3} {"|"} {self.get_Limite} {"$":<3}'

    #Metodos do Objeto
    def saca(self, valorDeSaque):
        self.operacoes = {'dataOperacao': '', 'horaOperacao': '', 'operacao': ''}

        if self._status == "Ativa":
            valor_com_taxa = valorDeSaque + (valorDeSaque * 0.05)

            if valor_com_taxa <= self._saldo and valorDeSaque != 0:
                # Edições
                self._saldo = round((self._saldo - valor_com_taxa), 2)
                Conta._transacoesBanco.append(self.operacoes)
                Conta._saldo_total -= valor_com_taxa

                # Registro
                self.operacoes['dataOperacao'] = tm.strftime('%D')
                self.operacoes['horaOperacao'] = tm.strftime('%H:%M:%S %p')
                self.operacoes['operacao'] = f'Saque de {valorDeSaque}$ (com taxa 5%: {valor_com_taxa}$) | Saldo Atual: {self._saldo}$ | Saldo Anterior: {self._saldo + valor_com_taxa}$'
                self._extrato_pessoal.append(self.operacoes)
                return 1

            elif valorDeSaque > self._saldo and valorDeSaque != 0:
                # Registro
                self.operacoes['dataOperacao'] = tm.strftime('%D')
                self.operacoes['horaOperacao'] = tm.strftime('%H:%M:%S %p')
                self.operacoes['operacao'] = f'Tentativa de Saque de {valorDeSaque}$ porém saldo insuficiente! | Saldo Atual: {self._saldo}$'
                self._extrato_pessoal.append(self.operacoes)
                Conta._transacoesBanco.append(self.operacoes)
                return 2
            else:
                # Registro
                self.operacoes['dataOperacao'] = tm.strftime('%D')
                self.operacoes['horaOperacao'] = tm.strftime('%H:%M:%S %p')
                self.operacoes['operacao'] = f'Tentativa de Saque de {valorDeSaque}$'
                self._extrato_pessoal.append(self.operacoes)
                Conta._transacoesBanco.append(self.operacoes)
                return 3
        else:
            # Registro
            self.operacoes['dataOperacao'] = tm.strftime('%D')
            self.operacoes['horaOperacao'] = tm.strftime('%H:%M:%S %p')
            self.operacoes['operacao'] = f'Tentativa de Saque | Operação inválida: Conta Encerrada!'
            self._extrato_pessoal.append(self.operacoes)
            Conta._transacoesBanco.append(self.operacoes)
            return 4

        
    def deposita(self, valorDeDeposito):
        self.operacoes = {'dataOperacao': '','horaOperacao': '', 'operacao': ''}
        if self._status == "Ativa":
            valor_com_taxa = valorDeDeposito - (valorDeDeposito * self._taxaDeposito)  # Aplica a taxa de depósito

            if (self._saldo + valor_com_taxa) <= self._limite and valorDeDeposito != 0:
                # Edição
                Conta._saldo_total += valor_com_taxa
                self._saldo = round((self._saldo + valor_com_taxa), 2)

                # Registro
                self.operacoes['dataOperacao'] = tm.strftime('%D')
                self.operacoes['horaOperacao'] = tm.strftime('%H:%M:%S %p')
                self.operacoes['operacao'] = f'Deposito de {valorDeDeposito}$ (com taxa {self._taxaDeposito*100}%: {valor_com_taxa}$) | Saldo Atual: {self._saldo}$ | Saldo Anterior: {self._saldo - valor_com_taxa}$'
                self._extrato_pessoal.append(self.operacoes)
                Conta._transacoesBanco.append(self.operacoes)
                return 1

            elif (self._saldo + valor_com_taxa) > self._limite and valorDeDeposito != 0:
                # Registro
                self.operacoes['dataOperacao'] = tm.strftime('%D')
                self.operacoes['horaOperacao'] = tm.strftime('%H:%M:%S %p')
                self.operacoes['operacao'] = f'Tentativa de Deposito de {valorDeDeposito}$ porém o valor ultrapassa o Limite! | Limite: {self.get_Limite}$'
                self._extrato_pessoal.append(self.operacoes)
                Conta._transacoesBanco.append(self.operacoes)
                return 2

            else:
                # Registro
                self.operacoes['dataOperacao'] = tm.strftime('%D')
                self.operacoes['horaOperacao'] = tm.strftime('%H:%M:%S %p')
                self.operacoes['operacao'] = f'Tentativa de Deposito de {valorDeDeposito}$'
                self._extrato_pessoal.append(self.operacoes)
                Conta._transacoesBanco.append(self.operacoes)
                return 3
        else:
            # Registro
            self.operacoes['dataOperacao'] = tm.strftime('%D')
            self.operacoes['horaOperacao'] = tm.strftime('%H:%M:%S %p')
            self.operacoes['operacao'] = f'Tentativa de Deposito | Operação inválida: Conta Encerrada!'
            self._extrato_pessoal.append(self.operacoes)
            Conta._transacoesBanco.append(self.operacoes)
            return 4


    def daEmprestimo(self, valorDeEmprestimo):
        if(valorDeEmprestimo <=self._saldo):
            print("Emprestimo de {}$ efetuado com sucesso!".format(valorDeEmprestimo))
            self.saca(valorDeEmprestimo)
            return valorDeEmprestimo
        else:
            print("Conta N°000{}:Tentativa de Emprestimo de {}$ porem saldo insuficiente! | Saldo Atual: {}$".format(self.get_Numero,valorDeEmprestimo, self._saldo))
            return 0
    def pegaEmprestimo(self, quantoQuer):
        return quantoQuer

    #Metodos Abstratos
    @abc.abstractmethod
    def atualiza(self, taxa):
      pass

    #Getters -----------------------------------------------------------------------------------------------------------
    @property
    def get_Numero(self):
        return self._numero
    @property
    def get_Saldo(self):      
        return round(self._saldo,2)
    @property
    def get_Limite(self):
        return self._limite
    @property
    def get_Titular(self):
        return self._cliente.nome
    @property
    def get_Endereco(self):
        return self._cliente.endereco
    @property
    def get_Cpf(self):
        return self._cliente.cpf
    @property
    def get_Idade(self):
        return self._cliente.idade
    @property
    def get_Cliente(self):
        return self._cliente
    @property
    def get_Status(self):
        return self._status
    @property
    def get_Extrato(self):
        return self._extrato_pessoal

    #Setters -----------------------------------------------------------------------------------------------------------
    def set_Limite(self, newLimite):
        self._limite = newLimite
    def set_Saldo (self, newSaldo):
      self._saldo = newSaldo
    def set_Status (self, newStatus):
        self._status = newStatus
