from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

menu=0
print("escolha: 1. cadastrar pessoa fisica\n 2.cadastrar pessoa juridica\n")
menu=int(input())
match menu:
    
    case 1:
        
        print("MENU PESSOA FISICA: \n")
        pessoaFisica = PessoaFisica(input('digite nome: '),input('digite cpf: '),input('digite saldo: '))
        
        print(pessoaFisica)
        print("deseja adcionar segundo titular? 1.sim e 2.nao")
        s=int(input())
        if s == 1:
            segundaPf = pessoaFisica.segundo_titular = input('digite nome do 2 titular: ')
            print(segundaPf)
    case 2:
        print("MENU PESSOA JURIDICA: \n")
        pessoaJuridica = PessoaJuridica(input('digite nome: '),input('digite cnpj: '),input('digite saldo: '))
        print(pessoaJuridica)
        s=int(input())
        if s == 1:
             segundaPj = pessoaJuridica.segundo_titular = input('digite nome do segundo titular: ')

             print(segundaPj)
        






