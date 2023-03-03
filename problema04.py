#Dado un rango de numeros obtener la cantidad de numeros enteros que contiene 

# Variables | Ingresar Datos.
numeros = []
contador = 0

i = 1 
while i < 5: 
    #numeros[i] = input(">>> Ingrese un numero: ")
    numeros.insert(i-1,input(">>> Ingrese un numero: "))
    i += 1
    
for num in numeros:
    if ('.' not in num):
        contador += 1

'''for num in numeros:
    if isinstance(num, str):
        contador += 1'''

print(f"En la lista hay: {contador} numeros enteros!")
print("En la lista hay: %d numeros enteros!"%(contador))



# definir una lista de números
'''numeros = [1, 2.5, "tres", 4, 5.7, 6]

# iterar sobre los elementos de la lista y verificar si cada elemento es un entero
for num in numeros:
    if isinstance(num, int):
        print(f"{num} es un entero")
    else:
        print(f"{num} no es un entero")'''
        
        
n = int(input('Ingrese primer numero: ')) #2
nf = int(input('Ingrese numero final: ')) #7

i = 0
contador = 0

i = n + 1
while i < nf:
    contador += 1
    i += 1

print('CONTADOR:',contador)
