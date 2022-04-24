from struct import pack
from tkinter import *
import numpy as np
import sounddevice as sd
import soundfile as sf

volumenM = 1

raiz=Tk()
raiz.title("Reproductor")
ventana = Frame()

ventana.pack(fill="both",expand="True")

ventana.config(bg="black")
ventana.config(width="650",height="350")

def Sonido(volumen):
    x,fs = sf.read('acdc.wav',dtype='float32')

    y = volumen * x
    muestras = 1*fs 
    zeros = np.zeros( muestras-1, dtype=int)
    sd.play(y,fs)
    status = sd.wait()

def Volumen_Menos():
    v = volumenM - 0.1
    return v

VolumenMenos = Button(raiz, text="-" , command=lambda:Volumen_Menos())
VolumenMenos.pack()

Reproducir = Button(ventana, text="Reproducir" , command=lambda:Sonido(volumenM))
Reproducir.grid(row=0 , column= 1)

raiz.mainloop()