from random import randint as rd
import numpy as np


class Animal:
    def __init__(self, world, energy, position, ernergy_loss_per_turn):
        self.world = world
        self.energy = energy
        self.position = position
        self.age = 0
        self.tick = 0

    def upgrade_energy(self, energy_loss):
        if (self.tick == 20 or self.tick == 40) and self.age < 3:
            self.age += 1

        if self.tick % 10 == 0:
            self.energy -= energy_loss

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
