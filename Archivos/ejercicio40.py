"""Crear una función para multiplicar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la función y regresar
como resultado la multiplicacion de todos los valores pasados como argumentos"""

def multiplicarValores(*args):
    multiplicar = 1
    for i in args:
        multiplicar = multiplicar * i
        print(multiplicar)
        
print(multiplicarValores(1,6,4,7))
print(multiplicarValores(4,6,8,7))