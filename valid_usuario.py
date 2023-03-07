#Programa que valida nombre de usuarios 
#  El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
#  El nombre de usuario debe ser alfanumérico
#  Nombre de usuario con menos de 6 caracteres, retorna el mensaje “El nombre de usuario debe contener al menos 6 caracteres”
#  Nombre de usuario con más de 12 caracteres, retorna el mensaje “El nombre de usuario no puede contener más de 12 caracteres”
#  Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje “El nombre de usuario puede contener solo letras y números”
# Nombre de usuario válido, retorna True


def validar_usuario(usuario):
    if (6 <= len(usuario)) and (len(usuario) <= 12):
        if (usuario.isalpha()):
            return usuario.isalpha()
        else:
            print("El nombre de usuario puede contener solo letras y números! ")
        
    else:
        print("El usuario debe contener de 6-12 carcateres. ")

usuario = input("Ingrese el nombre de usuario: ")

validar_usuario(usuario)

