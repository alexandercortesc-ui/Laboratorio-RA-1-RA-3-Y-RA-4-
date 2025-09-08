name = input("Ingrese su nombre completo: ")
ID = int(input("Ingrese su número de identificación: "))
cont = int(input("Ingrese contraseña: "))
Rol = input("Ingrese su rol (si es paciente o médico): ")
resultado = {
    "nombre": name,
    "ID": ID,
    "contraseña": cont,
    "rol que desempeña": Rol
}
print("\nResultados finales:")
print(f"Nombre: {resultado['nombre']}, ID: {resultado['ID']}, contraseña: {resultado['contraseña']}, rol: {resultado['rol que desempeña']}")