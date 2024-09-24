import random

def adivinar_numero():
    # Genera un número secreto entre 1 y 10
    numero_secreto = random.randint(1, 10)
    
    # Pide al usuario que adivine el número
    try:
        adivinanza = int(input("Adivina el número secreto entre 1 y 10: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        return
    
    # Compara la adivinanza con el número secreto
    if adivinanza == numero_secreto:
        print("¡Correcto! Has adivinado el número secreto.")
    else:
        print(f"Incorrecto. El número secreto era {numero_secreto}.")

# Llama a la función para ejecutar el juego
adivinar_numero()
