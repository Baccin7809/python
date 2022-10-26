from controller import validarMedia
def leitura():
    aluno={}
    aluno['nome']=str(input("Digite seu nome: "))
    aluno['nota1']=int(input("Digite sua primeira nota: "))
    aluno['nota2']=int(input("Digite sua segunda nota: "))
    aluno['nota3']=int(input("Digite sua terceira nota: "))
    print(validarMedia(aluno))

leitura()