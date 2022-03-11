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

#Diccionarios dict, vuelve diccionario un conjunto de variables
dic =  dict(nombre='nestor', 
            apellido='Plasencia', 
            edad=22)
print(dic)

#Diccionarios zip, itera dos conjuntos de datos y los vuelve diccionario
dic = dict(zip('abcd',[1,2,3,4]))
print(dic)

#Diccionarios items
dic =   {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
items = dic.items()
print(items)

#Dicciconarios keys, muestra solo las llaves
dic =  {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
keys= dic.keys()
print(keys)

#Diccionarios values, muestra solo los values
dic =  {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
values= dic.values()
print(values)