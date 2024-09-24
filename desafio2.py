
nombre = input("Introduce el nombre del contacto: ")
correo = input("Introduce el correo electrónico del contacto: ")
telefono = input("Introduce el número de teléfono del contacto: ")

# Almacenar los datos en un diccionario
persona = {
    "Nombre": nombre,
    "Correo": correo,
    "Teléfono": telefono
}

# Realizar operaciones básicas
caracteres_nombre = len(nombre)

# Imprimir los resultados
print("\nInformación del contacto:")
print(f"Nombre: {persona['Nombre']}")
print(f"Correo: {persona['Correo']}")
print(f"Teléfono: {persona['Teléfono']}")
print(f"Número total de caracteres en el nombre: {caracteres_nombre}")
