# -*- coding: utf-8 -*-
import numpy as np


class Voiture:

    def __init__(self, position_init, direction_init=[1,0]):
        self.vecteur_vitesse = np.array(direction_init)
        self.position = np.array(position_init)
    
    def avancer(self, check_obstacle=lambda x: False):
        new_position = self.position + self.vecteur_vitesse
        if check_obstacle(new_position):
            self.tourner()
        else:
            self.position = new_position
        
    def tourner(self):
        self.vecteur_vitesse = self.vecteur_vitesse.dot(np.array([[0,1],[-1,0]]))

    def photo_image(self):
        if self.vecteur_vitesse.array_equal([0,1]):
            return PhotoImage(file="car.png")