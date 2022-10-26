def validarCT(pessoa):
    if pessoa['carteiraTrabalho'] > 0:
        pessoa['primeiroAno']=int(input("Digite o primeiro ano de contratação: "))
        pessoa['salario']=int(input("Digite o salario: "))
        return pessoa
    else:
        return pessoa