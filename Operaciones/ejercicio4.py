"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
Matemáticas, Física, Química, Historia y Lengua) en una tupla y la muestre por pantalla.
"""

materias = ('Matematicas', 'Sociologia', 'Metodologia', 'Operativos')
print(materias)
print(type(materias))

"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una tupla y la muestre por pantalla el mensaje 
Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista."""

for mat in materias:
    print('Yo estudio ',mat)
    input()
"""Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
y muestre por pantalla el menor y el mayor de los precios."""

tupla = (50, 75, 46, 22, 80, 65, 8)
print('El numero menor de la tupla es: ',min(tupla))
print('El numero mayor de la tupla es: ',max(tupla))
print(type(tupla))
