import tkinter #libreria para importar las interfaces graficas

ventana = tkinter.Tk() #instanciando un objeto, crear una ventana
ventana.geometry('300x300') #para cambiar el tamaño de la ventan

#cajas de texto

#txt = tkinter.Entry(ventana)
#txt = tkinter.Entry(ventana,font='Calibry 50') #cambia la fuente y el tamaño
txt = tkinter.Entry(ventana)
etiqueta = tkinter.Label(ventana)
txt.pack()
etiqueta.pack()

def textoCajaTexto():
    textoA = txt.get()
    print(textoA)
    etiqueta["text"] = textoA

boton=tkinter.Button(ventana, text='clic', command=textoCajaTexto) #pasa el valor ingresado en la caja de texto a la etiqueta
boton.pack()
ventana.mainloop() #para que la ventana permanezca abierta
