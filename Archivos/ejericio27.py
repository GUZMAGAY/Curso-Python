"""Crear un archivo
Elegir la ruta y el nombre mas adecuada donde deesee crearlo
Eligir la opción de: 
    Write: w
    Read: r
    Abrir: a

Escribir los nombres de 5 personas a traves de variables
   
No olvidar cerrar el archivo
"""

from io import open 

#escribiendo el archivo
archivo = open(r"C:\Curso Python\Archivos\ejericio.txt", "a")

i = 0
while i < 5:
    nombres = input('Esriba un nombre: ')
    archivo.write(nombres+'\n')
    i +=1
   
archivo.close()

#leyendo el archivo
leer = open(r"C:\Curso Python\Archivos\ejericio.txt", "r")
texto = leer.readlines() 
leer.close()
l=0
while l < 5:
    print(texto[l])
    l +=1 