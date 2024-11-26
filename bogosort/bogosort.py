import random as ra
Lista=[5,8,3,4,21,11,33]

def ordenada(Lista):
    for i in range(len(Lista)-1):
        if(Lista[i]>Lista[i+1]):
            return False
    return True

def bogoSort(Lista):
    contador=0
    while(not ordenada(Lista)):
        ra.shuffle(Lista)
        contador+=1
    print(contador, "veces")
    return Lista

print(Lista)
print("---")
print(bogoSort(Lista))