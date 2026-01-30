import numpy as np
import random as rd


class Grass:
    def __init__(self, position, age):

        self.position = position
        self.age = age
        self.compteur = 0

    def update_grass(self):

        self.compteur += 1

        if (self.compteur == 10 or self.compteur == 20) and self.age < 3:
            self.age += 1

    def grass_ate(self):

        self.compteur = 0
        self.age = 0
