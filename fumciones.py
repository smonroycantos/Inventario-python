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

DB_FILE = "productos.txt"

def cargar_productos():
    nombres = []
    cantidades = []
    precios = []
    try:
        with open(DB_FILE, 'r') as file:
            for linea in file:
                nombre, cantidad, precio = linea.strip().split(',')
                nombres.append(nombre)
                cantidades.append(int(cantidad))
                precios.append(float(precio))
    except FileNotFoundError:
        pass 
    return nombres, cantidades, precios

def guardar_productos(nombres, cantidades, precios):
    with open(DB_FILE, 'w') as file:
        for nombre, cantidad, precio in zip(nombres, cantidades, precios):
            file.write(f"{nombre},{cantidad},{precio}\n")
