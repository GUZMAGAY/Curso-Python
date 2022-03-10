"""Crear una lista con los nombres de 5 estudiantes
crear una lista2 con 5 notas 
Crear una lista3 que permita observar los nombres y las notas en estas posiciones"""

lista = ['Daniela', 'Oscar', 'Steven', 'Erick', 'Jose']
print(lista)

lista2 = [8, 7 , 8, 9, 10]
print(lista2)

lista3 = [lista[0],lista2[0],lista[1],lista2[1],lista[2],lista2[2],lista[3],lista2[3],lista[4],lista2[4]]
print(lista3)

lista4 = lista + lista2
print(lista4)