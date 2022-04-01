"""Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, 
convertir a horas,minutos y segundos o salir del programa."""

def seconds():
    segundos = int(input('Ingrese los segundos a calcular: '))

    segundos2 = segundos % 60
    minutos = segundos // 60
    if minutos < 60:
        horas=0
    else:
        horas = minutos // 60
        minutos = minutos % 60

    print(segundos,'segundos son', horas,'horas', minutos, 'minutos y', segundos2, 'segundos')

def hour():
    hora = input('Escribir la hora que desee convertir a segundos con el siguiente formato hh:mm:ss ')

    lista = hora.split(':')
    segundos = int(lista[2])
    minutos = int(lista[1]) * 60
    horas = int(lista[0]) * 3600

    total = horas + minutos + segundos
    print('La hora',hora,'corresponde a',total,'segundos')
    
print('\n Que operacion desea realizar \n')
print(' 1) Transformar de segundos a horas minutos y segundos')
print(' 2) Transformar de horas minutos y segundos a segundos')
print(' 3) Salir')
    
operacion = int(input('Escoja la operacion que desea realizar: '))
    
if operacion == 1:
    seconds()
elif operacion == 2:
    hour()
elif operacion == 3:
    print("Saliendo del sistema")
else:
    print("Opción no válida")   
