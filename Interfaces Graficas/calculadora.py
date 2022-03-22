"""crear una calculadora sencilla con tkinter"""

from tkinter import *
import tkinter

ventana = tkinter.Tk()
ventana.geometry('800x600')

#caja de texto
txt1 = tkinter.Entry(ventana, font='Calibry 16',width=22)
txt1.grid(row=0, column=0, columnspan=5)


#botones

boton1 = tkinter.Button(ventana, text='1',width=8, height=3)
boton2 = tkinter.Button(ventana, text='2',width=8, height=3)
boton3 = tkinter.Button(ventana, text='3',width=8, height=3)
boton4 = tkinter.Button(ventana, text='4',width=8, height=3)
boton5 = tkinter.Button(ventana, text='5',width=8, height=3)
boton6 = tkinter.Button(ventana, text='6',width=8, height=3)
boton7 = tkinter.Button(ventana, text='7',width=8, height=3)
boton8 = tkinter.Button(ventana, text='8',width=8, height=3)
boton9 = tkinter.Button(ventana, text='9',width=8, height=3)
boton0 = tkinter.Button(ventana, text='0',width=8, height=3)

suma = tkinter.Button(ventana, text='+',width=8, height=3)
resta = tkinter.Button(ventana, text='-',width=8, height=3)
division = tkinter.Button(ventana, text='/',width=8, height=3)
multiplicacion = tkinter.Button(ventana, text='*',width=8, height=3)

borrar = tkinter.Button(ventana, text='CE',width=8, height=3)
igual = tkinter.Button(ventana, text='=',width=8, height=3)
punto = tkinter.Button(ventana, text='.',width=8, height=3)

parentesis1 = tkinter.Button(ventana, text='(',width=8, height=3)
parentesis2 = tkinter.Button(ventana, text=')',width=8, height=3)
#posicion botones

boton1.grid(row=4,column=0)
boton2.grid(row=4,column=1)
boton3.grid(row=4,column=2)
boton4.grid(row=3,column=0)
boton5.grid(row=3,column=1)
boton6.grid(row=3,column=2)
boton7.grid(row=2,column=0)
boton8.grid(row=2,column=1)
boton9.grid(row=2,column=2)
boton0.grid(row=5,column=1)

suma.grid(row=4,column=4)
resta.grid(row=3,column=4)
multiplicacion.grid(row=2,column=4)
division.grid(row=1,column=4)

borrar.grid(row=1,column=2)
igual.grid(row=5,column=4)
punto.grid(row=5,column=2)

parentesis1.grid(row=1,column=0)
parentesis2.grid(row=1,column=1)

ventana.mainloop()