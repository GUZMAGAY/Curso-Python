'''Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a 
utilizar dos enteros: numerador y denominador.

Vamos a crear las siguientes funciones para trabajar con funciones:

Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. 
Cuando leas una fracción debes simplificarla.
Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el 
numerador.
Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y 
dominador por el MCD del numerador y denominador.
Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. 
La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. 
Se debe simplificar la fracción resultado.
Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, 
para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, 
para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.'''

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

def Leer_Fraccion():
	numerador = int(input('Numerador:'))
	denominador = int(input('Denominador:'))
	numerador,denominador = Simplificar_Fraccion(numerador,denominador)
	return numerador,denominador

def Simplificar_Fraccion(numerador,denominador):
	mcd = CalcularMCD(numerador,denominador)
	numerador = numerador / mcd
	denominador = denominador / mcd
	return numerador,denominador

def Escribir_Fraccion(numerador,denominador):
	if denominador!= 1:
		print(numerador)
		print('---')
		print(denominador)
	else:
		print('')
		print(numerador)
		print('')


def Sumar_Fracciones(n1,d1,n2,d2):
	nr = n1*d2 + d1*n2
	dr = d1 * d2
	nr,dr = Simplificar_Fraccion(nr,dr)
	return nr,dr

def Restar_Fracciones(n1,d1,n2,d2):
	nr = n1*d2 - d1*n2
	dr = d1 * d2
	nr,dr = Simplificar_Fraccion(nr,dr)
	return nr,dr

def Multiplicar_Fracciones(n1,d1,n2,d2):
	nr = n1 * n2
	dr = d1 * d2
	nr,dr = Simplificar_Fraccion(nr,dr)
	return nr,dr

def Dividir_Fracciones(n1,d1,n2,d2):
	nr = n1 * d2
	dr = d1 * n2
	nr,dr = Simplificar_Fraccion(nr,dr)
	return nr,dr

print('\n Que operacion desea realizar \n')
print('1) Sumar dos fracciones')
print('2) Restar dos fracciones')
print('3) Multiplicar dos fracciones')
print('4) Dividir dos fracciones')
print('5) Salir')
opcion = int(input('Ingrese la opcion: '))
if opcion>=1 and opcion <=4:
	print('Ingrese la primer fracción: ')
	num1,den1= Leer_Fraccion()
	print('Ingrese la segunda fracción: ')
	num2,den2= Leer_Fraccion()
if opcion == 1:
    numr,denr = Sumar_Fracciones(num1,den1,num2,den2)
    print('El resultado de la suma es:')
    Escribir_Fraccion(numr,denr)
elif opcion == 2:
    print('Restar fracciones')
    numr,denr = Restar_Fracciones(num1,den1,num2,den2)
    print('El resultado de la resta es:')
    Escribir_Fraccion(numr,denr)
elif opcion == 3:
    numr,denr = Multiplicar_Fracciones(num1,den1,num2,den2)
    print('El resultado de la multiplicación es:')
    Escribir_Fraccion(numr,denr)
elif opcion == 4:
    numr,denr = Dividir_Fracciones(num1,den1,num2,den2)
    print('El resultado de la división es:')
    Escribir_Fraccion(numr,denr)
elif opcion == 5:
	print('Saliendo del sistema')
else:
	print('Opción incorrecta')
