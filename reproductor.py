import tkinter as tk
import pygame
import os


root= tk.Tk()

repro = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
repro.pack()
titulo = tk.Label(root, text='El Kaspotify')
titulo.config(font=('helvetica', 14))
repro.create_window(200, 25, window=titulo)

os.chdir("C:/Users/santi/Desktop/Codigo y Demas/Reproductor/canciones")
canciones=os.listdir()
print(canciones)
i=0

cancion=canciones[i]

pygame.mixer.init()


def play ():
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    
def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()
    
def volumen_down():
    volumen=pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(volumen-0.05)

def volumen_up():
    volumen=pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(volumen+0.05) 

def siguiente_cancion():
    global i
    i=i+1
    pygame.mixer.music.pause()
    pygame.mixer.music.load(canciones[i])
    pygame.mixer.music.play()

def anterior_cancion():
    global i
    i=i-1
    pygame.mixer.music.pause()
    pygame.mixer.music.load(canciones[i])
    pygame.mixer.music.play()


titulo_cancion = tk.Label(root, text=cancion)
titulo_cancion.config(font=('helvetica', 14))
repro.create_window(200, 100, window=titulo_cancion)

reproducir = tk.Button(text='Reproducir', command=play)
repro.create_window(200, 180, window=reproducir)

parar = tk.Button(text='Parar', command=stop)
repro.create_window(200, 240, window=parar)

pausa = tk.Button(text='Pausar', command=pause)
repro.create_window(300, 180, window=pausa)

continuar = tk.Button(text='Continuar', command=unpause)
repro.create_window(300, 240, window=continuar)

vol_down = tk.Button(text='Menos', command=volumen_down)
repro.create_window(100, 240, window=vol_down)

vol_up = tk.Button(text='Mas', command=volumen_up)
repro.create_window(100, 180, window=vol_up)

sigue = tk.Button(text='Siguiente', command=siguiente_cancion)
repro.create_window(50, 240, window=sigue)

ante = tk.Button(text='Anterior', command=anterior_cancion)
repro.create_window(50, 180, window=ante)


root.mainloop()