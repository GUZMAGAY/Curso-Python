"""Crear una función que calcule el MCD de dos número por el método de Euclides. 
El método de Euclides es el siguiente:
Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma 
hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD."""

def Intercambiar(mayor, menor):
	if mayor<menor:
		aux = mayor
		mayor = menor
		menor = aux
	return (mayor, menor)

def CalcularMCD(num1,num2):
	Intercambiar(num1,num2)
	residuo = num1 % num2
	if residuo == 0: 
		mcd = num2
	else:
		mcd = CalcularMCD(num2,residuo)
	return mcd

def MCDEuclides():
    num1 = int(input('Escriba el primer número: '))
    num2 = int(input('Escriba el segundo número: '))
    print("MCD: ", CalcularMCD(num1,num2))

MCDEuclides()
