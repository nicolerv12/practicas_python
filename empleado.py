class Empleado:
    def __init__(self, nombre, salario):
        self.nombre=nombre #publico
        self._departamento= None #protegido
        self.__salario=salario #privado
        
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("salario debe ser positivo")
    
    def _asignar_departamento(self,departamento):
        self.departamento = departamento
    
    def _calcular_bonus(self):
        return self.__salario * 0.1
    
#main
empleado=Empleado("roberto",200)
print(Empleado.nombre) #acceso directo a atributo publicp
empleado.salario=550 #uso setter
print(empleado.salario) #uso getter
empleado._asignar_departamento("ventas") #uso protegio
print(empleado.__salario)
