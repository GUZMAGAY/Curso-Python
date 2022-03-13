"""Escribe un programa que pida un nombre de usuario y una contraseña y 
si se ha introducido 'pepe' y 'passwd#' se indica “Has entrado al sistema”,
 sino se da un error."""

usuario = 'pepe'
clave = 'passwd#'

val_usuario = input('Ingrese su usuario: ')
val_clave = input('Ingrese su clave: ')

if val_usuario == usuario and val_clave == clave:
    print('Has entrado al sistema')
else:
    print('Error, credenciales incorrectas')