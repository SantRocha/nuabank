class Emprestimo:
    #Variaveis de Classe
    _transacoesBanco = []

    @classmethod
    def transacoes_Banco(cls):
        return cls._transacoesBanco

    #Slots
    __slots__ = ["credor","devedor","emprestimo","qntParcelas","juros","emprestimoR","parcelasR","valorCadaParcela","jurosIndividual","jurosAcumulado","parcelaPlusJuros","devolucao"]

    #Variaveis de Objeto:
    def __init__(self, credor, devedor):
        self.credor       = credor
        self.devedor      = devedor

        #Para Calculos
        self.emprestimoR      = 0
        self.parcelasR        = 0
        self.emprestimo       = 0
        self.qntParcelas      = 0
        self.juros            = 0
        self.valorCadaParcela = 0
        self.jurosIndividual  = 0
        self.jurosAcumulado   = 0
        self.parcelaPlusJuros = 0
        self.devolucao        = 0

    def debug(self):
        print("#00 Valor do juros:     " , self.juros,"%")
        print("#01 Valor cada parcela: " , self.valorCadaParcela)
        print("#02 Juros individual:   " , self.jurosIndividual)
        print("#03 Juros Acumulado:    " , self.jurosAcumulado)
        print("#04 ParcelaPlusJuros:   " , self.parcelaPlusJuros)
        print("#05 Devolução:          " , self.devolucao)

#Getters e Setters
# -----------------------------------------------------------------------------------------------------------------------
    def get_emprestimo_Total(self):
        if(self.emprestimo != 0):
            print("Com um emprestimo de {}$ com taxa de {}% dividido em {} parcelas vocÃª pagara: {}$".format(self.emprestimo, self.juros, self.qntParcelas, self.devolucao))
        else:
            print("Emprestimo invalido!")

#-----------------------------------------------------------------------------------------------------------------------
    def get_Qnt_Parcelas(self):
        if (self.emprestimo != 0):
            #print("Seu emprestimo de {}$ deve ser pago em {} parcelas!".format(self._emprestimo, self.qntParcelas))
            return self.qntParcelas
        else:
            print("Emprestimo invalido!")
    def set_Qnt_Parcelas(self, new_Qnt_Parcelas):
        self.qntParcelas = new_Qnt_Parcelas

#-----------------------------------------------------------------------------------------------------------------------
    def get_Juros(self):
        return self.juros
    def set_Juros(self, new_Juros):
        self.juros = new_Juros

#-----------------------------------------------------------------------------------------------------------------------
    def get_Parcelas_Restantes(self):
        return self.parcelasR
    def Set_Parcelas_Restantes(self, new_Parcelas_Restantes):
        self.parcelasR = new_Parcelas_Restantes

#Metodos de classe

    #Metodo para pegar um emprestimo
    @property
    def get_Emprestimo(self):
        if (self.emprestimoR != 0):
            print("Emprestimo de {}$ da conta N°{} para a conta N°{}".format(self.emprestimo, self.credor.get_Numero, self.devedor.get_Numero))
            return True, self.emprestimo
        else:
            print("Nenhum emprestimo disponivel ainda!")
            return False

    def set_Emprestimo(self, quantoDeEmprestimo, quantasParcelas, quantosJuros):
        self.emprestimo = quantoDeEmprestimo
        self.set_Qnt_Parcelas(quantasParcelas)
        self.set_Juros(quantosJuros)
        self.emprestimoR = self.emprestimo
        foiEmprestado, valorEmprestimo = self.credor.saca(quantoDeEmprestimo)
        pegoEmprestado, valorPego     = (self.devedor.deposita(quantoDeEmprestimo))

        if (quantoDeEmprestimo != 0 and foiEmprestado == True and pegoEmprestado == True):
            print("Emprestimo de {}$ da conta N°000{} para a conta N°000{} efetuado com sucesso!".format(self.emprestimo, self.credor.get_Numero, self.devedor.get_Numero))
            Emprestimo._transacoesBanco.append("Emprestimo de {}$ da conta N°000{} para a conta N°000{} efetuado com sucesso!".format(self.emprestimo, self.credor.get_Numero, self.devedor.get_Numero))
            self.parcelasR = quantasParcelas
            self.valorCadaParcela = self.emprestimo / self.get_Qnt_Parcelas()
            self.jurosIndividual  = self.valorCadaParcela * (self.get_Juros() / 100)
            self.jurosAcumulado   = self.jurosIndividual * self.qntParcelas
            self.parcelaPlusJuros = self.valorCadaParcela + self.jurosIndividual
            self.devolucao        = valorEmprestimo + self.jurosAcumulado
            # self.debug()

        # Ã‰ pra informar que o saque do emprestimo ultrapasa o limite
        elif (quantoDeEmprestimo != 0 and (self.credor.saca(quantoDeEmprestimo)) == False):
            print("Emprestimo invalido: ", end="")
            self.credor.saca(quantoDeEmprestimo)
            Emprestimo._transacoesBanco.append("Tentativa de emprestimo de {}$ da conta N°000{} para a conta N°000{} no valor de {}$ porem o saldo do credor Ã© insuficinte | Saldo: {}$".format(self.emprestimo, self.credor.get_Numero, self.devedor.get_Numero,quantoDeEmprestimo),self.credor.get_Saldo)

        # Ã‰ pra informar que o deposito do emprestimo ultrapasa o limite
        elif (quantoDeEmprestimo != 0 and (self.devedor.deposita(quantoDeEmprestimo)) == False):
            print("Emprestimo invalido: ", end="")
            self.devedor.deposita(quantoDeEmprestimo)
            Emprestimo._transacoesBanco.append("Tentativa de emprestimo de {}$ da conta N°000{} para a conta N°000{} no valor de {}$ porem o deposito extrapola o valor do limite do devedor | Limite: {}$".format(self.emprestimo, self.credor.get_Numero, self.devedor.get_Numero,quantoDeEmprestimo),self.devedor.get_Limite)

        elif (quantoDeEmprestimo == 0):
            print("Emprestimo invalido: emprestimo não pode ser 0")

    #Metodo Para pagar um emprestimo
    def pagaParcela(self, quantasVaiPagar):
        emprestimoFeito, valorEmprestimo = self.get_Emprestimo
        if(emprestimoFeito == True):
            # self.debug()
            if(quantasVaiPagar != 0 and (self.parcelasR - quantasVaiPagar) >=0 ):
                pagoDessaVez   = (self.parcelaPlusJuros * quantasVaiPagar)
                print("Pago dessa vez", pagoDessaVez)
                pagamentoFeito = False
                pagamentoFeito, valorPagamento = self.devedor.saca(pagoDessaVez)
                if(pagamentoFeito == True):
                    self.credor.deposita(valorPagamento)
                    self.parcelasR -= quantasVaiPagar
                    print("Seu pagamento de {} parcelas de {} foi efetuado com sucesso".format(quantasVaiPagar, self.parcelaPlusJuros))
                    if(self.parcelasR != 0):
                        print("Parcelas Restantes: ", self.get_Parcelas_Restantes())

                    else:
                        print("Divida quitada! ;D")


            elif(quantasVaiPagar != 0 and (self.parcelasR - quantasVaiPagar) < 0 ):
                print("Seu pagamento ultrapassa o montante que falta!")

            else:
                print("Impressão nossa ou você está tentando pagar 0 reais? Rum D:<")
        else:
            print("Emprestimo Invalido!")

