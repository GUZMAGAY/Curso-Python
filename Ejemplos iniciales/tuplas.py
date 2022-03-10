"""Ejemplo de tuplas"""

#las tuplas no se pueden modificar, instrucciones como append o remove no son aplicables
#las tuplas se definen con paréntesis las listas con corchetes
tupla1= (4, 5, 'Juan', True, 5>4, 'Curso')
print(type(tupla1))
print(tupla1)

#aunque se declaran con paréntesis, para acceder a sis índices se realiza con corchetes
print(tupla1[4])