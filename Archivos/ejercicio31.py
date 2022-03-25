"""Escribir una función que devuelva el volumen de una esfera por su radio"""

import math
from fractions import Fraction



radio = int(input('Ingrese el radio de la esfera: '))

def calculo(radio):
    volumen = Fraction(4,3) * math.pi * radio ** 3
    print('El volumen de la esfera es: ',round(volumen,2))
    
calculo(radio)