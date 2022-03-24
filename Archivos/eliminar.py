import os #libreria para ejecutar comandos propios del sistema

if os.path.exists(r"C:\Curso Python\Archivos\archivo.txt"): #valida si el archivo existe en la ruta
    os.remove(r"C:\Curso Python\Archivos\archivo.txt") #para eliminar archivos
else:
    print("El archivo no existe")