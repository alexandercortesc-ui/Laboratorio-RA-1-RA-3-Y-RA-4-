from json import dumps

# Función para solicitar los datos del usuario
def datos():
    name = input("Ingrese su nombre completo: ")
    ID = int(input("Ingrese su número de identificación: "))
    cont = int(input("Ingrese su contraseña: "))
    Rol = input("Ingrese su rol (paciente o médico): ")

    return {
        "nombre": name,
        "ID": ID,
        "contraseña": cont,
        "rol que desempeña": Rol
    }

# Solicita el nombre del archivo
archivo = input("Ingrese el nombre del archivo: ")

# Carga los registros existentes como texto plano
registros_existentes = []

# Solicita cuántos usuarios se van a registrar
cantidad = int(input("¿Cuántos usuarios desea registrar?: "))

with open(archivo, 'a') as archivo_escritura:
    for i in range(cantidad):
        print(f"\n Registro de la persona {i + 1}:")
        usuario = datos()
        usuario_serializado = dumps(usuario)

        # Verifica si el ID ya existe en los registros existentes
        existe_id = (["ID"] == usuario["ID"] == registros_existentes)
        if existe_id == registros_existentes:
            print(f" Error: El usuario con ID {usuario['ID']} ya está registrado.")
        else:
            archivo_escritura.write(usuario_serializado + "\n")
            registros_existentes.append(usuario)
            print(f" Registro exitoso para {usuario['nombre']}.")