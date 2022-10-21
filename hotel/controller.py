import os


def fazerCheckin(cliente):
    with open('hotel/hotel.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+"\n")

        
def relatorioHospedes():
    with open('hotel/hotel.txt') as arquivo:  
        print(arquivo.read())


def procurarHospedes(clienteFind):
    index=0
    flag=0
    arquivo = open("hotel/hotel.txt", "r") 
    for line in arquivo:
        index +=1
        if clienteFind == eval(line)['nome']:
            print(line)
            flag =1
    if flag == 0:
        print("Cliente não encontrado")
        

def fazerCheckout(clienteFind):
    index=0
    flag=0
    arquivo = open("hotel/hotel.txt", "r") 
    for line in arquivo:
        index +=1
        if clienteFind == eval(line)['nome']:
            chave = index
            flag =1
    arquivo.close()
    if flag == 0:
        print("Cliente não encontrado")
    
    else:
        try:
            with open('hotel/hotel.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                
          
                # pointer for position
                ptr = 1
      
                # opening in writing mode
                with open('hotel/hotel.txt', 'w') as fw:
                    for line in lines:
                
                        # we want to remove 5th line
                        if ptr != chave:
                            fw.write(line)
                        ptr += 1
            print("Deleted")
      
        except:
            print("Oops! someting error")
    
    
    
    
