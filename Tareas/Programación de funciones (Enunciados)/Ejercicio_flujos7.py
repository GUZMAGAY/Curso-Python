"""7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
pero no debe repetise ningún elemento en la nueva lista:"""

lista1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
lista2 = [1,3,9,1,3,5,7,9]

lista3 = []

for caracter in lista1:
    if caracter in lista2 and caracter not in lista3:
        lista3.append(caracter)

print('La nueva lista es: ',lista3)