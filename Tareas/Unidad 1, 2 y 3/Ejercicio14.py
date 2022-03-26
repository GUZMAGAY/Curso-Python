"""Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el 
producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un 
signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120"""


def factorial(n):
    if n ==1:
        return 1
#definicion matematica
    return n * factorial(n-1)
n = int(input('Escribe un entero: '))
print ('El factorial es: ',factorial(n))