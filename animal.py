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
            print("in x ")
            return int(np.sign(dx + 0.5)) * (1, 0)
        else:
            print("in y ", np.sign(dy + 0.5))
            return int(np.sign(dy + 0.5)) * (0, 1)

    # def next_move(self, target):
    #     target_near = is_target_near()
    #     directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    #     if target_near != (0, 0, 0, 0):
    #         m = max(target_near)
    #         indices_max = [i for i, val in enumerate(target_near) if val == m]
    #         n = rd.choice(indices_max)
    #     else:
    #         possibles = []
    #         if self.pos[1] < 49:
    #             possibles.append(0)  # Top
    #         if self.pos[1] > 0:
    #             possibles.append(1)  # Down
    #         if self.pos[0] > 0:
    #             possibles.append(2)  # Left
    #         if self.pos[0] < 49:
    #             possibles.append(3)  # Right
    #         n = rd.choice(possibles)

    #     # Application du mouvement
    #     dx, dy = directions[n]
    #     self.pos[1] += dy
    #     self.pos[0] += dx
