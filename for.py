#recorriendo una lista
frutas =["Platano", "Manzana", "Sandia", "Pera"]
print(frutas)
for fruta in frutas:
    print(f"El nombre de la fruta es: {fruta}")
    
#recorriendo una palabra   
palabra= "Python" 
for letra  in palabra:
    print(f"esta es una letra de la palabra :{letra.upper()}")

#recorriendo un dictionario
estudiante= {"Matias":10, "Roberto":7, "Axel":9}
for nombre in estudiante:
    print(nombre)
    
for nombre,nota in estudiante.items():
    print(f"{nombre} tiene una calificacion de {nota}")
    
# recorriendo numeros
numeros=[23,76,34,89,90,100,90] 
suma=0
for numero in numeros:
    suma += numero # suma= numero + suma 
print(f"la suma de los numero es:{suma}") 
print(f"numero de de elemento en numeros :{len(numeros)}")
media= suma / len(numeros)  
print(f"la media es: {media}")
#sumar valores de un diccionario
ventas ={"enero": 1000, "febrero":1500 , "marzo":1200}
total_ventas=0
for mes, cantidad in ventas.items():
    total_ventas += cantidad #totalventas= cantidad + totalventas
print(f"El total de la ventas es {total_ventas}")   

numbers=[1,2,3,4,5,7,8,9,10,11,12,13,14,15] 
pares=[]
for number in numbers:
    if number % 2 == 0:
       pares.append(number) 
print(f"Numero pares{pares}")

#usando break
nums=[10,20,30,50,20,-5]
for num in nums:
    if num <= 0:
        print(f"El numero{num} no es positivo")
        break
else:
    print("todo los numero son positivos")


