from model import Conta
from controller import create, read
menu = int(input("1. criar conta \n2. mostrar contas\n3.sair\n"))
while(menu!=0):
    match menu:
        case 1:
            conta = Conta()
            conta.titular=str(input("digite o nome: "))
            conta.numero=int(input("digite o numero: "))
            conta.saldo=float(input("digite o saldo: "))
            create(conta)
        case 2:
            
            lista_conta = read()
            print(lista_conta)
            print("*"*30)
            for c in lista_conta:
                print(c)
    menu = int(input("1. criar conta \n2. mostrar contas\n3.sair"))
    








