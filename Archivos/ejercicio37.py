"""4. El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:

El usuario proporcionará un valor entre 0 y 10.

Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F

Cualquier otro valor debe imprimir: Valor desconocido

Por ejemplo:

    Proporciona un valor entre 0 y 10:
    A"""


from io import open 

lista = open(r"C:\Curso Python\Archivos\calificaciones.txt", "a")

def escribir():
    while True:
        datos = input('Esriba un nombre y apellido del alumno, escriba "S" para salir: ')
        if datos == 'S':
            break
        else:
            nota = int(input('Escriba la nota del estudiante entre 1 y 10: '))
            if nota >= 9 and nota <= 10:
                calificacion='A'
            elif nota >= 8 and nota < 9:
                calificacion='B'
            elif nota >= 7 and nota < 8:
                calificacion='C'
            elif nota >= 6 and nota < 7:
                calificacion='D'
            else:
                calificacion='F'
            lista.write(datos+'\t'+str(nota)+'\n')
            print("La nota de " +datos+ " es " + calificacion)
 
escribir()       
lista.close()
