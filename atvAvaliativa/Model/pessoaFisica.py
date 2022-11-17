from Model.conta import Conta
class PessoaFisica(Conta):
    
    __segundoTitular = ''
    __titular = ''
    __cpf = ''
    __saldoInicial = 0

    @property
    def segundoTitular(self):
        return self.__segundoTitular
    @segundoTitular.setter
    def segundoTitular(self, segundoTitular):
        self.__segundoTitular = segundoTitular

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def saldoInicial(self):
        return self.__saldoInicial
    @saldoInicial.setter
    def saldoInicial(self, saldoInicial):
        self.__saldoInicial = saldoInicial

    def __str__(self):
        return f'{super().__str__()};{self.segundoTitular};{self.titular};{self.cpf};{self.saldoInicial}' 