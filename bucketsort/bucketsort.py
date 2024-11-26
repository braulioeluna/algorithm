Lista=[5,7,2,1,9,8,21,11,32,23,16,34,2,1,3,56]

def encontrarMenMay (Lista):
    return min (Lista),max(Lista)

def preparar(n):
    recipientes=[]
    for i in range(n+1):
        recipientes.append(0)
    return recipientes

def llenar (recipientes, Lista,men):
    for e in Lista:
        recipientes[e-men]+=1
    return recipientes

def revisarRecipientes (recipientes, men) :
    LR= []
    for i in range(len (recipientes)):
        for j in range(recipientes [i]):
            LR. append (i+men)
    return LR

def bucketSort (Lista):
    men, may=encontrarMenMay (Lista)
    n=may-men
    recipientes=preparar (n)
    recipientes=llenar(recipientes,Lista,men)
    LR=revisarRecipientes(recipientes,men)
    return LR

print(Lista)
print("----")
print(bucketSort(Lista))