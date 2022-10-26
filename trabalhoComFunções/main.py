from controller import validarCT
def leitura():
    pessoa={}
    pessoa['nome']=str(input("Digite seu nome: "))
    pessoa['dataNasc']=str(input("Digite sua data de nascimento: "))
    pessoa['carteiraTrabalho']=int(input("Digite sua carteira de trabalho: "))
    print(validarCT(pessoa))

leitura()
        
                
