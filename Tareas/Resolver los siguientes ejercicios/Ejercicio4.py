"""Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena 
con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
Crea un programa principal donde se use dicha función."""


def main():
    frase = input('Escriba una frase: ')
    print(ConvertirEspaciado(frase))

def ConvertirEspaciado(frase):
    espaciado=''
    for letra in frase:
        espaciado = espaciado +' '+ letra 
    return espaciado

main()