# lo que se hace es importar las clases y funciones necesarias de los otros archivos
from productos_ejercicioD import Producto
from inventario_ejercicioD import mostrar_inventario, buscar_producto
def mostrar_menu():
    #funcion para mostrar el menu
    print("MENÚ")
    #chcp 65001 en la terminal para que me muestre bien los caracteres especiales
    print("1. Mostrar inventario")
    print("2. Comprar producto (aumentar stock)")
    print("3. Vender producto (disminuir stock)")
    print("4. Salir")
    print("\n")#esto es un salto de linea para que se vea mejor el menu
def main():#esta es la funcion principal que ejecuta el programa
    # Crear productos iniciales
    inventario = [
    Producto("Mouse", 30000, 10),
    Producto("Teclado", 80000, 5),
    Producto("USB 16GB", 20000, 20),
    Producto("Audífonos", 45000, 12),
    Producto("Monitor 24", 450000, 4),
    Producto("Cable HDMI", 15000, 25),
    Producto("Parlantes", 70000, 8),
    Producto("Mouse Pad", 12000, 30),
    Producto("Cargador USB-C", 35000, 15),
    Producto("Disco Duro 1TB", 200000, 6),
    Producto("Silla Gamer", 600000, 2),
    Producto("Router WiFi", 120000, 5),
    Producto("Laptop 15''", 2500000, 3)
]
    while True:
#bucle infinito para el menu(hace que el menu se repita hasta que el usuario decida salir)
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a comprar: ")
            producto = buscar_producto(nombre, inventario)
            if producto:
                cantidad = int(input("Cantidad a aumentar: "))
                producto.aumentar_stock(cantidad)
            else:
                print("Producto no encontrado.")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a vender: ")
            producto = buscar_producto(nombre, inventario)
            if producto:
                cantidad = int(input("Cantidad a vender: "))
                producto.disminuir_stock(cantidad)
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.\n")
if __name__ == "__main__":
#esto hace que se ejecute la funcion main solo si se ejecuta este archivo 
    main()
