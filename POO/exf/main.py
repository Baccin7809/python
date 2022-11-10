from conta import Conta



#objeto da minha classe
conta = Conta(
    str(input("digite o nome do titular")),
    int(input("digite o numero do titular")),
    float(input("digite o saldo")),
    float(input("digite o limite"))
)
conta.gerarExtrato()
conta.depositar(float(input("digite o valor do deposito: ")))
conta.sacar(float(input("digite o valor do saque: ")))
conta2=Conta(
    str(input("digite o nome do titular")),
    int(input("digite o numero do titular")),
    float(input("digite o saldo")),
    float(input("digite o limite"))
)
conta.transferir(float(input("digite o valor da transferencia: ")),conta,conta2)

    
#imprimindo valores
