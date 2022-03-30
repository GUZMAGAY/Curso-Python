"""1) Realiza una función llamada area_rectangulo() que devuelva el área del rectangulo a 
partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.

Nota: El área de un rectángulo se obtiene al multiplicar la base por la altura."""


base = int(input('Ingrese la base del rectángulo: '))
altura = int(input('Ingrese la altura del rectángulo: '))

def area(b,a):
    calculo = b * a
    return f"El área del rectángulo es {calculo}"

print(area(base,altura))