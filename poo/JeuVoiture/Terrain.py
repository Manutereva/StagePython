# -*- coding: utf-8 -*-
from .Voiture import Voiture
from .Obstacle import Obstacle
import numpy as np
from random import randint as rd


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
        """
            Ajouter plusieurs voitures aléatoirement avec randint
            Ajouter des obstacles (il faut se créer la classe Obtacle)
            Les voitures ne peuvent pas se superposer
            ni traverser les obstacles
        """
        self.liste_obstacles = [Obstacle([rd(0,10),rd(0,10)]) for i in range(10)]
        self.liste_voitures = [Voiture([rd(0,10),rd(0,10)]) for i in range(5)]
        self.taille = np.array([10,10])
        
    def fait_un_tour(self):
        for voit in self.liste_voitures:
            voit.avancer(self.is_accessible)
            
    def display(self):
        print("debut")
        for i in range(self.taille[0]+1):
            ligne = []
            for j in range(self.taille[1]+1):
                if self._is_voiture([i,j]):
                    ligne.append("X")
                elif self._is_obstacle([i,j]):
                    ligne.append("O")
                else:
                    ligne.append(" ")
            print("".join(ligne))
            
    def is_accessible(self, position):
        """
            return False si la position est accessible sur le
            terrain sinon return True
        """
        inside_board = ((position > self.taille).any() or
                (position < np.array([0,0])).any())
        return inside_board or \
            self._is_obstacle(position) or \
            self._is_voiture(position) \
        
    def _is_voiture(self, position):
        for voit in self.liste_voitures:
            if (voit.position == position).all():
                return True
        return False

    def _is_obstacle(self, position):
        for obs in self.liste_obstacles:
            if (obs.position == position).all():
                return True
        return False
    