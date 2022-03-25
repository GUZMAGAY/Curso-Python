"""Escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo"""

from io import open 

lista = open(r"C:\Curso Python\Archivos\lista.txt", "a")

def escribir():
    while True:
        datos = input('Esriba un nombre y apellido para agregarlo al archivo, escriba "S" para salir: ')
        if datos == 'S':
            break
        else:
            lista.write(datos+'\n')
 
escribir()       
lista.close()
