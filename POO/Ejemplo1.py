class Monster:
    def __init__(self,nombre,categoria):
        self.nombre = nombre
        self.categoria = categoria
    def myfunc(self):
        print('Hey, yo soy ' + self.nombre)

monstruito = Monster('Sullivan', 'Asustador')
print(monstruito.categoria)
monstruito.myfunc()

monstruito2 = Monster('Mike', 'Ayudante')
monstruito2.myfunc()