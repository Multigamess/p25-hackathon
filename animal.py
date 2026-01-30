from random import randint as rd
import numpy as np


class Animal:
    def __init__(self, world, energy, position):
        self.world = world
        self.energy = energy
        self.position = position
        self.age = 0
        self.compteur = 0

    def upgrade_energy(self):
        self.compteur += 1

        if (self.compteur == 20 or self.compteur == 40) and self.age < 3:
            self.age += 1

        if self.compteur == 20:
            self.energy -= 10

    def get_next_move(self, target):
        dx = target[0] - self.position[0]
        dy = target[1] - self.position[1]

        if abs(dx) + abs(dy) == 0:
            return (0, 0)

        # probability to go in x direction
        p = abs(dx)/(abs(dx) + abs(dy))
        if np.random.rand() < p:
            sign = int(np.sign(dx + 0.5))
            return (sign, 0)
        else:
            sign = int(np.sign(dx + 0.5))
            return (0, sign)