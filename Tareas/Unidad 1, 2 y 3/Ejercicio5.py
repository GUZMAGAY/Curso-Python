"""Realiza un programa que reciba una cantidad de minutos y 
muestre por pantalla a cuantas horas y minutos corresponde"""

minutos = int(input('Ingrese los minutos a calcular: '))

horas = int(minutos / 60)
min1 = minutos % 60

print(minutos,'minutos son', horas,'horas y', min1, 'minutos')