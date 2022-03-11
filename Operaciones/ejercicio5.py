"""Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""

diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
print('Ingrese una divisa:')
divisa=input()

if (divisa in diccionario) == True:
    print('El símbolo de la divisa es', diccionario.get(divisa))
else :
    print('La divisa no está en el diccionario')