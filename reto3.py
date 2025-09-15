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
archivo = input("Ingrese el nombre del archivo (con extensión .txt): ")

# Carga los registros existentes como texto plano
registros_existentes = []
try:
    with open(archivo, 'r') as archivo_lectura:
        for linea in archivo_lectura:
            registros_existentes.append(linea.strip())
except FileNotFoundError:
    print(" El archivo no existe, se creará uno nuevo.")

# Solicita cuántos usuarios se van a registrar
cantidad = int(input("¿Cuántos usuarios desea registrar?: "))

# Abre el archivo en modo 'a' para agregar nuevos registros
with open(archivo, 'a') as archivo_escritura:
    for i in range(cantidad):
        print(f"\n Registro de la persona {i + 1}:")
        usuario = datos()
        usuario_serializado = dumps(usuario)

        # Verifica si el ID ya existe buscando el texto '"ID": <valor>'
        id_texto = f'"ID": {usuario["ID"]}'
        existe_id = False
        for linea in registros_existentes:
            if id_texto in linea:
                existe_id = True
                print(f" Error: El usuario con ID {usuario['ID']} ya está registrado.")
                break
        if not existe_id:
            archivo_escritura.write(usuario_serializado + "\n")
            registros_existentes.append(usuario_serializado)
            print(f" Registro exitoso para {usuario['nombre']}.")
              