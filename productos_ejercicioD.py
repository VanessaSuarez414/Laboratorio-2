# clase Producto para representar cada producto en el inventario
class Producto:
    #aca se definen los atributos de la clase
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        #funcion para aumentar el stock del producto
    def aumentar_stock(self, cantidad):
        self.cantidad += cantidad
        print(f"Se aumentó el stock de {self.nombre} en {cantidad}. Total: {self.cantidad}")
    def disminuir_stock(self, cantidad):#funcion para disminuir el stock del producto
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Se disminuyó el stock de {self.nombre} en {cantidad}. Total: {self.cantidad}")
        else:
            print(f"No hay suficiente stock de {self.nombre} para vender {cantidad} unidades.")
