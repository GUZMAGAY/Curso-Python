"""Escribir una funcion que indique cuantas vocales tiene una palabra"""

palabra = input('Ingrese una palabra: ').lower()

def vocales(palabra):
    vocal = 0
    for v in palabra:
        if v =='a' or v =='e' or v =='i' or v =='o'or v =='u':
            vocal +=1
    print('El numero de vocales en la palabra es: ',vocal)
    

vocales(palabra)