"""Crear las funciones anonimas:
Restar
Multiplicar
Dividir
Potenciar"""


num1= int(input('Ingrese el primer número: '))
num2= int(input('Ingrese el segundo número: '))


restar = lambda rest1,rest2: rest1-rest2
multiplicar = lambda mult1,mult2: mult1 * mult2
dividir = lambda div1,div2: div1 / div2
potencia = lambda pot1,pot2: pot1 ** pot2

print('Resultado de la resta:',restar(num1,num2))
print('Resultado de la multiplicacion:', multiplicar(num1,num2))
print('Resultado de la division:', dividir(num1,num2))
print('Resultado de la potenciacion:', potencia(num1,num2))
