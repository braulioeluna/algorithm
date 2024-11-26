numbers= [54,26,93,17,1,34,50]

def Bubble(numbers):
    for numPasada in range(len(numbers)-1,0,-1):
        for i in range(numPasada):
            if numbers[i]>numbers[i+1]:
                temp = numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=temp
print("numbers: ", numbers)
Bubble(numbers)
print("sort: ", numbers)