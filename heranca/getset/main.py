from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoaFisica = PessoaFisica("bruno",'02667725018',20.00)
pessoaJuridica =PessoaJuridica("starley",'1002121',20000.00)
print("MENU PESSOA FISICA: \n")
print(pessoaFisica)
segundaPf = pessoaFisica.segundo_titular = "edu"
print("MENU SEGUNDO TITULAR PESSOA FISICA: \n")
print(segundaPf)

print("MENU PESSOA JURIDICA: \n")

print(pessoaJuridica)
segundaPj = pessoaFisica.segundo_titular = "joe"
print("MENU SEGUNDO TITULAR PESSOA JURIDICA: \n")
print(segundaPj)




