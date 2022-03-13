"""Escribe un programa que pida un número entero entre uno y doce 
e imprima el número de días que tiene el mes correspondiente"""

mes = int(input('Ingrese un numero del 1 al 12: '))

meses = {1: 31, 
        2: 28, 
        3: 31, 
        4: 30, 
        5: 31, 
        6: 30, 
        7: 31, 
        8: 31, 
        9: 30, 
        10: 31, 
        11: 30, 
        12: 31}

if mes >= 1 and mes <=12:
    print('El mes', mes ,'tiene',meses.get(mes), 'dias')
else:
    print('Numero ingresado fuera del rango')