# -*- coding: utf-8 -*-

from JeuVoiture.Voiture import Voiture

"""
    Définir dans voiture une classe Voiture
    construite à partir de poistion
    qui contient une position et une direction
    en numpy array: self.direction = np.array([0,1])
    avancer() : position += direction
    tourner()
"""

voiture = Voiture([3,4])

for i in range(10):
    voiture.avancer()
    print(voiture.position)