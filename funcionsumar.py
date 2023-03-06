'''def sumar(*args):
    
    suma = 0
    for n in args:
        suma += n
    return suma

suma_total = sumar(1,2,3,4,5,6)

print("La suma total es: ", suma_total)'''


def sumar(*args, **kwargs):
    
    suma = 0
    for n in args:
        suma += n
    return suma, kwargs

suma_total, datos = sumar(2,6,8,7, nombre = "Enrique", edad = '25')

print(suma_total)
print(datos)


