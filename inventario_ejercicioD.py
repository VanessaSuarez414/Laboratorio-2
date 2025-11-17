# definimos funciones para manejar el inventario
def mostrar_inventario(lista_productos):
    print("\nINVENTARIO")
    for producto in lista_productos:
        print(f"Nombre: {producto.nombre} | Precio: {producto.precio} | Cantidad: {producto.cantidad}")
    print("\n")#salto de linea
def buscar_producto(nombre, lista_productos):#funcion para buscar un producto por su nombre
    for producto in lista_productos:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None# si no se encuentra el producto
