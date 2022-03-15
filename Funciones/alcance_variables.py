"""variable = 60
def funcion():
    global variable
    variable = 30
    if variable < 100:
        print(variable)

print(variable)
funcion()
print(variable)
"""
from re import A


a = int(input('Por favor ingrese un valor: '))
b = int(input('Por favor ingrese un valor: '))

def suma(a,b):
    print(a+b)

suma(a,b)

#ó

a = int(input('Por favor ingrese un valor: '))
b = int(input('Por favor ingrese un valor: '))

def suma():
    global a 
    global b
    print(a+b)

suma()
