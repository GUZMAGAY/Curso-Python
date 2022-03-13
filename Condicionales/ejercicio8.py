"""
Ejercicio1: Imprimir en pantalla los numeros pares del 1 al 500
Ejercicio2: Imprimir en pantalla los numeros primos del 1 al 100
"""


for pares in range(0,501):
    valor = pares % 2
    if valor == 0:
        print(pares)

"""for pares in range(0,501):
    if pares % 2 == 0:
        print(pares)
"""
contador = 1
limite = 100
for a in range(1, limite+1):
    c = 0
    for b in range(1, contador+1):
        a = contador % b
        if a == 0:
            c = c + 1
    if c == 2:
        print(contador)
    else:
        a = a - 1
    contador += 1
   