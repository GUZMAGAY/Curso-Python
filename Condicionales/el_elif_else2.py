"""Saber el rango de edad de una persona 
Si es menor o igual a 12 años es un niño 
Si es mayor a 12 años pero menor a 18 años es un adolescente 
Si es mayor o igual a 18 años pero menor o igual a 60 es un adulto 
Si es mayor a 60 años es un adulto mayor"""

#De esta manera también se puede transformar el input a otro tipo de dato
edad = int(input("Por favor ingrese su edad: "))

if edad <= 12:
    print("Es un niño")
elif edad < 18:
    print("Es un adolescente")
elif edad <= 60:
    print("Es un adulto")
elif edad > 60 and edad <= 110:
    print("Es un adulto mayor")
else:
    print("La edad ingresa no es correcta")