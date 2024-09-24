# Clase Coche
class Coche:
    def __init__(self, marca, modelo,anio):
        self.marca =marca
        self.modelo = modelo
        self.anio = anio
    def describir(self):
        return f"Coche: {self.marca} ,\nModeloe{self.modelo},\nanio:{self.anio}"
    def arrancar(self):
        return f"el {self.marca},{self.modelo} esta arrancando"  
#clase moto    
class Moto:
    def __init__(self, marca, modelo,anio):
        self.marca=marca
        self.modelo=modelo
        self.anio= anio
    def mostrar_detalle(self): 
        return f"Coche: {self.marca} ,\nModeloe{self.modelo},\nanio:{self.anio}"
    def encender(self):
        return f"La moto es: {self.marca},{self.modelo} esta arrancando"   
          
#Main 
#invocar las clase coche   
mi_coche =Coche("Toyota","Yaris","2017")#Crear objeto coche
print(mi_coche.describir())
print(mi_coche.arrancar())

mi_moto = Moto("Yamaha","XR","2020")
mi_moto2 = Moto("Ducatti","Multiestraba","2023")
print(mi_moto.mostrar_detalle())
print(mi_moto2.mostrar_detalle())
