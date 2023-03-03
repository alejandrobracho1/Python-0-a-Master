#Crear un programa que permita convertir una cantidad de segundos en horas, minutos y segundos.

#Análisis: Para la solución de este problema, se requiere que el usuario ingrese un tiempo expresado 
#en segundos y el sistema procesa y obtiene las horas, minutos y segundos restantes.

#Entrada

#Tiempo en segundos (t)

#Salida

#  Horas (h)

#  Minutos (m)

#  Segundos (s)

#Declaracion de variables 
horas = 0.0
minutos = 0.0
segundos = 0.0

#lectura de datos 
segundos = float(input("Ingrese los segundos: "))

#Calculos 
minutos = segundos / 60
horas = minutos / 60

#Salida 
print("- Horas: (%0.2f)"%(horas))
print("- Minutos: (%0.2f)"%(minutos))
print("- Segundos: (%0.2f)"%(segundos))