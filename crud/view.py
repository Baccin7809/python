from model import Conta
from controller import create, read, update, busca
menu = int(input("1. criar conta \n2. mostrar contas\n3.update\n"))
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
        case 3:
            conta = Conta()
            conta.numero=int(input("digite o id de busca: "))
            flag=busca(conta.numero)
            if flag==1:
                conta.titular=str(input("digite o nome: "))
                conta.saldo=float(input("digite o saldo: "))
                update(conta)
            else:
                print("NAO ENCONTRADO")

    menu = int(input("1. criar conta \n2. mostrar contas\n3.update\n"))
    








