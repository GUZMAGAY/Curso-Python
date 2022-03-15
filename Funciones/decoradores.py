"""def funcion_a(funcion_b):
    def funcion_c():
        #bloque de codigo
        funcion_b()
    return funcion_c()

@funcion_a
def saludo():
    print('Hola ahí!')"""

"""def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)

@mi_decorador
def resta(a ,b):
    print("Entra en funcion resta")
    return a - b

resta(5, 3)"""

num1= int(input('Ingrese el primer número: '))
num2= int(input('Ingrese el segundo número: '))

def operaciones(funcion):
    def calculos(num1,num2):
        print('Operacion a ejecutar')
        ope = funcion (num1,num2)
        print('Se ha ejecutado')
        return ope
    return calculos

@operaciones
def restar(num1,num2): 
    print('Resultado de la resta:',num1-num2)

@operaciones
def multiplicar(num1,num2):
    print('Resultado de la multiplicacion:', num1*num2)

@operaciones
def dividir(num1,num2):
    print('Resultado de la division:', num1/num2)

@operaciones
def potencia(num1,num2):
    print('Resultado de la potenciacion:', num1**num2)

restar(num1,num2)
multiplicar(num1,num2)
dividir(num1,num2)
potencia(num1,num2)