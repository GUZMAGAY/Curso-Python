"""Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es 
múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, 
y devuelve si el primero es múltiplo del segundo."""

def EsMultiplo():
    try:
        num1 = int(input('Ingrese el primero numero: '))
        num2 = int(input('Ingrese el segundo numero: '))
        if num1 % num2 == 0:
            print(f"El numero {num1} es multiplo de {num2}")
        else:
            print(f"El numero {num1} no es multiplo de {num2}")
    except Exception as e:
        print("Los valores ingresados no son entero, error", type(e).__name__)

EsMultiplo()