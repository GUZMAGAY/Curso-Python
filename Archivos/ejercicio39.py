"""7. Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.

La función se llama calcular_total()

La función recibe dos parámetros:

1. pago_sin_impuesto

2. impuesto (Ej. Valor de 10, significa 10% de impuesto, Valor de 16 significa el 16% de impuesto)

La función debe regresar el total del pago incluyendo el porcentaje de impuesto proporcionado.

Ej. Si llamamos a la función calcular_total(1000, 16) debe retornar el valor 1,160.0

Los valores los debe proporcionar el usuario y se procesados con la función input, convirtiendolos a tipo float.
"""


pago_sin_impuesto = float(input('Ingrese el valor sin impuesto: '))
impuesto = float(input('Ingrese el valor del impuesto: '))

def calcular_total(pago,impuesto):
    impuesto = round(pago * impuesto /100,2)
    pago = pago + impuesto
    print(f"El total a pagar es de ${pago}")

calcular_total(pago_sin_impuesto, impuesto)