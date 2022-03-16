def restar(rest1=0,rest2=0):
    print('Resultado de la resta:',rest1-rest2)

def multiplicar(mult1=0,mult2=0):
    print('Resultado de la multiplicacion:', mult1*mult2)

def dividir(div1=0,div2=0):
    print('Resultado de la division:', div1/div2)

def potencia(pot1=0,pot2=0):
    print('Resultado de la potenciacion:', pot1**pot2)

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

      
control()

restar(num1,num2)
multiplicar(num1,num2)
dividir(num1,num2)
potencia(num1,num2)   




