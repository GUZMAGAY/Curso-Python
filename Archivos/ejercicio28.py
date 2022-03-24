"""Multiplicar 2 numeros sin usar el simbolo de la multiplicacion"""

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

num=1
resultado=0
while num <= num1:
    resultado += num2
    num += 1

print(resultado)