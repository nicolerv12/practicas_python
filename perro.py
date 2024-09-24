class Dog:
    def __init__(self, name, raza,pasear):
        self.name= name
        self.raza = raza
        self.pasear=pasear
    def ladrar(self):
        print(f"el perro {self.name},ladra asi wuawau, y tiene raza de {self.raza}")
    
    #main
perro =Dog("jefazo", "labrador")
perro.ladrar()

