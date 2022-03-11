"""Ejemplos de operaciones con listas"""

#longitud de una lista

lista = ['a', 'e', 'i', 'o', 'u']
print('La cantidad de valores de lista es: ', len(lista))

#crear una sublista de la lista principal
print(lista[0:3])
lista2 = lista[0:3]
print(lista2)

#añadir un valor
lista.append('j')
print(lista)
print(len(lista))

#quitar un valor, si el valor que se coloca a borrar no existe ocasiona un error
lista.remove('j')
print(lista)
print(len(lista))

#insertar un valor en una posición específica
lista.insert(3,'Juan')
print(lista)

#buscar un valor dentro de una lista, devuelve un boleano
print('j' in lista)
print('Juan' in lista)

#saber la posición de un valor dentro de la lista, solo considera la posición de la primera coincidencia
print(lista.index('e'))

#concatenar listas
lista3 = lista + lista2
print(lista3)

print(lista[0:5])

#muestra los valores de la lista en un intervalo de dos en dos, este valor lo marca el último número
print(lista3[0:5:2])

#valor minimo de una lista
print(min(lista))

#valor maximo de una lista
print(max(lista))

print(lista3.index('e'))
print(lista3.count('e'))