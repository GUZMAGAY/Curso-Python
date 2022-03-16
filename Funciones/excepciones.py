"""Aqui va el codigo de excepciones"""

"""while True:
    try: #intenta ejecutar le codigo
        x = int(input('Por favor ingrese un numero: '))
        break
    except ValueError: #maneja el error
        print('Oops! No era valido, Intenta de nuevo')"""

def suma():
    try: 
        a = int(input('Por favor ingrese un valor: '))
        b = int(input('Por favor ingrese un segundo valor: '))
        sum = a + b
        return sum       
    except ValueError:
        print('Número no valido')
    
print(suma())