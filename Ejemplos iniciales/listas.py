"""Ejemplos de listas"""

compras = ['manzanas','pollo','zanahorias','papa']
print(compras)
print(type(compras))

print(compras[0])
#muestra el tercer caracter del string ubicado en la posicion 0 de la lista
print(compras[0][3]) 

#se usa append para agregar mas valores a una lista
compras.append('uvas')
print(compras)

#remove se usa para quitar valores de una lista
compras.remove('manzanas')
print(compras)

notas = [9.4, 5.8, 10.0]
print(notas)
print(type(notas))
print(notas[0]+notas[1])

indefinido = [6.7, 'Juan', True, ['Pedro','Pablo'], 5j]
print(indefinido)