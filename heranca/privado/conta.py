class Conta:
    def __init__(self,__numero,__agencia, __tipo):
        self.__numero = __numero
        self.__agencia = __agencia
        self.__tipo = __tipo

        
    def __str__(self):
        return f'{self.__numero} {self.__tipo}'
    
    