"""El día juliano correspondiente a una fecha es un número entero que indica los días que han 
transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que al 
introducir una fecha nos diga el día juliano que corresponde. 
Para ello podemos hacer las siguientes subrutinas:

LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
EsBisiesto: Recibe un año y nos dice si es bisiesto.
Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano."""

def EsBisiesto(anio):
    if anio % 4 != 0: 
        return False
    elif anio % 4 == 0 and anio % 100 != 0: 
        return True
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: 
        return False
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: 
        return True
    
def DiasDelMes(mes2,anio):
    dias = 0
    if mes2 == 1 or mes2 == 3 or mes2 == 5 or mes2 == 7 or mes2== 8 or mes2== 10 or mes2 == 12:
        dias = 31
    elif mes2 == 4 or mes2 == 6 or mes2== 9 or mes2 == 11:
        dias = 30
    elif mes2 == 2:
        if EsBisiesto(anio):
            dias = 29
        else:
            dias = 28
    return dias
    

def Calcular_Dia_Juliano(dia,mes,anio):
    mes2 = 1
    diaj = 0
    for mes2 in range(mes):
        diaj = diaj + DiasDelMes(mes2,anio)
    diaj = diaj + dia
    return diaj

def LeerFecha():
    dia = int(input('Ingrese el día de la fecha en número: '))
    mes = int(input('Ingrese el mes de la fecha en número: '))
    anio = int(input('Ingrese el año de la fecha en número: '))
    print("Día Juliano: ",Calcular_Dia_Juliano(dia,mes,anio))
    
LeerFecha()
    