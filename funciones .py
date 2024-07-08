
def menu():
    print("--------Sistema de Inventarios--------")
    print("1. Ingresar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Lista de productos")
    print("5. Salir")

def seleccionar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            return opcion
        except ValueError:
            print("Opción no válida. Intente de nuevo.")
