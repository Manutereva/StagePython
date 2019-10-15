# -*- coding: utf-8 -*-
from .Voiture import Voiture
import numpy as np

class Terrain:
    """
        Faire une classe terrain qui possède une liste de
        voitures (avec une voiture donnée: 
            self.liste_voitures = [Voiture([4,3])]
            )   et une taille ([10, 10]).
        * Les voitures ne peuvent pas sortir du terrain
        La méthode fait_un_tour(self), fait avancer chaque voiture
        
        La méthode display afficher la position de chaque voiture
    """
    def __init__(self):
        self.liste_voitures = [Voiture([2,4])]
        self.taille = np.array([10,10])
        
    def fait_un_tour(self):
        for voit in self.liste_voitures:
            voit.avancer(self.check_obstacle)
            
    def display(self):
        for i, voit in enumerate(self.liste_voitures):
            print(f"voiture n{i} : {voit.position}")
            
    def check_obstacle(self, position):
        """
            return False si la position est accessible sur le
            terrain sinon return True
        """
        return ((position > self.taille).any() or
                (position < np.array([0,0])).any())
        
    