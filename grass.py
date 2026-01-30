import numpy as np
import random as rd


class Grass:
    def __init__(self, world, position, age):
        self.world = world
        self.position = position
        self.age = age
        self.compteur = 0
        self.dead = 0

    def die(self):
        self.compteur = 0
        self.age = 0
        self.world.grasses.remove(self)
        self.dead = 1

    def update(self):

        self.compteur += 1

        if (self.compteur == 10 or self.compteur == 20) and self.age < 3:
            self.age += 1
        if self.dead==1 and compteur>10:
            x = np.random()
            if x<0.7:
                self.age = 0
                self.dead = 0
                self.world.grasses.append(self)
