class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print('guau')
        
class Gato(Animal):
    def hablar(self):
        print('miau')

class Vaca(Animal):
    def hablar(self):
        print('muu')
        
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    animal.hablar()