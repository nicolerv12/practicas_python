class Animal:
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        return "Gua"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"
def animal_sonido(objeto):
    print(objeto.hacer_sonido())
    
perro=Perro()
gato=Gato()
vaca=Vaca()

animal_sonido(perro)
animal_sonido(gato)
animal_sonido(vaca)


