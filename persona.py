class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def description(self):
        return f"el nombre es : {self.nombre}, tiene la edad:  {self.edad}"

class Empleado(Persona):
    def __init__(self, nombre, edad,salario):
        super().__init__(nombre, edad)
        self.salario = salario
        
    def description(self):
        return f"{super().description}y gana {self.salario} dolar al mes"
    
    #main
    empleado=Empleado("roberto",38,500)
    print(empleado.description())
    