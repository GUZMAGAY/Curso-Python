""""
Crear ficheros o archivos
"""

from io import open 

archivo_texto = open(r"C:\Curso Python\Archivos\archivo.txt", "w")

frase = "Esto es un texto diferen al anterior"

archivo_texto.write(frase)

archivo_texto.close()