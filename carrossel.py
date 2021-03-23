import random 
quantidadeVeiculos = int(input())
numeros = input().split()
numeros = [int(i) for i in numeros]

sequence = 0
lastNumber = None
greaterSequence = None

i = 0
count = 0
while True:
    if lastNumber == numeros[i]:
        sequence = 1 
        lastNumber = numeros[i]
    
    if lastNumber == None or numeros[i] > lastNumber:
        lastNumber = numeros[i]
        sequence += 1
        
    if lastNumber > numeros[i]:
        sequence = 1
        lastNumber = numeros[i]

    if greaterSequence == None or sequence > greaterSequence:
        greaterSequence = sequence

    i += 1
    if i >= quantidadeVeiculos:
        i = 0
        if count == 1:
            break
        count += 1
           

print(greaterSequence)
