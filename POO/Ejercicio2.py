"""
Crear una clase de algún animal específileConfig

Ejemplo de clase 
    Gato 
    Caballo
Definir en el metodo __init__ por lo menos 5 caracteristicas que los identifiquen
Definir en el método __str__ un mensaje que resalte por lo menos  2 caracteristicas del metodo __init__
En la instancia poder tener diferencias entre objetos propios de la misma clase"""

class Gato:
    def __init__(self, nombre, color, edad, tamanio, raza):
        self.nombre = nombre
        self.color = color
        self.edad = edad
        self.tamanio = tamanio
        self.raza = raza
    
    def __str__(self):
        return f"Mi nombre es {self.nombre} y soy de raza {self.raza}"

    def flexible(self):
        return f"- {self.nombre} tiene gran flexibilidad"
    
    def agil(self):
        return f"- {self.nombre} puede saltar hasta 3 metros"

    def cazar(self):
        return f"- {self.nombre} es un buen cazador"
    
    def temperamento(self):
        return f"- {self.nombre} no le gusta que lo toquen"
    
    def enfermedad(self):
        return f"- {self.nombre} tiene problemas renales"
    
    def banio(self):
        return f"- {self.nombre} pasa gran parte del día bañandose"


gato1 = Gato('Songo','Amarillo y Blanco',10,'grande','de todas un poco')
print(gato1)
print(gato1.agil())
print(gato1.temperamento())
print(gato1.flexible())

print('\n')

gato1 = Gato('Puerquin','Amarillo',7,'mediano','criolla')
print(gato1)
print(gato1.cazar())
print(gato1.enfermedad())
print(gato1.banio())