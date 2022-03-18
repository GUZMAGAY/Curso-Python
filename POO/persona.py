class Abuelo:
    def __init__(self,nombre,apellido,edad):
        self.nombre= nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"Yo soy la clase Abuelo, mi nombre es {self.nombre}" 
    
    def contarHistorias(self,epoca):
        self.epoca=epoca
        return f"Esta historia pasó en la epoca de {self.epoca}"

class Padre(Abuelo):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre,apellido,edad)
        
    def __str__(self):
        return super().__str__()
    
    def empleo(self,profesion):
        self.profesion = profesion
        return f"Yo tengo la profesion de  {self.profesion}" 

class Hijo(Padre):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre,apellido,edad)
    
    def __str__(self):
        return super().__str__()
    
    def jugar(self,deporte):
        self.deporte = deporte
        return f"Yo suelo juegar {self.deporte}"
    
Juan = Padre('Juan','Perez',40)
print(Juan.empleo('Carpintero'))

Luisa = Hijo('Luisa','Perez',12)
print(Luisa)
print(Luisa.contarHistorias('antes de 1980'))
