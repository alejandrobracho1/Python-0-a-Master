import random

pares = []
impares = []
tupla = (1,2,3,4,5,6,7,8,9)
numero = 0

for num in tupla:
    aux = random.randint(1,100)
    numero = num * aux
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        
    print("%d x %d = %d"%(num,aux, numero))

print(pares)
print(impares)