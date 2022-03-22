"""crear varios elementos caja de texto, donde se pueda ingresar un nombre y 
con un botón colocar ese nombre ne una etiqueta"""
import tkinter

ventana = tkinter.Tk() 
ventana.geometry('450x100')

txt = tkinter.Entry(ventana,font='Calibry 12')
etiqueta = tkinter.Label(ventana,font='Calibry 12', bg='pink', foreground='white', width=20)

def textoCajaTexto():
    textoA = txt.get()
    print(textoA)
    etiqueta["text"] = textoA

boton=tkinter.Button(ventana, text='Copiar', command=textoCajaTexto) 


txt.grid(row=1,column=0)
boton.grid(padx=10, pady=10,row=1,column=1)
etiqueta.grid(row=1, column=2)

txt2 = tkinter.Entry(ventana,font='Calibry 12')
etiqueta2 = tkinter.Label(ventana,font='Calibry 12', bg='pink', foreground='white', width=20)

def textoCajaTexto2():
    texto2 = txt2.get()
    print(texto2)
    etiqueta2["text"] = texto2

boton2=tkinter.Button(ventana, text='Copiar', command=textoCajaTexto2) 


txt2.grid(row=2,column=0)
boton2.grid(padx=10, pady=10,row=2,column=1)
etiqueta2.grid(row=2, column=2)
ventana.mainloop() #para que la ventana permanezca abierta
