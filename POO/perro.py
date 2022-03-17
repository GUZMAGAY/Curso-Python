class Perro:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} de {self.age} años"

    def ladrar(self):
        return f"{self.name} ladra fuerte"

perro_1 = Perro('Wolf',7)
print(perro_1)
print(perro_1.ladrar())