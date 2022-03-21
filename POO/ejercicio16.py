"""
Crear una clase padre que permita determinar algunos atributos basicos y metodos 
Crear 3 clases hijas que cambien el comportamiento tanto de atributos como de metodos de la clase padre 
que reciba a traves de la herencia"""

class Monoplaza:
    def __init__(self,velocidad,neumaticos,motor):
        self.velocidad=velocidad
        self.neumaticos=neumaticos
        self.motor=motor
        
    def marca(self):
        pass
    
    def aleron(self):
        pass
    
    def halo(self):
        pass
    
    def modelo(self):
        pass
    
class RedBull(Monoplaza):
    
    def __init__(self):
        pass
    
    def marca(self):
        print('-Red Bull')
        
    def aleron(self):
        print('- Carga extra con construcción menos rígida')
        
    def halo(self):
        print('- Fabricado de titanio')
    
    def modelo(self):
        print('- RB18')
    
class McLaren(Monoplaza):
    def __init__(self):
        pass
    
    def marca(self):
        print('- McLaren')
        
    def aleron(self):
        print('- Construccion rigida ')
        
    def halo(self):
        print('- Fabricado de titanio')
    
    def modelo(self):
        print('- MCL37')
        
class Ferrari(Monoplaza):
    def __init__(self):
        pass
    
    def marca(self):
        print('- Ferrari')
    
    def aleron(self):
        print('- Aleron flexible')
        
    def halo(self):
        print('- Fabricado de titanio')
    
    def modelo(self):
        print('- F1-75')
        

monoplazas = [RedBull(), McLaren(), Ferrari()]

for monoplaza in monoplazas:
    monoplaza.marca()
    monoplaza.aleron()
    monoplaza.halo()
    monoplaza.modelo()
    print('\n')