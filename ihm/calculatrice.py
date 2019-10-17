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
resultat.set("")

op1 = 0
op2 = 0
operator = "+"
is_reset = False

def handle_number(e):
    global is_reset
    if is_reset:
        is_reset = False
        return resultat.set(e.widget.cget("text"))
    resultat.set(resultat.get() + e.widget.cget("text"))

def handle_op(e):
    global operator, op1, op2
    op2 = int(resultat.get())
    if operator == "+":
        op1 += op2
    if operator == "-":
        op1 -= op2
    if operator == "*":
        op1 *= op2
    if operator == "/":
        op1 /= op2
    operator = e.widget.cget("text")
    resultat.set("")


def handle_enter(e):
    global operator, op1, op2, is_reset
    op2 = int(resultat.get())
    if operator == "+":
        op1 += op2
    if operator == "-":
        op1 -= op2
    if operator == "*":
        op1 *= op2
    if operator == "/":
        op1 /= op2
    resultat.set(str(op1))
    op1, op2, operator, is_reset = 0, 0, "+", True
    
label = Label(fen, textvariable=resultat, height=2)
label.pack()

button_enter = Button(fen, text="Enter", height=2)
button_enter.pack(side=BOTTOM, expand=True, fill='x')
button_enter.bind("<Button-1>", handle_enter)

frame_operator = Frame(fen)
frame_operator.pack(side=RIGHT)

frame_numbers = Frame(fen)
frame_numbers.pack()

button_zero = Button(fen, text="0", height=2)
button_zero.pack(expand=True, fill='x')
button_zero.bind("<Button-1>", handle_number)

for op in ["+","-","*","/"]:
    button = Button(frame_operator, text=op, width=5, height=2)
    button.pack()
    button.bind("<Button-1>", handle_op)

for i,j in product(range(3), range(3)):
    button = Button(frame_numbers, text=f"{3*(2-i)+j+1}", width=5, height=2)
    button.grid(column=j, row=i)
    button.bind("<Button-1>", handle_number)
    
fen.mainloop()
