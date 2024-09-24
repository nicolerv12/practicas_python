
libros = []

def agregar_libro():
    titulo=input("Ingrese el titulo del libro:")
    autor=input("Ingrese el autor del libro:")
    año = input("Ingrese el año de publicación: ")
    libro={"titulo":titulo,"autor":autor, "año":año, "prestado":False}
    libros.append(libro)
    print(f"Libro '{titulo}' agregado exitosamente.")
    
def buscar_libro(titulo):
    for libro in libros:
        if 
    
    



def mostrar_menu():
    print("-------Menu Principal--------")
    print("1.Agregar un libro")
    print("2.buscar un libro")
    print("3.listar todos los libros")
    print("4.registrar un prestamo")
    print("5.registrar una devolucion")
    print("6.Salir")
    
    def ejecutar_programa(): 
       while True:
        mostrar_menu()   
        opcion=int(input("Selecione una opcion:"))
        if opcion== 1:
            agregar_libro()