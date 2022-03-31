from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=12)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)
    
class Trabajador(models.Model):
    #Campo para la relacion
    
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    
    #Es posible indicar un valor por defecto mediante default 
    antiguedad = models.IntegerField(default=0)
    
    def __str__(self):
        
        texto = "{0}, {1}"
        return texto.format(self.empresa,self.nombre)
        