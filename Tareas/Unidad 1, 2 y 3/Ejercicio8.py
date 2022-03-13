"""Escribe un programa que lea un número e indique si es par o impar"""

numero = int(input('Ingrese un numero: '))

valor = numero % 2
if valor == 0:
    print('El numero ingresado es par')
else:
    print('El numero ingresado es impar')