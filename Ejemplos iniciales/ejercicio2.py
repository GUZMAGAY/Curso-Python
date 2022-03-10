"""Crear 2 variable con cada tipo de dato:
    numerico(entero,flotante)
    cadenas de caracteres (string)
    boleano (True o False)

    listas (que se representan por corchetes y son mutable)
    tuplas (que se representan por parentisis y son inmutable)
    diccionario (que se representas por llaves y se asignan mediante clave y valor, solo el valor es mutable)

    set (se representa con llaves y muestra datos de forma ordenada sin repetir valores)

    utilizar el print para conocer el valor de cada dato
    utilizar el type para conocer el valor de cada dato

    Ejemplo

a = 4
b = 5
print(a, b)
print(type(a),type(b))"""


#Numerico
#Entero
num1 = 5
num2 = 7
print(num1, num2)
print(type(num1), type(num2))

#Flotante
flo1 = 5.7
flo2 = 7.8
print(flo1, flo2)
print(type(flo1), type(flo2))

#Cadenas
cad1 = 'Daniela'
cad2 = 'Burgos'
print(cad1, cad2)
print(type(cad1), type(cad2))

#Boleano
bol1 = 5 > 6
bol2 = 6 == 6
print(bol1, bol2)
print(type(bol1), type(bol2))

#Listas
lista1 = [1, 4, 6, 7]
lista2 = ['tren', 'avion', 'barco']
print(lista1, lista2)
print(type(lista1), type(lista2))

#Tuplas
tupla1 = ('bueno', 'malo', True, 6 < 0)
tupla2 = (2.6, 5.7, 6.6)
print(tupla1, tupla2)
print(type(tupla1), type(tupla2))

#Diccionario
dic1 = {'fruta':'manzana', 'grano':'arroz', 'cereal':'quinua'}
dic2 = {'nombre': 'Daniela', 'apellido':'Burgos', 'edad':32}
print(dic1, dic2)
print(type(dic1), type(dic2))

#Set
set1 = {1, 4 ,6 , 'negro', 5.5 , 9, 1, 9, 10, 5.5}
set2 = {'gris', 'negro', 'rojo', 'gris', 'blanco', 'negro', 'rojo'}
print(set1, set2)
print(type(set1), type(set2))