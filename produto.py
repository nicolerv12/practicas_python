class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def mostrar(self):
        return f"el producto es: {self.nombre} \nPrecio: {self.precio},\n-cantidad: {self.cantidad}"
    def agregar_stock(self,cantidad):
        self.cantidad += cantidad
        print(f"se han agregado: {cantidad} unidades de {self.nombre},la cantidad actuale es: {self.cantidad}")
        
    def vender(self,cantidad):
        if cantidad > self.cantidad:
            print(f"No hay suficiente stock de {self.nombre}, solo hay: {self.cantidad}")
        else:
            self.cantidad -= cantidad
            print(f"Se han vendido: {cantidad} unidades de {self.nombre}, la cantidad actuale es: {self.cantidad}")
            
         #main
producto1 = Producto("laptop",1500,10) 
producto2=  Producto("mesa",200,30)

print(producto1.mostrar())
print(producto2.mostrar())
producto1.agregar_stock(10)
print(producto1.mostrar())
producto2.vender(15)
print(producto2.mostrar())
producto1.vender(40)
print(producto1.mostrar())
                    
        