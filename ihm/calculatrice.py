# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Button, Frame, StringVar
from tkinter import BOTTOM, LEFT, RIGHT, TOP
from itertools import product

"""
    1 etape: Afficher les chiffres les uns à la suite des autres
    2 etape: Prendre en compte l'opérateur 
            (remise à zero de l'affichage et sauvegarde de l'opérateur)
    3 etape: Quand on appuie sur "Enter" faire le calcul
"""
fen = Tk()

resultat = StringVar()
resultat.set("0")

def handle_number(e):
    print(e.widget.cget("text"))
    resultat.set(e.widget.cget("text"))
    
label = Label(fen, textvariable=resultat, height=2)
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
    button.bind("<Button-1>", handle_number)
    
fen.mainloop()
