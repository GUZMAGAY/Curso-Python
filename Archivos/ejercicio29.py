"""Ingresar nombre y apellido e imprimirlo al reves"""

nombre = input('Ingrese su nombre y apellido: ')

reves=''
for a in nombre:
    reves = a + reves

print(reves)
