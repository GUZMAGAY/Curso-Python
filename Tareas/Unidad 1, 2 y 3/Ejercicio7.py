"""Realiza un programa que pida dos números 'a' y 'b' e indique si su suma es positiva, negativa o cero"""

numero1 = float(input('Ingrese el primer numero: '))
numero2 = float(input('Ingrese el segundo numero: '))

resultado = numero1 + numero2

if resultado > 0:
    print('El resultado: ', resultado, 'es positivo')
elif resultado < 0:
    print('El resultado: ', resultado, 'es negativo')
else:
    print('El resultado: ', resultado, 'es cero')