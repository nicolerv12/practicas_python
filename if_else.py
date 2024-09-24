x=int(input("Ingrese un número: "))
if x > 5:
    print("x es mayor que 5")
else:
    print("x  no es mayor que 5")
    
    y=int(input("Ingrese otro número y "))
    if y <10:
        print("y es menor que 10")
    elif y==10:
        print("y es igual a 10")
    elif y < 20:
        print("y es mayor que 10,pero menor que 20")
    else:
        print("y 20 o mayor")
    edad=int(input("Ingrese su edad: "))
    if edad < 18:
        print("debe tener al menos 18 para registrarse")
    elif 18 <= edad <= 120:  
        print("registro exitoso.Bienvenido")
    else:
        print("Edad no valida. por favor ingrese una edad correcta")           