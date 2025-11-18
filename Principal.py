#LLamar funciones del archivo Figuras.py
#from Figuras import area_cuadrado, area_triangulo, area_circulo, area_pentagono, area_trapecio, area_romboide, area_rombo, area_rectangulo
from Figuras import *
#LLamar funciones del archivo Interfaz.py
#from Interfaz import solicitar_datos_cuadrado, mostrar_area_cuadrado
from Interfaz import *
#Funcion principal
#Variables menu
opcion = 0
CUADRADO = 1
TRIANGULO = 2
CIRCULO = 3
PENTAGONO = 4   
TRAPECIO = 5
ROMBOIDE = 6
ROMBO = 7
RECTANGULO = 8
SALIR = 9
while opcion != SALIR:
    opcion = mostrar_menu()
    if opcion == CUADRADO:
        lado = solicitar_datos_cuadrado()
        area = area_cuadrado(lado)
        mostrar_area_cuadrado(area)
    elif opcion == TRIANGULO:
        base, altura = solicitar_datos_triangulo()
        area = area_triangulo(base, altura)
        mostrar_area_triangulo(area)
    elif opcion == CIRCULO:
        radio = solicitar_datos_circulo()
        area = area_circulo(radio)
        mostrar_area_circulo(area)
    elif opcion == PENTAGONO:
        perimetro, apotema = solicitar_datos_pentagono()
        area = area_pentagono(perimetro, apotema)
        mostrar_area_pentagono(area)
    elif opcion == TRAPECIO:
        Bmayor, Bmenor, altura = solicitar_datos_trapecio()
        area = area_trapecio(Bmayor, Bmenor, altura)
        mostrar_area_trapecio(area)
    elif opcion == ROMBOIDE:
        base, altura = solicitar_datos_romboide()
        area = area_romboide(base, altura)
        mostrar_area_romboide(area)
    elif opcion == ROMBO:
        Dmayor, Dmenor = solicitar_datos_rombo()
        area = area_rombo(Dmayor, Dmenor)
        mostrar_area_rombo(area)
    elif opcion == RECTANGULO:
        base, altura = solicitar_datos_rectangulo()
        area = area_rectangulo(base, altura)
        mostrar_area_rectangulo(area)
    elif opcion == SALIR:
        print("Saliendo de la calculadora. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")