"""Operaciones con tuplas"""

tupla1 = ('a', 'b', 'c')
tupla2 = ('d', 'e', 'f')

print(tupla1 + tupla2)

#repite el valor la cantidad de veces por el cual se multiplica
print(tupla1*3)

#campara tuplas
print(tupla1 > tupla2)
print(tupla1 < tupla2)

#convertir una lista a una tupla
lista = [1,2,3,1,1,3]
print(type(lista))
print(lista)
tupla = tuple(lista)
print(tupla)
print(type(tupla))

#recorrer una tupla
for t in tupla:
    print(t)

#contar cuantas veces se repite un valor n en la tupla
print(tupla.count(1))

#muestra el indice en el que se encuentra un determinado valor, si no lo encuentra indica el error valueerror
print(tupla.index(3))

#tambien se le puede indicar desde que posición empezar a contar
print(tupla.index(3, 3))