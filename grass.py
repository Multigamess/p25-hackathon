import numpy as np
import random as rd


class Grass:
    def __init__(self, world, position, age):
        self.world = world
        self.position = position
        self.age = age
        self.compteur = 0

    def update(self):

        self.compteur += 1

        if (self.compteur == 10 or self.compteur == 20) and self.age < 3:
            self.age += 1

    def die(self):
        self.compteur = 0
        self.age = 0
        self.world.grasses.remove(self)
