import funciones

def main():
    nombres = []
    cantidades = []
    precios = []
    cantidad_productos = 0

    while True:
        funciones.menu()
        opcion = funciones.seleccionar_opcion()

        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            nombres.append(nombre)
            cantidades.append(cantidad)
            precios.append(precio)
            cantidad_productos += 1
            print("Producto agregado exitosamente.")
        elif opcion == 2:
            nombre = input("Ingrese el nombre del producto a editar: ")
            if nombre in nombres:
                i = nombres.index(nombre)
                cantidades[i] = int(input("Ingrese la nueva cantidad: "))
                precios[i] = float(input("Ingrese el nuevo precio: "))
                print("Producto editado exitosamente.")
            else:
                print("Producto no encontrado.")
        elif opcion == 3:
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            if nombre in nombres:
                i = nombres.index(nombre)
                del nombres[i]
                del cantidades[i]
                del precios[i]
                cantidad_productos -= 1
                print("Producto eliminado exitosamente.")
            else:
                print("Producto no encontrado.")
        elif opcion == 4:
            print("\nLista de productos en inventario:\n")
            print("Nombre\t\tCantidad\tPrecio")
            for i in range(cantidad_productos):
                print(f"{nombres[i]}\t\t{cantidades[i]}\t\t{precios[i]:.2f}")
        elif opcion == 5:
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
