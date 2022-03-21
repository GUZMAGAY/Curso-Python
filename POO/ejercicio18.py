"""Crear una clase Deportes 

Modificar el metodo __str__

E instanciar 3 objetos"""


class Deportes:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def __str__(self):
        return f"El deporte {self.nombre} es un deporte de tipo {self.tipo}"
    

natacion = Deportes('natacion','acuatico')
ajedrez = Deportes('ajedrez','mental')
surf = Deportes('surf','extremo')

print(natacion)
print(ajedrez)
print(surf)