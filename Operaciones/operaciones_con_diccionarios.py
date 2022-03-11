"""Operaciones con diccionarios"""


diccionario = {'nombre':'Daniela', 'apellido':'Burgos', 'cedula': 1300000001, 'f_nacimiento': '4-6-94'}

lista1 = [('persona1','Juan'), ('persona2','Pedro'), ('persona3','Maria')]
lista2 = ['persona1', 'persona2', 'persona3']
lista3 = ['Maria', 'Juan', 'Pedro']

"""zip(lista1,lista2)
print(zip)"""

lista1 = [('persona1','Juan'), ('persona2','Pedro'), ('persona3','Maria')]
print(dict(lista1))
print(type(dict(lista1)))
"""print(dic)"""
#obtiene el valor de la llave
print(diccionario.get("nombre"))

#obtiene el valor y lo elimina
print(diccionario.pop("nombre"))
print(diccionario)

#permite actualizar los valores de la llave
diccionario.update({'f_nacimiento':'7-9-20'})
print(diccionario)

#devuelve un boleano de si la llave existe o no en el diccionario
print('cedula' in diccionario)
print('pais' in diccionario)

#devuelve un boleano de si el valor existe o no en el diccionario, no considera las llaves
print(1300000001 in diccionario.values())
print('Casa' in diccionario.values())