from json import dumps, loads
import os

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

# --- Reto 4: Función de inicio de sesión del usuario ---
def iniciar_sesion(registros_existentes):
    """
    Permite el inicio de sesión de un usuario.
    Verifica que el usuario exista y que la contraseña sea correcta.
    Si es exitoso, agrega un campo 'sesion_activa' al diccionario del usuario.
    """
    print("\n--- Inicio de sesión del usuario ---")
    id_ingresado = int(input("Ingrese su número de identificación: "))
    contrasena_ingresada = int(input("Ingrese su contraseña: "))
    
    usuario_encontrado = None
    for usuario in registros_existentes:
        if usuario.get("ID") == id_ingresado:
            usuario_encontrado = usuario
            break
            
    if usuario_encontrado:
        if usuario_encontrado.get("contraseña") == contrasena_ingresada:
            usuario_encontrado['sesion_activa'] = True
            print(f"Inicio de sesión exitoso. ¡Bienvenido, {usuario_encontrado['nombre']}!")
            # Muestra el diccionario con el nuevo campo para verificar
            print("Estado de la sesión:", usuario_encontrado)
        else:
            print("Error: Contraseña incorrecta. Por favor, intente de nuevo.")
    else:
        print("Error: El usuario no se encuentra registrado.")

# Solicita el nombre del archivo
archivo = input("Ingrese el nombre del archivo (con extensión .txt): ")

# Carga los registros existentes o crea el archivo si no existe
registros_existentes = []
if os.path.exists(archivo):
    with open(archivo, 'r') as archivo_lectura:
        for linea in archivo_lectura:
            linea = linea.strip()
            if linea:
                try:
                    registros_existentes.append(loads(linea))
                except loads.JSONDecodeError:
                    pass
else:
    print("El archivo no existe, se creará uno nuevo.")

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        # Lógica para registrar un usuario
        cantidad = int(input("¿Cuántos usuarios desea registrar?: "))
        with open(archivo, 'a') as archivo_escritura:
            for i in range(cantidad):
                print(f"\n Registro de la persona {i + 1}:")
                usuario = datos()
                usuario_serializado = dumps(usuario)

                # Verifica si el ID ya existe usando any()
                existe_id = any(u.get("ID") == usuario["ID"] for u in registros_existentes)
                if existe_id:
                    print(f" Error: El usuario con ID {usuario['ID']} ya está registrado.")
                else:
                    archivo_escritura.write(usuario_serializado + "\n")
                    registros_existentes.append(usuario)
                    print(f" Registro exitoso para {usuario['nombre']}.")
    
    elif opcion == '2':
        # Llama a la función para iniciar sesión
        iniciar_sesion(registros_existentes)

    elif opcion == '3':
        print("Saliendo del programa. ¡Hasta pronto!")
        break # Esto sale del bucle 'while' y termina el programa

    else:
        print("Opción no válida. Por favor, intente de nuevo.")
