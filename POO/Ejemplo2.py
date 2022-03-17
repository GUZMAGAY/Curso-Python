class Vehiculo:

    def __init__(self, tipo, motor):
        self.tipo=tipo #atributos
        self.motor=motor
    
    def acelerar(self): #metodo
        print('Estoy acelerando')
    
    def frenar(self): #metodo
        print('Estoy frenando')
    
    def girar_a_la_derecha(self): #metodo
        print('Estory girando a la derecha')
    
    def girar_a_la_izquierda(self): #metodo
        print('Estory girando a la izquierda')

    def cambiar_marcha(self): #metodo
        print('Estor cambiando de marcha')

moto=Vehiculo('moto', '125') #objeto
print(moto.tipo) #llamada atributos
print(moto.motor)
moto.acelerar() #llamada al metodo
moto.frenar()
moto.girar_a_la_derecha()
moto.girar_a_la_izquierda()

carro = Vehiculo('carro','1800cc')
print(carro.tipo)
print(carro.motor)
carro.frenar()