"""6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares:

Por ejemplo:

pares, impares = separar([6,5,2,1,7])
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]
Nota: Para ordenar una lista automáticamente puedes usar el método .sort().
numeros = [-12, 84, 13, 20, -33, 101, 9]"""

numeros = [-12, 84, 13, 20, -33, 101, 9]
pares = []
impares = []

def separar(*valores):
    numeros.sort()
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return numeros
    
print('Lista original ordenada:',separar(numeros))
print('Lista de números pares:',pares)
print('Lista de números impares:',impares)