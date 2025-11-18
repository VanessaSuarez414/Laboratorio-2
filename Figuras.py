#Importar libreria
import math
#Area del cuadrado 
def area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el lado. Retorna el área del cuadrado
    Parametros: lado(float): Longitud del lado del cuadrado
    area = lado * lado"""
    area= lado * lado
    return area
#Area triangula
def area_triangulo(base, altura):
    """
    Calcula el area de un triangulo dado la base y la altura.
    Retorna el area calculada del Triangulo
    """
    area= (base*altura)/2
    
    return area 
#Area Circulo
def area_circulo(radio):
    """
    "Calcula el area del circulo dado el radio. 
    Retorna el area calculada del circulo 
    Parametros: 
    Radio(float): Longitud del radio del circulo 
    area= pi* radio * radio 
    """
    area= math.pi * (radio **2)
    return area 
#Area pentagono
def area_pentagono(perimetro, apotema):
    """Calcula el perimetro del pentagono dado el apotema
        parametros:
            perimetro(float):La longitud total del area del perimetro del pentagono
            apotema (float): La longitud del apotema (distancia del centro al lado)
             Retorna:
        """
    perimetro = (perimetro * apotema ) /2
    return perimetro
#Area trapecio
def area_trapecio(Bmayor,Bmenor):
        """Calcula el area del trapecio
    parametros:
    Base mayor(float): B la Base Mayor
    Base menor(float): b la base menor
     altura (float): h, la altura perpendicular entre las bases
    retorna:
    float:Area del trapecio
    """
        area = (Bmayor + Bmenor) / 2
        return area 
#Area Romboide 
def area_romboide(base, altura):
     area= base * altura 
     return area
#Area del rombo 
def area_rombo(Dmayor, Dmenor):
     area= (Dmayor * Dmenor)/2
     return area
#Area del rectangulo
def area_rectangulo(base,altura):
     area= base * altura
     return area