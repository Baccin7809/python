class Conta:
    def __init__(self,__numero,__agencia, __tipo):
        self.__numero = __numero
        self.__agencia = __agencia
        self.__tipo = __tipo

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,numero):
        self.__numero = numero

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self,agencia):
        self.__agencia= agencia
    
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo= tipo

    def __str__(self):
        return f'{self.numero} {self.agencia} {self.tipo}'
    
    