def tamanhoLista(lista):
    return len(lista)
def media(lista,soma):
    return soma/len(lista)
    
def verificaMulher(lista,mulheres):
    for i in range(len(lista)):
        if lista[i]['sexo']=='f':
            mulheres.append(lista[i])
    return mulheres
def verificarAcimaMedia(lista,media,acimaMedia):
    for i in lista:
        if i['idade']>= media:
            
            acimaMedia.append(i)
    
    
