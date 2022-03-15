"""def nombre(nombre='Nombre',apellido=3):
    yield nombre
    yield apellido

nombre_completo = nombre('Diego',5)
print(next(nombre))
print(next(nombre))
https://blog.adrianistan.eu/yield-generadores-python
"""

def generator():
    yield "Hola"
    yield "Mundo"

def main():
    f = generator()
    for x in f:
        print(x)

main()