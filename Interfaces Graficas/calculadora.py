"""crear una calculadora sencilla con tkinter"""

from tkinter import *
import tkinter

ventana = tkinter.Tk()
ventana.title('Calculadora') #nombre de la ventra
ventana.geometry('268x310')

icono=PhotoImage(file=r"C:\Curso Python\Interfaces Graficas\backspace.png")
icono = icono.zoom(1)

#caja de texto
txt1 = tkinter.Entry(ventana, font='Calibry 16',justify = RIGHT, width=22)
txt1.grid(row=0, column=0, columnspan=5)

#funciones
i = 0
def click_boton(valor):
    """insertar numeros en caja de texto"""
    global i
    txt1.insert(i, valor)
    i += 1

def borrar_txt():
    """boton borrar todo"""
    txt1.delete(0, END)
    i = 0
    
    
def igual_txt():
    """boton igual"""
    ecuacion = txt1.get() #traigo el valor de la caja de texto
    resultado = eval(ecuacion) #con eval tranforma el contenido de la caja de texto y ejecuta la operacion
    txt1.delete(0, END) #borro el contenido de la caja de texto
    txt1.insert(0, resultado) #se inserta en la caja de texto el resultado de la operacion
    i = 0
    
def backspace():
    """boton de retroceso"""
    input_len = len(txt1.get())
    txt1.delete(input_len - 1)
    
#botones

boton1 = tkinter.Button(ventana, text='1',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(1))
boton2 = tkinter.Button(ventana, text='2',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(2))
boton3 = tkinter.Button(ventana, text='3',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(3))
boton4 = tkinter.Button(ventana, text='4',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(4))
boton5 = tkinter.Button(ventana, text='5',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(5))
boton6 = tkinter.Button(ventana, text='6',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(6))
boton7 = tkinter.Button(ventana, text='7',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(7))
boton8 = tkinter.Button(ventana, text='8',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(8))
boton9 = tkinter.Button(ventana, text='9',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(9))
boton0 = tkinter.Button(ventana, text='0',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton(0))

suma = tkinter.Button(ventana, text='+',width=8, height=3,bg='#C8C8C8',font=('Calibry', 9,'bold'), command=lambda: click_boton('+'))
resta = tkinter.Button(ventana, text='-',width=8, height=3,bg='#C8C8C8',font=('Calibry', 9,'bold'), command=lambda: click_boton('-'))
division = tkinter.Button(ventana, text='/',width=8, height=3,bg='#C8C8C8',font=('Calibry', 9,'bold'), command=lambda: click_boton('/'))
multiplicacion = tkinter.Button(ventana, text='*',width=8, height=3,bg='#C8C8C8',font=('Calibry', 9,'bold'), command=lambda: click_boton('*'))

borrar = tkinter.Button(ventana, text='CE',width=8, height=3,bg='#C8C8C8',font=('Calibry', 9,'bold'), command=lambda: borrar_txt())
igual = tkinter.Button(ventana, text='=',width=8, height=3,bg='#C8C8C8',font=('Calibry', 9,'bold'), command=lambda: igual_txt())
punto = tkinter.Button(ventana, text='.',width=8, height=3,font=('Calibry', 9,'bold'), command=lambda: click_boton('.'))
retroceso = tkinter.Button(ventana, image=icono ,width=59, height=51,font=('Calibry', 9,'bold'), command=lambda: backspace())

parentesis1 = tkinter.Button(ventana, text='(',width=8, height=3,bg='#C8C8C8',font=('Calibry', 9,'bold'), command=lambda: click_boton('('))
parentesis2 = tkinter.Button(ventana, text=')',width=8, height=3,bg='#C8C8C8',font=('Calibry', 9,'bold'), command=lambda: click_boton(')'))

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
retroceso.grid(row=5,column=0)
parentesis1.grid(row=1,column=0)
parentesis2.grid(row=1,column=1)

ventana.mainloop()