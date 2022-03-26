"""Pedir un número por teclado y mostrar la tabla de multiplicar"""

tabla = int(input('Ingrese el número del que se desea conocer la tabla de multiplicar: '))

for numero in range(0,13):
	multiplicacion = tabla * numero 
	print(f'{tabla} x {numero} = {multiplicacion}')