"""def gen_basico(): #es una forma de presentacion de los datos
    yield "uno"
    yield "dos"
    yield "tres"

for valor in gen_basico():
    print(valor)
"""

from tkinter import N


def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n 

g = generador()
print(next(g))
print(next(g))
print(next(g))

