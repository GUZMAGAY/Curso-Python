"""Encontrar el mayor de tres numeros ingresados por teclado
"""

numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
numero3 = int(input("Ingrese el tercer valor: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El primer valor ingresado es el mayor: ", {numero1})
elif numero2 > numero1 and numero2 > numero3:
    print(f"El segundo valor ingresado es el mayor: ", {numero2})
elif numero3 > numero1 and numero3 > numero2:
    print(f"El tercer valor ingresado es el mayor: ", {numero3})
else:
    print(f"Los números ingresados: {numero1}, {numero2} y {numero3} son iguales")

