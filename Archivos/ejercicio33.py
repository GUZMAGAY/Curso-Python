"""Escribir una función que permita calcular si un numero es par o impar"""

numero = int(input('Ingrese un numero: '))

def par_impar(numero):
    valor = numero % 2
    if valor == 0:
        print('El numero ingresado es par')
    else:
        print('El numero ingresado es impar')
        
par_impar(numero)