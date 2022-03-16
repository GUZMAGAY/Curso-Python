"""def gen_basico(): #es una forma de presentacion de los datos
    yield "uno"
    yield "dos"
    yield "tres"

for valor in gen_basico():
    print(valor)
"""

"""from tkinter import N


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

"""

def generadorPares(Limite):
    num = 1
    while num < Limite:
        yield num*2
        num += 1
devuelvepares = generadorPares(10)

print(next(devuelvepares))
print('Aqui va un poco mas de codigo')
print(next(devuelvepares))
print('Aqui va mas codigo del necesario')
print(next(devuelvepares))

