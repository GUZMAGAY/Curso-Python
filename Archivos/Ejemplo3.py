""""
Leer ficheros o archivos
"""

from io import open 

archivo_texto = open(r"C:\Curso Python\Archivos\archivo.txt", "r")

texto = archivo_texto.readlines() #lee el archivo como una lista

archivo_texto.close()

print(texto[2]) #se imprime mediante índices