"""Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo 
y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, 
utilizando la función anterior."""


lista = []
print('Por favor ingrese números y para salir escriba "S"')

def calculaMaxMin(*args):
    lista.sort()
    print('El número menor de la lista es:',lista[0])
    print('El número mayor de la lista es:',lista[-1])

def ingreso():   
    while True:
        valor = input('Ingrese un valor: ')
        if valor == 'S':
            calculaMaxMin(lista)
            break
        else:
            try:
                valor = int(valor)
                lista.append(valor)
            except:
                print('Dato inválido')
                exit()


ingreso()
