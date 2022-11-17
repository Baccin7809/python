class Conta:
    __agencia = 'blumenau'
    __numero = 7809
   

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    def __str__(self):
        return f'{self.agencia};{self.numero}'