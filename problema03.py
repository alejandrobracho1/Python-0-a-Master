#Dado 4 números, devolver los números en orden ascendente.


numeros = [4, 2, 3, 1]

for i in range(len(numeros)):
    for j in range(i+1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print(numeros)
        
        
        
        
# Variables | Ingresar Datos.
numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))
numero3 = int(input('Número 3: '))

# Solución

# Hallar el número mayor
if numero1 > numero2 and numero1 > numero3:
    mayor = numero1
else:
    if numero2 > numero1 and numero2 > numero3:
        mayor = numero2
    else:
        mayor = numero3

# Hallar el número menor 
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
else:
    if numero2 < numero1 and numero2 < numero3:
        menor = numero2
    else:
        menor = numero3

# Hallar el número intermedio 
intermedio = (numero1 + numero2 + numero3) - (mayor - menor)

# Mostrar Datos
print(f'Mayor: {mayor}')
print(f'Intermedio: {intermedio}')
print(f'Menor: {menor}')