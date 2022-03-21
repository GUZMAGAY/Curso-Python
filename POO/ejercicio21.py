"""Crea una función “calcularMaxMin” que recibe una lista con 
valores numéricos y devuelve el valor máximo y el mínimo. 
Crea un programa que pida números por teclado y 
muestre el máximo y el mínimo, utilizando la función anterior."""

lista_num = [2,3,6,1]
"""num_max = int(input('ingrese el maximo '))
min = int(input('ingrese el minimo '))"""

def calcularMaxMin(lista_num):
    num_max = 0
    num_min = 0
    
    for i, dato in enumerate(lista_num):
        num_max = max(num_max, dato)
        num_min = min(num_max, dato)
    print(f"la lista es {lista_num}")
    print(f"el numero maximo es {num_max}")
    print(f"el numero minimo es {num_min}")
    
calcularMaxMin([4,2,8,3,7,1])