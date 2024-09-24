import random

def adivina_el_numero_secreto():
    # Generar un número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    print("Bienvenido al juego de 'Adivina el Número Secreto'!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    while True:
        # Pedir al usuario que adivine el número
        try:
            adivinanza = int(input("Adivina el numero secreto:"))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        # Comparar el número ingresado con el número secreto
        if adivinanza > numero_secreto:
            print("El número secreto es menor. Intenta de nuevo.")
        elif adivinanza < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            print("¡Felicidades! Has adivinado el número secreto.")
            break

# Llamar a la función para iniciar el juego
adivina_el_numero_secreto()

