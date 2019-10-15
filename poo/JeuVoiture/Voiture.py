# -*- coding: utf-8 -*-
import numpy as np


class Voiture:
    def tourner(self):
        self.direction = self.direction.dot(np.array([[0,1],[-1,0]]))
