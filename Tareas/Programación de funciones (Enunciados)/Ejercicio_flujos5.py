"""5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número 
no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de 
números y notificarlo:

Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra 
en una lista (devuelve True o False)"""

lista = (0,1,2,3,4,5,6,7,8,9)

numero = 10

while numero < 0 or numero > 9:
    numero = int(input('Ingrese un número entero del 0 al 9: '))

if numero in lista:
    print('El número se encuentra en la lista')