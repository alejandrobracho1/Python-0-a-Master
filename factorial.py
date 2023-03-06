def factorial(n):
    print("Valor inicial: ", n)
    if n > 1:
        n = n * factorial(n-1)
    print("Valor Final: ", n)
    return n

numero = int(input(">>> Ingrese un numero: "))
f = factorial(numero)

print("Su factorial es: ", f)