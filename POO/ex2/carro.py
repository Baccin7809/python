class Carro:
    # Atributos recebendo tipos
    marca = ''
    modelo = ''
    valor = 0
 
    #methodo de acesso aos atributos da classe
    def __str__(self): #Carro
        return f' {self.marca} - {self.modelo} - {self.valor}'