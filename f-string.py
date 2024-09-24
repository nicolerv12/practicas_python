#ejemplo de uso f-string

nombre="roberto"
edad= 38
    print(f"hola,{nombre}, tienes {edad} años")
#ejemplo de suma f-string
precio1= 78292
precio2= 312
    print(f"El precio total es: ${precio1 + precio2}")
# if dentro de un print
temperatura=30
    print(f"La temperatura esta {"alta" if {temperatura}>25 else "baja"})