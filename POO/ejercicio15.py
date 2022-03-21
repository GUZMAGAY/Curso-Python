class Cuenta:
    
    def __init__(self):
        self.__numero = 12345
        self.__tipo = 'ahorro'
        
    def __pass(self):
        return f"Valor privado"
    
    def __monto(self):
        return f"Monto no disponible para consulta"
    
    def cta(self):
        return self.__numero
    
    def tip(self):
        return self.__tipo
    
    def acceso(self):
        return self.__pass()
    
    def valor(self):
        return self.__monto()

c = Cuenta()

print(c.cta())
print(c.tip())
print(c.acceso())
print(c.valor())



