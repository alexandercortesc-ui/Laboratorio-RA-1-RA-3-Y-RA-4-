from json import dumps, loads

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
        if usuario["ID"] == id_ingresado:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        if usuario_encontrado["contraseña"] == contrasena_ingresada:
            usuario_encontrado['sesion_activa'] = True
            print(f"Inicio de sesión exitoso. ¡Bienvenido, {usuario_encontrado['nombre']}!")
            print("Estado de la sesión:", usuario_encontrado)
            return usuario_encontrado
        else:
            print("Error: Contraseña incorrecta. Por favor, intente de nuevo.")
    else:
        print("Error: El usuario no se encuentra registrado.")
    return None

# --- Reto 5: Gestión de consultas médicas ---
def agendar_consulta(registros_existentes, usuario_logueado):
    """
    Permite al usuario agendar una consulta médica.
    """
    # 1. El paciente debe haber iniciado una sesión
    if not usuario_logueado or usuario_logueado['rol que desempeña'] != 'paciente':
        print("\nError: Debe iniciar sesión como paciente para agendar una consulta.")
        return

    print("\n--- Agendar nueva consulta ---")

    # 2. El médico debe existir como usuario registrado y tener el rol 'médico'
    id_medico = int(input("Ingrese el ID del médico con el que desea la consulta: "))
    medico_encontrado = None
    for usuario in registros_existentes:
        if usuario["ID"] == id_medico and usuario["rol que desempeña"] == "médico":
            medico_encontrado = usuario
            break

    if not medico_encontrado:
        print("Error: El médico con ese ID no está registrado o no tiene el rol de médico.")
        return

    # 3. Solicitar detalles de la consulta
    fecha = input("Ingrese la fecha de la consulta (ej. '2025-12-25'): ")
    hora = input("Ingrese la hora de la consulta (ej. '15:30'): ")
    motivo = input("Ingrese el motivo de la consulta: ")

    # Crear el diccionario de la consulta
    nueva_consulta = {
        "paciente_id": usuario_logueado['ID'],
        "medico_id": medico_encontrado['ID'],
        "fecha": fecha,
        "hora": hora,
        "motivo": motivo
    }

    # 4. Almacenar la consulta en un archivo JSON
    archivo_consultas = "consultas.txt"
    with open(archivo_consultas, 'a') as archivo_escritura:
        consulta_serializada = dumps(nueva_consulta)
        archivo_escritura.write(consulta_serializada + "\n")
        print("¡Consulta agendada con éxito!")

# ----------------- INICIO DEL CODIGO PRINCIPAL -----------------

# Solicita el nombre del archivo de usuarios
archivo_usuarios = input("Ingrese el nombre del archivo de usuarios (con extensión .txt): ")

# Carga los registros existentes o crea el archivo si no existe
registros_existentes = []
try:
    with open(archivo_usuarios, 'r') as archivo_lectura:
        for linea in archivo_lectura:
            linea = linea.strip()
            if linea:
                try:
                    registros_existentes.append(loads(linea))
                except loads.JSONDecodeError:
                    pass
except FileNotFoundError:
    print("El archivo no existe, se creará uno nuevo.")

# Variable para mantener el usuario logueado
usuario_actual = None

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Agendar consulta médica")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        cantidad = int(input("¿Cuántos usuarios desea registrar?: "))
        with open(archivo_usuarios, 'a') as archivo_escritura:
            for i in range(cantidad):
                print(f"\n Registro de la persona {i + 1}:")
                usuario = datos()
                usuario_serializado = dumps(usuario)

                # Verifica si el ID ya existe
                existe_id = any(u["ID"] == usuario["ID"] for u in registros_existentes)
                if existe_id:
                    print(f" Error: El usuario con ID {usuario['ID']} ya está registrado.")
                else:
                    archivo_escritura.write(usuario_serializado + "\n")
                    registros_existentes.append(usuario)
                    print(f" Registro exitoso para {usuario['nombre']}.")
    
    elif opcion == '2':
        # La función retorna el usuario, por eso se asigna a usuario_actual
        usuario_actual = iniciar_sesion(registros_existentes)

    elif opcion == '3':
        # Se llama a la función con el usuario que está actualmente logueado
        agendar_consulta(registros_existentes, usuario_actual)

    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Por favor, intente de nuevo.")