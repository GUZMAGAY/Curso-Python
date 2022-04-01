"""Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y 
te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer 
login incremente este valor.

Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
solamente tenemos tres oportunidades para intentarlo."""


def Login(usuario,contrasenia):
    Login = True
    if usuario == 'usuario1' and contrasenia == 'asdasd':
        return True
    else:
        return False    
    
def main():
    contador = 0
    while contador < 3:
        usuario = input('Escriba el usuario: ')
        constrasenia = input('Escriba la contraseña: ')
        
        if Login(usuario,constrasenia) == False: 
            print('Login incorrecto')
            contador = contador + 1
        elif Login(usuario,constrasenia) == True:
            print('Acceso exitoso')
            break

main()