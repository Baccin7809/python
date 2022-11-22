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

def busca(find):
    contas = open("contas.txt", "r") 
    for conta in contas:
        conta=conta.strip()
        contaObjeto = conta.split(";")
        if find == int(contaObjeto[1]):
            flag=1
            return flag
        else:
            flag = 0
            return flag


def update(conta_update:Conta):
    lista_contas=[]
    contas = open("contas.txt", "r") 
    for conta in contas:
        conta=conta.strip()
        contaObjeto = conta.split(";")
        if conta_update.numero == int(contaObjeto[1]):
            lista_contas.append(conta_update)
            
        else:
            lista_contas.append(conta)
    
    contas.close
    contas = open("contas.txt", "w") 
    contas.writelines(str(lista_contas))
    contas.close

       
    
    
    
    
    

