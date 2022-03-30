"""2) Realiza un programa que lea un número impar por teclado. 
Si el usuario no introduce un número impar, debe repetise el proceso hasta que 
lo introduzca correctamente."""

impar = int(input('Escriba un número impar: '))

if impar % 2 != 0:
    print('Gracias por ingresar un número impar')
else:
    while impar % 2 == 0:
        impar = int(input('Escriba un número impar: '))
    if impar % 2 != 0:
        print('Gracias por ingresar un número impar')