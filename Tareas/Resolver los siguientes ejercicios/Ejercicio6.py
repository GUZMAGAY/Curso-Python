"""Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza dicha función en un programa principal que lea el radio de una circunferencia y 
muestre su área y perímetro."""



def calculo(alto,ancho):
    area = alto * ancho
    perimetro = (alto + ancho) * 2
    print('Area: ', area)
    print('Perimetro: ', perimetro)

def main():
    alto = int(input('Proporciona el alto: '))
    ancho = int(input('Proporciona el ancho: '))
    calculo(alto,ancho)
    
main()