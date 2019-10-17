# -*- coding: utf-8 -*-
from .Terrain import Terrain
from tkinter import Tk, Canvas, PhotoImage
from random import randint as rd
from PIL import Image, ImageTk


class TerrainUI(Terrain):
    def __init__(self):
        Terrain.__init__(self)
        self.fen = Tk()
        
        self.canvas = Canvas(
                self.fen,
                width=(self.taille[0]+1)*128,
                height=(self.taille[1]+1)*128
                )
        self.canvas.pack()
        
    def run(self):
        self.fait_un_tour()
        self.canvas.delete("all")
        for voit in self.liste_voitures:
            self.canvas.create_image(
                    128*voit.position[0] + 64,
                    128*voit.position[1] + 64,
                    image=voit.photo_image())
        
        self.fen.after(1000, self.run)
    def start(self):
        self.fen.after(1000, self.run)
        self.fen.mainloop()
