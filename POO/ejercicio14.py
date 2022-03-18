"""Crear dos clases 

Ejemplo

Toro y una Vaca 

Toro: y sus caracteristicas
Vaca: da leche, se obtiene mantequilla

Ternero(Toro)
Ternera(Vaca)"""

class Toro():
    def __init__(self,raza,color,edad,longitud,alto):
        self.raza =  raza
        self.color = color
        self.edad = edad
        self.longitud = longitud
        self.alto = alto
    
    def __str__(self):
        return f"-Soy un toro de raza {self.raza} de color {self.color}, soy un adulto de {self.edad} años, mido {self.longitud} cm de longitud y {self.alto} cm de alto"        
    
    def cornamenta(self):
        return f"-Tiene buena cornamenta"
    
    def salud(self):
        return f"-Poseo excelente salud"
    
class Vaca():
    def __init__(self,raza,color,edad,longitud,alto):
        self.raza =  raza
        self.color = color
        self.edad = edad
        self.longitud = longitud
        self.alto = alto
        
    def __str__(self):
        return f"-Soy una vaca de raza {self.raza} de color {self.color}, tengo {self.edad} años, mido {self.longitud} cm de longitud y {self.alto} cm de alto"        
    
    def produccion(self,litros):
        self.litros=litros
        return f"-Puedo producir {litros} litros de leche al año"
    
    def gestacion(self):
        return f"Puedo gestar a una única cría cada vez"
    
class Novillo(Toro):
    def __init__(self, raza, color, edad, longitud, alto):
        super().__init__(raza, color, edad, longitud, alto)
    
    def __str__(self):
        return f"-Soy un novillo de raza {self.raza} de color {self.color}, soy un adulto de {self.edad} años, mido {self.longitud} cm de longitud y {self.alto} cm de alto"        
    
    def temperamento(self,caracter):
        self.caracter=caracter
        return f"-Mi temperamento es {caracter}"
            
class Ternera(Vaca):
    def __init__(self, raza, color, edad, longitud, alto):
        super().__init__(raza, color, edad, longitud, alto)
    
    def __str__(self):
        return f"-Soy una ternera de raza {self.raza} de color {self.color}, soy un adulto de {self.edad} años, mido {self.longitud} cm de longitud y {self.alto} cm de alto"        
    
    def carne(self):
        return f"Mi carne aporta mucho hierro"

Lidia = Toro('Lidia','negro',4,250,150)
print(Lidia)
print(Lidia.cornamenta())

Holstein =Vaca('Holstein', 'blanco y negro',5,200,150)
print(Holstein)
print(Holstein.produccion(10000))

Angus = Novillo('Angus','Negro',1,200,100)
print(Angus)
print(Angus.salud())

Brown = Ternera('Brown Swiss','cafe', 1,180,100)
print(Brown)
print(Brown.carne())