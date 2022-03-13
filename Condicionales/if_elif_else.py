"""Ejemplos"""

"""Una persona necesita ingresar por teclado 1 valor numrico, este valor necesita comprobar lo siguiente:
Caso1: si este valor es positivo
Caso2: si este valor es negativo
Caso3: Si este valor es 0"""

#el valor que se ingresa desde un input se convierte en str, por lo que si es necesario deberá transformse a otro tipo de datos, como para el caso de este ejemplo
numero = input("Por favor ingres un valor numerico: ")

if int(numero) > 0:
    print(f"El valor ingresado es positivo: ", {numero})
elif int(numero) < 0:
    print(f"El valor ingresado es negativo: ", {numero})
else:
    print(f"El valor ingresado es cero: ", {numero})
