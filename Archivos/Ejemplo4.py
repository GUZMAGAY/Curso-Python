""""
Abrir ficheros o archivos
"""

from io import open 

archivo_texto = open(r"C:\Curso Python\Archivos\archivo.txt", "a")

texto = archivo_texto.write("\nSiempre es bueno aprender")

archivo_texto.close()

