# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Button, Frame
from tkinter import BOTTOM, LEFT, RIGHT, TOP
from itertools import product


fen = Tk()

label = Label(fen, text="", height=2)
label.pack()

button_enter = Button(fen, text="Enter", height=2)
button_enter.pack(side=BOTTOM, expand=True, fill='x')

frame_operator = Frame(fen)
frame_operator.pack(side=RIGHT)

frame_numbers = Frame(fen)
frame_numbers.pack()

button_zero = Button(fen, text="0", height=2)
button_zero.pack(expand=True, fill='x')

for op in ["+","-","*","/"]:
    button = Button(frame_operator, text=op, width=5, height=2)
    button.pack()

for i,j in product(range(3), range(3)):
    button = Button(frame_numbers, text=f"{3*(2-i)+j+1}", width=5, height=2)
    button.grid(column=j, row=i)
    
fen.mainloop()
