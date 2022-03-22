from ctypes import alignment
import tkinter #libreria para importar las interfaces graficas

ventana = tkinter.Tk() #instanciando un objeto, crear una ventana
ventana.geometry('300x300') #para cambiar el tamaño de la ventan

etiqueta = tkinter.Label(ventana, text ='Hola Mundo', bg='pink', foreground='white') #creacion de etiqueta, se debe especificar a que ventana pertenece
#etiqueta.pack(side=tkinter.LEFT) 
#etiqueta.pack(side=tkinter.RIGTH) 
#etiqueta.pack(side=tkinter.BOTTOM) 
#etiqueta.pack(side=tkinter.TOP) #esto se coloca etiqueta.pack() después de la creacion caso contrario no se va a mostrar
#etiqueta.pack(fill=tkinter.X) #ocupa toda la linea
#etiqueta.pack(fill=tkinter.Y, expand=True) #ocupa todo el alto de la ventana
etiqueta.pack(fill=tkinter.BOTH, expand=True) #ocupa toda la ventana
ventana.mainloop() #para que la ventana permanezca abierta
