"""4) Realiza un programa que pida al usuario cuantos números quiere introducir. 
Luego lee todos los números y realiza una media aritmética:"""

numeros = int(input('Ingrese cuantos números desea ingresar a la lista: '))
control = 0
lista= []

while control < numeros:
    valor = int(input('Ingrese un valor a la lista y presione enter: '))
    lista.append(valor)
    control += 1
    
suma = sum(lista) 
media= suma/len(lista)  
print (media) 