"""Calcular el perímetro y área de un círculo dado su radio."""

import math
math.pi


radio = float(input('Ingrese el radio del circulo '))

area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print('El área del círculo es: ', round(area,2))
print('El perímetro del círculo es: ', round(perimetro,2))

