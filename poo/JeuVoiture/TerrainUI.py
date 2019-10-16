# -*- coding: utf-8 -*-
from .Terrain import Terrain
from tkinter import Tk, Canvas, PhotoImage

class TerrainUI(Terrain):
    def __init__(self):
        Terrain.__init__(self)
        self.fen = Tk()
        
        self.canvas = Canvas(self.fen, width=10*128, height=10*128)
        self.canvas.pack()
        
        self.photo_voiture = PhotoImage(file="car.png")
        self.canvas.create_image(128*4+64,64, image=self.photo_voiture)

    def start(self):
        self.fen.mainloop()
