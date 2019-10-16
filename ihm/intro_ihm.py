# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Button, Frame
from tkinter import BOTTOM, LEFT, RIGHT, TOP
from itertools import product


fen = Tk()

label = Label(fen, text="We love Python")
label.pack(side=BOTTOM)

button1 = Button(fen, text="Bouton 1")
button1.pack(side=LEFT, expand=True, fill='y')

button2 = Button(fen, text="Bouton 2")
button2.pack(side=RIGHT, expand=True, fill='y')

frame = Frame(fen)
frame.pack()

for i,j in product(range(3), range(3)):
    button = Button(frame, text=f"{i}-{j}", width=5, height=2)
    button.grid(column=j, row=i)

fen.mainloop()
