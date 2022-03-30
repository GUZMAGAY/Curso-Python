"""4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

Nota: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

Comprueba el punto intermedio entre -12 y 24"""

def intermedio(num1,num2):
    calculo = round((num1 + num2) / 2,2)
    return f"El punto intermedio de {num1} y {num2} es {calculo}"

print(intermedio(-12,24))