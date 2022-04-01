"""Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima 
y mínima de cada día y vaya mostrando la media. 
El programa pedirá el número de días que se van a introducir."""

def intermedio(num1,num2):
    calculo = round((num1 + num2) / 2, 2)
    return f"La temperatura media entre {num1} y {num2} es {calculo}"

def principal():
    dias = int(input('Ingrese la cantidad de días de los que desea cualcular la media de temperatura: '))
    control = 1
    while control <= dias:
        max = int(input(f'Ingrese la tempuratura máxima del día {control}: '))
        min = int(input(f'Ingrese la tempuratura mínima del día {control}: '))
        print(intermedio(max,min))
        control += 1
        
        
principal()