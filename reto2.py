from json import dumps

# Función para solicitar los datos del usuario
def datos():
    nombre = input("Ingrese su nombre completo: ")
    identificacion = int(input("Ingrese su número de identificación: "))
    contraseña = int(input("Ingrese su contraseña: "))
    rol = input("Ingrese su rol (paciente o médico): ")

    # Retorna los datos como diccionario
    return {
        "nombre": nombre,
        "ID": identificacion,
        "contraseña": contraseña,
        "rol que desempeña": rol
    }

# Solicita el nombre del archivo y lo abre en modo 'a' (agregar)
archivo = input("Ingrese el nombre del archivo (con extensión .txt): ")
with open(archivo, 'w') as archivo:
    usuario = datos()
    archivo.write(dumps(usuario) + "\n")

# Muestra los resultados en consola
print("\nResultados finales:")
print(f"Nombre: {usuario['nombre']}, ID: {usuario['ID']}, contraseña: {usuario['contraseña']}, rol: {usuario['rol que desempeña']}")