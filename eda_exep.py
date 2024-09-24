class EdainvalidError(Exception):
    pass
    def verificarEdad(edad):
        if edad < 18:
            raise ValueError("debe ser mayor de 18anios pra refisyrarse")
        return "registro completo"

    try:
        mensaje= verificarEdad(15)
        print(mensaje)

    except ValueError as e:
        print(f"Error{e}")
        
        
        
        