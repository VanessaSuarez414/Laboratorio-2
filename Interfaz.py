#Solicitud de datos
#Solicitud datos cuadrado
def solicitar_datos_cuadrado():
    """
    Solicita al usuario la longitud del lado del cuadrado.
    Retorna la longitud del lado como un número flotante.
    """
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    return lado
#Solicitud datos triangulo
def solicitar_datos_triangulo():
    """
    Solicita al usuario la base y la altura del triángulo.
    Retorna la base y la altura como números flotantes.
    """
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return base, altura
#Solicitud datos circulo
def solicitar_datos_circulo():
    """
    Solicita al usuario el radio del círculo.
    Retorna el radio como un número flotante.
    """
    radio = float(input("Ingrese el radio del círculo: "))
    return radio
#Solicitar datos Pentagono
def solicitar_datos_pentagono():
    """
    Solicitar el perimetro y la apotema del pentagono. 
    La apotema es la distancia desde el centro del pentágono hasta el punto medio de uno de sus lados. 
    El perimetro es la suma de la longitud de los lados del Pentagono 
    Retorna el perimetro y el apotema como numeros flotantes
    """
    apotema= float(input("Ingrese la apotema del Pentagono: "))
    Perimetro= float(input("Ingrese el perimetro del Pentagono: " ))
    return apotema, Perimetro
#Solicitar datos Trapecio
def solicitar_datos_trapecio():
    """
    Solicitar al usuario la base mayor, base menor y la altura del Trapecio.
    Base mayor y base menor: Son los dos lados paralelos del trapecio.
    Altura: Es la distancia perpendicular que une las dos bases. 
    Retorna la base mayor, base menor y la altura como numeros flotantes.
    """
    Bmayor=float(input("Ingrese la base mayor del Trapecio:"))
    Bmenor=float(input("Ingrese la base menor del Trapecio: "))
    Altura= float(input("Ingrese la altura del Trapecio: "))
    return Bmayor,Bmenor, Altura
#Solicitar datos Romboide 
def solicitar_datos_romboide():
    """Solicitar al usuario la base y la altura de el romboide.
    La altura es la distancia perpendicular desde la base hasta el lado opuesto.  
     Retorna la base y la altura como numeros flotantes 
     """
    base = float(input("Ingrese la base del Romboide: "))
    altura = float(input("Ingrese la altura del Romboide: "))
    return base, altura
#Solicitud datos Rombo 
def solicitar_datos_rombo():
    """Solicitar al usuario la diagonal mayor y la diagonal menor. 
    Retorna la diagonal mayor y la diagonal menor como numeros flotantes."""
    Dmayor=float(input("Ingrese la Diagonal mayor del Rombo: "))
    Dmenor= float(input("Ingrese la diagonal menor del Rombo: "))
    return Dmayor, Dmenor
#Solicitud datos Rectangulo 
def solicitar_datos_rectangulo():
    """Solicitar al usuario la base y la altura de el rectangulo 
     Retorna la base y la altura como numeros flotantes 
     """
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))
    return base, altura

#Mostrar datos
#Mostrar area cuadrado
def mostrar_area_cuadrado(area):
    """
    Muestra el área del cuadrado al usuario.
    Parámetros:
        area (float): El área del cuadrado a mostrar.
    """
    print(f"El área del cuadrado es: {area}")
#Mostrar area triangulo
def mostrar_area_triangulo(area):    
    """
    Muestra el área del triángulo al usuario.
    Parámetros:
        area (float): El área del triángulo a mostrar.
    """
    print(f"El área del triángulo es: {area}")
#Mostrar area circulo
def mostrar_area_circulo(area):
    """
    Muestra el área del círculo al usuario.
    Parámetros:
        area (float): El área del círculo a mostrar.
    """
    print(f"El área del círculo es: {area}")
#Mostrar area pentagono
def mostrar_area_pentagono(area):
    """
    Muestra el área del pentagono al usuario.
    Parámetros:
        area (float): El área del pentagono a mostrar.
    """
    print(f"El área del pentagono es: {area}")
#Mostrar area del trapecio
def mostrar_area_trapecio(area):
    """
    Muestra el área del trapecio al usuario.
    Parámetros:
        area (float): El área del trapecio a mostrar.
    """
    print(f"El área del trapecio es: {area}")
#Mostrar area del Romboide
def mostrar_area_romboide(area):
    """
    Muestra el área del romboide al usuario.
    Parámetros:
        area (float): El área del romboide a mostrar.
    """
    print(f"El área del romboide es: {area}")
#Mostrar area del Rombo
def mostrar_area_rombo(area):
    """
    Muestra el área del rombo al usuario.
    Parámetros:
        area (float): El área del rombo a mostrar.
    """
    print(f"El área del rombo es: {area}")
#Mostrar area del Rectangulo
def mostrar_area_rectangulo(area):
    """
    Muestra el área del rectangulo al usuario.
    Parámetros:
        area (float): El área del rectangulo a mostrar.
    """
    print(f"El área del Rectangulo es: {area}")
#Menu calculadora
def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    Retorna la opción seleccionada por el usuario como un entero.
    """
    print("Calculadora de Áreas de Figuras Geométricas")
    print("1. Calcular área del cuadrado")
    print("2. Calcular área del triángulo")
    print("3. Calcular área del círculo")
    print("4. Calcular área del pentagono")
    print("5. Calcular área del trapecio")
    print("6. Calcular área del Romboide")
    print("7. Calcular área del Rombo")
    print("8. Calcular área del Rectangulo")
    print("9. Salir")
    opcion = int(input("Seleccione una opción (1-9): "))
    return opcion