"""Ejemplo con while"""

"""contador = 0
while contador < 5:
    print(contador)
    contador += 1"""

#while con else
"""contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print('Dejo de contar')

print('El programa termino')"""

#while con if y break
"""contador = 0
while contador < 5:
    contador += 1
    if contador == 4:
        print('Se rompio')
        break
print(contador)"""

#while con continue
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        print('llego a tres')
        continue
print(contador)   