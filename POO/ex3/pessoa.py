class Pessoa:
    # Atributos recebendo tipos
    nome = ''
    cpf = ''
    idade = 0
 
    #methodo de acesso aos atributos da classe
    def __str__(self): #Pessoa
        return f' {self.nome} - {self.cpf} - {self.idade}'