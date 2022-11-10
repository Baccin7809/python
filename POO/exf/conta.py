class Conta:
    # Atributos recebendo tipos
  
    
    def __init__(self,titular,numero,saldo,limite):
        self.__titular=titular
        self.__numero=numero
        self.__saldo=saldo
        self.__limite=limite
        


    #methodo de acesso aos atributos da classe
    #def __str__(self): #Conta
    #   return f' {self.titular} - {self.numero} - {self.saldo} - {self.limite}'
    def set_limite(self,limite):
        self.__limite=limite
    def get_limite(self,limite):
        return self.__limite   
    def gerarExtrato(self):
        print(f'{self.titular} - {self.numero} - {self.saldo} - {self.limite}')

    def depositar(self,valor):
        self.saldo += valor

        print(f'saldo atual: {self.saldo}')
    def sacar(self,valor):
        self.saldo -= valor

        print(f'saldo atual: {self.saldo}')

    def transferir(self, valor, origem, destino ):
        origem.sacar(valor)
        destino.depositar(valor)
        