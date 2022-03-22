import tkinter #libreria para importar las interfaces graficas

ventana = tkinter.Tk() #instanciando un objeto, crear una ventana
ventana.geometry('300x300') #para cambiar el tamaño de la ventan

boton1 = tkinter.Button(ventana, text='Bonton1ghhh')
boton2 = tkinter.Button(ventana, text='Bonton2')
boton3 = tkinter.Button(ventana, text='Bonton3')

#de esta manera indicamos la posicion en la ventana que van a tener los objetos
boton1.grid(row=0,column=0)
boton2.grid(row=1,column=0)
boton3.grid(row=3,column=2)

ventana.mainloop() #para que la ventana permanezca abierta
