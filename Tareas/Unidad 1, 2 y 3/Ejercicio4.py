"""Escribir un programa que le pida una palabra al usuario, 
para luego imprimirla 1000 veces, con espacios intermedios."""
import sys

palabra = input('Ingrese una parabra para ser impresa: ')

contador=0
while contador < 1000:
    str(sys.stdout.write(palabra))
    str(sys.stdout.write(' '))
    contador += 1
