#Dado un rango de números enteros num. inicial y num. final, obtener la cantidad 
# de números positivos y negativos que existen en el rango.

n = int(input('Ingrese primer numero: ')) #2
nf = int(input('Ingrese numero final: ')) #7

i = 0
num_pos = 0
num_neg = 0

i = n + 1
while i <= nf:
        if i <= 0:
            num_neg += 1
        else:
            num_pos += 1
        i += 1

print(f"La cantidad de numeros negativos es: {num_neg}")
print(f"La cantidad de numeros positivos es: {num_pos}")





valor1 = int(input('Número inicial: '))
valor2 = int(input('Número final: '))
valor2 += 1
cantidadPositivos = 0
cantidadNegativos = 0

# Solución
for numero in range(valor1, valor2):
    if numero % 2 == 0 :
        cantidadPositivos += 1  
    else:
        cantidadNegativos += 1


# Mostrar Datos
print('Cantidad POSITIVOS: ', cantidadPositivos)
print('Cantidad NEGATIVOS: ', cantidadNegativos)
