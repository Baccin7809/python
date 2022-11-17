from Model.pessoaFisica import PessoaFisica
def create_pf(conta):
    with open('pessoafisica.txt', 'a') as arquivo:
        arquivo.write(str(conta)+"\n")

def read_pf():
    lista_contas=[]
    contas = open("pessoafisica.txt", "r") 
    for conta in contas:
        conta=conta.strip()
        contaObjeto = conta.split(";")
        print(contaObjeto)
        pessoaFisica = PessoaFisica()
        pessoaFisica.agencia = contaObjeto[0]
        pessoaFisica.numero = contaObjeto[1]
        pessoaFisica.segundoTitular = contaObjeto[2]
        pessoaFisica.titular = contaObjeto[3]
        pessoaFisica.cpf = contaObjeto[4]
        pessoaFisica.saldoInicial = contaObjeto[5]
        
        
        lista_contas.append(pessoaFisica)
    contas.close
    return lista_contas
