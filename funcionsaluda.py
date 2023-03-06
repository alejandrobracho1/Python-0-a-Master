def saludar():
    nombre = input(">>> Cual es tu nombre? ")
    edad = input(">>> Que edad tienes? ")
    #print("Hola Bienvenido")
    #print(f"Como estas hoy: {nombre}")
    return 'Hola Bienvenido', nombre , edad 

#valores = saludar()
saludo, nombre, edad = saludar()

#print(valores)
print(saludo)
print(nombre, edad)
