import os #libreria para ejecutar comandos propios del sistema

if os.path.exists(r"C:\Curso Python\Archivos\eliminar"): #valida si la carpeta existe en la ruta
    os.rmdir(r"C:\Curso Python\Archivos\eliminar") #para eliminar carpetas
else:
    print("El directorio no existe")