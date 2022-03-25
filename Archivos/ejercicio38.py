"""Iterar un rango de 0 a 10 e imprimir solo los número divisibles entre 3"""

i=0
for i in range(0,10):
    if i != 0:
        valor = i % 3
        if valor == 0:
            print(f'El numero {i} es divisible para 3')


