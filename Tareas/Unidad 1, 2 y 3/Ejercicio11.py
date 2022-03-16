"""Escribir un programa que lea un anio indicar si es bisiesto. 
Nota: un anio es bisiesto si es un número divisible por 4, 
pero no si es divisible por 100, excepto que también sea divisible por 400

Si no es divisible para 4: no es bisiesto
Si es divisible para 4 y no es disible para 100: es bisiesto
Si es divisible para 4 y divisible para 100 pero no es divisible para 400: no es bisiesto
Si es divisible para 4 y divisible para 100 y divisible para 400: es bisiesto
"""

anio = int(input('Por favor ingrese un año: '))

if anio % 4 != 0: 
	print("No es bisiesto")
elif anio % 4 == 0 and anio % 100 != 0: 
	print("Es bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: 
	print("No es bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: 
	print("Es bisiesto")
