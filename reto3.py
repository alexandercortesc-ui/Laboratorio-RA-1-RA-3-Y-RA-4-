from json import dumps

# Función para solicitar los datos del usuario
def datos():
    name = input("Ingrese su nombre completo: ")
    ID = int(input("Ingrese su número de identificación: "))
    cont = int(input("Ingrese su contraseña: "))
    Rol = input("Ingrese su rol (paciente o médico): ")

    # Retorna los datos como diccionario
    return {
        "nombre": name,
        "ID": ID,
        "contraseña": cont,
        "rol que desempeña": Rol
    }

# Solicita el nombre del archivo
archivo = input("Ingrese el nombre del archivo (con extensión .txt): ")

# Abre el archivo en modo 'a' para agregar sin sobrescribir
with open(archivo, 'a') as archivo:
    usuario = datos()
    archivo.write(dumps(usuario) + "\n")

# Muestra los resultados en consola
print("\nResultados finales:")
print(f"Nombre: {usuario['nombre']}, ID: {usuario['ID']}, contraseña: {usuario['contraseña']}, rol: {usuario['rol que desempeña']}")