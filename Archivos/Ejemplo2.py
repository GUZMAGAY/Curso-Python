""""
Leer ficheros o archivos
"""

from io import open 

archivo_texto = open(r"C:\Curso Python\Archivos\archivo.txt", "r")

texto = archivo_texto.read()

archivo_texto.close()

print(texto)