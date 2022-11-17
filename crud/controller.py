from model import Conta

def create(conta):
    with open('contas.txt', 'a') as arquivo:
        arquivo.write(str(conta)+"\n")

def read():
    lista_contas=[]
    contas = open("contas.txt", "r") 
    for conta in contas:
        conta=conta.strip()
        contaObjeto = conta.split(";")

        conta = Conta()
        conta.titular = contaObjeto[0]
        conta.numero = contaObjeto[1]
        conta.saldo = contaObjeto[2]
        lista_contas.append(conta)
    contas.close
    return lista_contas

