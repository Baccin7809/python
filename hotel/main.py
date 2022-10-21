
from time import sleep
from datetime import datetime
from controller import fazerCheckin, fazerCheckout, procurarHospedes, relatorioHospedes

poli ="="*20
print(f"{poli} HOTELZINHA DOS CRIA {poli}")
#menu
menu=1
agora=datetime.now(tz=None)
if agora.hour >=5 and agora.hour<13:
    print("Bom dia")
if agora.hour >=13 and agora.hour<18:
    print("Boa tarde")
else:
    print("Boa noite")
while(menu!=0):
    print("Escolha a opção desejada:\n")
    menu=int(input("1.Fazer checkin\n2.Relatorio hospedes\n3.Procurar hospedes\n4.Fazer checkout\n0.Finalizar atendimento\n"))
    match menu:
        case 1:
            cliente={}
            cliente["nome"]=str(input("Digite seu nome:"))
            cliente["cpf"]=int(input("Digite seu cpf:"))
            cliente["idade"]=int(input("Digite sua idade:"))
            cliente["telefone"]=int(input("Digite seu telefone:"))
            fazerCheckin(cliente)
        case 2:
            relatorioHospedes()
        case 3:
            clienteFind=str(input("Digite o nome desejado:"))
            procurarHospedes(clienteFind)
        case 4:
            clienteFind=str(input("Digite o nome desejado:"))
            fazerCheckout(clienteFind)

