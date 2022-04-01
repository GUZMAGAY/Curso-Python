"""Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo."""

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

def EsMultiplo(num1, num2):
    if num1 % num2 == 0:
        return f"El número {num1} es múltiplo de {num2}"
    else:
        return f"El número {num1} no es múltiplo de {num2}"
    
print(EsMultiplo(num1,num2))