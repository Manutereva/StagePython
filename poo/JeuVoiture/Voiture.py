# -*- coding: utf-8 -*-
import numpy as np


class Voiture:

    def __init__(self, position_init, direction_init):
        self.vecteur_vitesse = np.array(direction_init)
        self.position = np.array(position_init)
    
    def avancer(self):
        self.position += self.vecteur_vitesse
        
    def tourner(self):
        self.direction = self.vecteur_vitesse.dot(np.array([[0,1],[-1,0]]))
