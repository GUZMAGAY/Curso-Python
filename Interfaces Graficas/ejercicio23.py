from ctypes import alignment
import tkinter #libreria para importar las interfaces graficas

ventana = tkinter.Tk() #instanciando un objeto, crear una ventana
ventana.geometry('300x300') #para cambiar el tamaño de la ventan

#BOTONES
"""def saludo():
    print('Hola Mundo') #con print lo impreme en consola"""
def saludo(nombre):
    print('Hola', nombre)
       
#boton = tkinter.Button(ventana, text='Presionar', padx=50, pady=50) #padx y pady para cambiar el tamaño
#boton = tkinter.Button(ventana, text='Presionar', command=saludo) #para que el boton se vincule a la funcion
#boton = tkinter.Button(ventana, text='Presionar', command=lambda: saludo('Daniela')) #vincular la funcion con parametros
boton = tkinter.Button(ventana, text='Presionar', command=lambda: print('Daniela'))
boton.pack() #si falta la propiedad pack el objeto no se va a mostrar

ventana.mainloop() #para que la ventana permanezca abierta
