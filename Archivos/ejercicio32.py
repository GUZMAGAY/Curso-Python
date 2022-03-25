"""Escribir una función que indique si el usuario es mayor de edad"""



class anios:
    def __init__(self,valor):
        self.valor=valor
        
    def mayor(self):
        if self.valor > 17 and self.valor <= 115:
            print('Usted es mayor de edad')
        elif self.valor >=1 and self.valor <= 17:
            print('Usted es menor de edad')
        else:
            print('No se aceptan números negativos o mayores a 115')

edad = int(input('Ingrese su edad: '))
calc = anios(edad)
print(calc.mayor())