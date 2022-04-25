from tkinter import *
import numpy as np
import sounddevice as sd
import soundfile as sf




raiz=Tk()
raiz.title("Reproductor")
ventana = Frame()

ventana.pack(fill="both",expand="True")

ventana.config(bg="black")
ventana.config(width="650",height="350")

def Sonido():
    x,fs = sf.read('acdc.wav',dtype='float32')
    muestras = 1*fs 
    zeros = np.zeros( muestras-1, dtype=int)
    sd.play(x,fs)
    status = sd.wait()

Reproducir = Button(ventana, text="Reproducir" , command=lambda:Sonido())
Reproducir.grid(row=1 , column= 0)

raiz.mainloop()