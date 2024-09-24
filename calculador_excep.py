def solicitar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, introduce un número válido.")

def realizar_operacion(a,b,operador):
    try:
        if operador == "+":
            return a + b
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            if b == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            return a / b
        else:
            raise ValueError("Operador no válido.")
    
    except ValueError as e:
        print(e)
        return None
#main


numero1 = solicitar_numero("Ingrese el primer número: ")
numero2 = solicitar_numero("Ingrese el segundo número: ")

operaciones=input("introdcue el operador usar ") 
