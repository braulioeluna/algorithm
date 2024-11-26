import numpy as np
Lista=np.random. randint (1,50,20)
#Lista= [1,5,7,21, 1, 3,45,43] 
def encontrarPivote(Lista):
    return sum(Lista)/len (Lista)

def encontrarMenMay (Lista,pivote):
    menores= [] 
    mayores= []
    for e in Lista:
        if(e<pivote):
            menores.append(e)
        else:
            mayores.append(e)
    return menores, mayores 
def repetidos (Lista):
    return sum(Lista)/len (Lista)==Lista[0]
def Quicksort (Lista):
    if(len (Lista)>1 and not repetidos (Lista)):
        pivote=encontrarPivote(Lista)
        menores, mayores=encontrarMenMay (Lista, pivote) 
        menores=Quicksort (menores) 
        mayores=Quicksort (mayores) 
        return menores + mayores
    else:
        return Lista
print (Lista)
print("----")
print(Quicksort(Lista))
