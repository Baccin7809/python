class Animal:
    # Atributos recebendo tipos
    especie = ''
    cor = ''
    raca = ''
 
    #methodo de acesso aos atributos da classe
    def __str__(self): #Animal
        return f' {self.especie} - {self.cor} - {self.raca}'