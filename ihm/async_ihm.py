# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Button, Frame, StringVar
from tkinter import BOTTOM, LEFT, RIGHT, TOP
from itertools import product
from time import sleep


fen = Tk()

compteur = StringVar()
compteur.set("0")

def inc_compteur():
    i = int(compteur.get()) + 1
    compteur.set(str(i))
    if i < 10:
        fen.after(1000, inc_compteur)

label = Label(fen, textvariable=compteur)
label.pack(side=BOTTOM)

button1 = Button(fen, text="Bouton 1")
button1.pack(side=LEFT, expand=True, fill='y')

button2 = Button(fen, text="Bouton 2")
button2.pack(side=RIGHT, expand=True, fill='y')

fen.after(2000, inc_compteur)
fen.mainloop()

