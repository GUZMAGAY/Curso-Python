"""Crear las funciones:
Restar
Multiplicar
Dividir
Potenciar"""

num1=4
num2=3
num1= int(input('Ingrese el primer número: '))
num2= int(input('Ingrese el segundo número: '))

def restar(rest1=0,rest2=0): #se pueden declarar las variables para que en caso de no enviar un valor la funcion no de error
    print('Resultado de la resta:',rest1-rest2)

def multiplicar(mult1=0,mult2=0):
    print('Resultado de la multiplicacion:', mult1*mult2)

def dividir(div1=0,div2=0):
    print('Resultado de la division:', div1/div2)

def potencia(pot1=0,pot2=0):
    print('Resultado de la potenciacion:', pot1**pot2)


restar(num1,num2)
multiplicar(num1,num2)
dividir(num1,num2)
potencia(num1,num2)