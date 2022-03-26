"""Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un 
número entero por teclado. A continuación va pidiendo números y va respondiendo 
si el número a adivinar es mayor o menor que el introducido. 
El programa termina cuando se acierta el número."""

numero = int(input('Ingrese un número: '))
adivina = 0

while numero != adivina:

    adivina = int(input('Intenta adivinar: ')) 

    if adivina < numero:
        print('El número ingresado es menor') 

    if adivina > numero:
        print('El numero ingresado es mayor')

    if adivina == numero:
        print('Adivinaste')
        



