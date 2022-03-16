"""Programa que lea un carácter por teclado y compruebe si es una letra mayúscula"""

letra = input('Ingrese una letra: ')

if letra.isupper():
    print('La letra:',letra, 'está en mayúscula')
else:
    print('La letra:',letra, 'no está en mayúscula')