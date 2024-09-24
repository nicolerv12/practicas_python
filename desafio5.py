def calcular_precio_final(precio_inicial, descuento):
    # Validación del descuento
    if descuento < 0 or descuento > 100:
        return "Descuento inválido"
    
    # Cálculo del precio final
    precio_final = precio_inicial * (1 - descuento / 100)
    return precio_final

# Solicitar entrada del usuario
def main():
    try:
        precio_inicial = float(input("Ingrese el precio del producto: "))
        descuento = float(input("Ingrese su descuento: "))
        
        # Obtener el precio final usando la función
        resultado = calcular_precio_final(precio_inicial, descuento)
        
        # Mostrar el resultado
        if isinstance(resultado, str):
            print(resultado)  # Si el resultado es un mensaje de error
        else:
            print(f"El precio final del producto es: {resultado:.2f}")
    
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
