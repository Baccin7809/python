from controller import tamanhoLista,media,verificaMulher,verificarAcimaMedia
def leitura(lista,mulheres,acimaMedia):
    cond=1
    
    soma=0

    while cond==1:
        pessoa={}
        pessoa['nome']=str(input("Digite seu nome: "))
        pessoa['sexo']=str(input("Digite seu sexo: "))
        pessoa['idade']=int(input("Digite sua idade: "))
        soma += pessoa['idade']
        lista.append(pessoa)
        
        cond=int(input("1.continuar\n2.finalizar"))

    print("quantidade de pessoas: {}".format(tamanhoLista(lista)))

    print("media: {}".format(media(lista,soma)))

    verificarAcimaMedia(lista,media(lista,soma),acimaMedia)
    print(f"acima da media:{acimaMedia}")
    verificaMulher(lista,mulheres)
    print(f"mulheres: {mulheres}")

lista=[]
mulheres=[]
acimaMedia=[]
leitura(lista,mulheres,acimaMedia)