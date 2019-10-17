# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image, ImageTk


class Voiture:
    image_voiture = Image.open("car.png")
    def __init__(self, position_init, direction_init=[1,0]):
        self.vecteur_vitesse = np.array(direction_init)
        self.position = np.array(position_init)
        self._photo_image = None
    
    def avancer(self, check_obstacle=lambda x: False):
        new_position = self.position + self.vecteur_vitesse
        if check_obstacle(new_position):
            self.tourner()
        else:
            self.position = new_position
        
    def tourner(self):
        self.vecteur_vitesse = self.vecteur_vitesse.dot(np.array([[0,1],[-1,0]]))

    def photo_image(self):
        if (self.vecteur_vitesse == [0,1]).all():
            self._photo_image = ImageTk.PhotoImage(Voiture.image_voiture.rotate(-90))
        elif (self.vecteur_vitesse == [0,-1]).all():
            self._photo_image = ImageTk.PhotoImage(Voiture.image_voiture.rotate(90))
        elif (self.vecteur_vitesse == [1,0]).all():
            self._photo_image = ImageTk.PhotoImage(Voiture.image_voiture)
        elif (self.vecteur_vitesse == [-1,0]).all():
            self._photo_image = ImageTk.PhotoImage(Voiture.image_voiture.rotate(180))
        return self._photo_image
