"""Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta."""

def input1():
    global num1
    num1 = int(input('Ingrese el primer número: '))
    return num1

def input2():
    global num2
    num2= int(input('Ingrese el segundo número: '))
    return num2

def control():

    try:
        input1()
        input2()         
    except ValueError:
        print('Número no valido')
        control()
    except NameError:
        print('Número no valido')
        control()
        
print('Operaciones con 2 números \n')

control()
"""num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))"""

while True:
    
    print('\n Que operacion desea realizar \n')
    print(' 1) Suma')
    print(' 2) Resta')
    print(' 3) Multiplicacion')
    print(' 4) Salir')
    
    operacion = int(input('Escoja la operacion que desea realizar: '))
    
    if operacion == 1:
        print("La suma de los numeros ", num1, "+", num2,"=",num1 + num2)
    elif operacion == 2:
        print("La resta de los numeros ", num1, "-", num2,"=",num1 - num2)
    elif operacion == 3:
        print("La multiplicacion de los numeros ", num1, "*", num2,"=",num1 * num2)
    else:
        print("Saliendo del sistema")
        break        
    break