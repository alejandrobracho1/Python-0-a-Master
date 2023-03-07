#Crear un módulo para validación de contraseñas. Dicho módulo, deberá cumplir con
#los siguientes criterios de aceptación:
#  • La contraseña debe contener un mínimo de 8 caracteres
#  • Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico
#  • La contraseña no puede contener espacios en blanco
#  • Contraseña válida, retorna True
#  • Contraseña no válida, retorna el mensaje “La contraseña elegida no es segura”

import string
#numeros = (1,2,3,4,5,6,7,8,9,0)

# Verificar presencia de letras minúsculas, mayúsculas, números y caracteres no alfanuméricos


def validar_pasword(password):
    if (8 <= len(password)):
        
        if (password.isupper() == True):
            print("La contraseña debe tener al menos 1 elemento en minuscula ")
        elif (password.islower() == True):
            print("La contraseña debe tener al menos 1 elemento en mayuscula ")
        elif (password.isalpha() == True):
            print("La contraseña debe tener al menos 1 elemento no alfanumerico ")
        elif (password.isdigit() == False):
            print("La contraseña debe tener al menos 1 numero")
        elif (password.find(" ") != -1):
            print("La contraseña no puede contener espacios en blanco")
        else:
            print("Contraseña Exitosa")
            return True
    else:
        print("La contraseña debe ser mayor a 8 caracteres")

password = input(">>> Ingrese la contraseña: ")

validar_pasword(password)











'''import re

contrasena = ""

def validar_contrasena(contrasena):
    # Comprobar si la contraseña cumple con los criterios de aceptación
    if len(contrasena) < 8:
        return "La contraseña debe tener al menos 8 caracteres"
    elif re.search("[a-z]", contrasena):
        return "La contraseña debe tener al menos una letra minúscula"
    elif not re.search("[A-Z]", contrasena):
        return "La contraseña debe tener al menos una letra mayúscula"
    elif not re.search("[0-9]", contrasena):
        return "La contraseña debe tener al menos un número"
    elif not re.search("[^a-zA-Z0-9]", contrasena):
        return "La contraseña debe tener al menos un caracter no alfanumérico"
    elif re.search("\s", contrasena):
        return "La contraseña no puede contener espacios en blanco"
    else:
        return True

contrasena = input(">>> Ingrese la contraseña: ")
validar_contrasena(contrasena)
'''



'''import string

def validar_contrasena(contrasena):
    # Verificar longitud mínima de la contraseña
    if len(contrasena) < 8:
        return "La contraseña elegida no es segura"

    # Verificar presencia de letras minúsculas, mayúsculas, números y caracteres no alfanuméricos
    categorias = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    if not all(any(c in categoria for c in contrasena) for categoria in categorias):
        return "La contraseña elegida no es segura"

    # Verificar ausencia de espacios en blanco
    if " " in contrasena:
        return "La contraseña elegida no es segura"

    # Si se han cumplido todos los criterios, la contraseña es válida
    return True


contrasena = input(">>> Ingrese la contraseña: ")
validar_contrasena(contrasena)'''


'''import string

def validar_contrasena(contrasena):
    # Verificar longitud mínima de la contraseña
    if len(contrasena) < 8:
        return "La contraseña elegida no es segura"

    # Verificar presencia de letras minúsculas, mayúsculas, números y caracteres no alfanuméricos
    contiene_minusculas = False
    contiene_mayusculas = False
    contiene_numeros = False
    contiene_no_alfanumericos = False
    for caracter in contrasena:
        if caracter.islower():
            contiene_minusculas = True
        elif caracter.isupper():
            contiene_mayusculas = True
        elif caracter.isdigit():
            contiene_numeros = True
        elif caracter in string.punctuation:
            contiene_no_alfanumericos = True
        if all([contiene_minusculas, contiene_mayusculas, contiene_numeros, contiene_no_alfanumericos]):
            break
    else:
        return "La contraseña elegida no es segura"

    # Verificar ausencia de espacios en blanco
    if " " in contrasena:
        return "La contraseña elegida no es segura"

    # Si se han cumplido todos los criterios, la contraseña es válida
    return True


contrasena = input(">>> Ingrese la contraseña: ")
validar_contrasena(contrasena)'''






