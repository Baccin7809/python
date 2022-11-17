from Model.pessoaJuridica import PessoaJuridica
def create_pj(conta):
    with open('pessoajuridica.txt', 'a') as arquivo:
        arquivo.write(str(conta)+"\n")

def read_pj():
    lista_contas=[]
    contas = open("pessoajuridica.txt", "r") 
    for conta in contas:
        conta=conta.strip()
        contaObjeto = conta.split(";")
        print(contaObjeto)
        pessoaJuridica = PessoaJuridica()
        pessoaJuridica.agencia = contaObjeto[0]
        pessoaJuridica.numero = contaObjeto[1]
        pessoaJuridica.segundoTitular = contaObjeto[2]
        pessoaJuridica.titular = contaObjeto[3]
        pessoaJuridica.cnpj = contaObjeto[4]
        pessoaJuridica.saldoInicial = contaObjeto[5]
        
        
        lista_contas.append(pessoaJuridica)
    contas.close
    return lista_contas
