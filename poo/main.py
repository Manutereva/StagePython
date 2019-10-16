# -*- coding: utf-8 -*-
from JeuVoiture.Terrain import Terrain
from time import sleep
import os


"""
    Définir dans voiture une classe Voiture
    construite à partir de poistion
    qui contient une position et une direction
    en numpy array: self.direction = np.array([0,1])
    avancer() : position += direction
    tourner()
"""

terrain = Terrain()

for i in range(50):
    os.system("cls")
    terrain.fait_un_tour()
    terrain.display()
    sleep(0.5)
    
