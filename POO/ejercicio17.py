"""Crear una clase Persona con los siguientes atributos 
Metodo __init__ 
Nombre 
Apellido 
Fecha de Nacimiento 

Saludar 
Despedirse 

Instanciar 3 objetos"""

class Persona:
    def __init__(self,nombre,apellido,fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
    
    def saludar(self):
        return f"Buenos dias {self.nombre}"
        
    def despedirse(self):
        return f"Hasta mañana {self.nombre}"
    

juan = Persona('Juan','Perez','23-08-1980')
print(juan.nombre)
print(juan.apellido)
print(juan.fecha_nacimiento)
print(juan.saludar())
print(juan.despedirse())
print('\n')
pedro = Persona('Pedro','Gimenez','05-10-1990')
print(pedro.nombre)
print(pedro.apellido)
print(pedro.fecha_nacimiento)
print(pedro.saludar())
print(pedro.despedirse())
print('\n')
martha = Persona('Martha','Alava','10-11-1987')
print(martha.nombre)
print(martha.apellido)
print(martha.fecha_nacimiento)
print(martha.saludar())
print(martha.despedirse())