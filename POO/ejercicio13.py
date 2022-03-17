"""
Crear una clase llamada animal 
    Crear 5 objetos
Razonar cuales son los metodos y atributos genericos que tienen los animales"""


class Animal:
    def __init__(self, clasificacion, subclasificacion,nombre):
        self.clasificacion = clasificacion
        self.subclasificacion = subclasificacion
        self.nombre = nombre
    
    def comer(self):
        print('Se alimenta')
    
    def trepar(self):
        print('Puede trepar')
    
    def veneno(self):
        print('Es venenoso')
    
    def nadar(self):
        print('Puede nadar')

    def volar(self):
        print('Puede volar')
    
    def respira_bajo_el_agua(self):
        print('Puede respirar bajo el agua')

gato = Animal('Vertebrado','Mamifero','Gato')
print(gato.nombre)
print(gato.clasificacion)
print(gato.subclasificacion)
gato.comer()
gato.trepar()

print('\n')

murcielago = Animal('Vertebrado','Mamifero','Murcielago')
print(murcielago.nombre)
print(murcielago.clasificacion)
print(murcielago.subclasificacion)
murcielago.comer()
murcielago.volar()

print('\n')

golondrina = Animal('Vertebrado','Ave','Golondrina')
print(golondrina.nombre)
print(golondrina.clasificacion)
print(golondrina.subclasificacion)
golondrina.comer()
golondrina.volar()

print('\n')

tilapia = Animal('Vertebrado','Peces','Tilapia')
print(tilapia.nombre)
print(tilapia.clasificacion)
print(tilapia.subclasificacion)
tilapia.comer()
tilapia.nadar()
tilapia.respira_bajo_el_agua()

print('\n')

rana = Animal('Vertebrado','Anfibio','Rana')
print(rana.nombre)
print(rana.clasificacion)
print(rana.subclasificacion)
rana.comer()
rana.nadar()
rana.respira_bajo_el_agua()

print('\n')

escorpion = Animal('Invertebrado','Artropodo','Escorpion')
print(escorpion.nombre)
print(escorpion.clasificacion)
print(escorpion.subclasificacion)
escorpion.comer()
escorpion.trepar()
escorpion.veneno()