class Extrato:
    #Variaveis de Classe:
    _transacoesBanco = []
    @classmethod
    def transacoes_Banco(cls):
        return cls._transacoesBanco

    #Variaveis de Objeto:
    def __init__(self):
        self.transacoes = []

    def imprime(self, numConta):

        print("Conta N°:", numConta)
        for i in self.transacoes:
            print(i)
        print("___________________________________________________________________________________________________")



