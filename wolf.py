import random as rd
from animal import Animal
import gameconfig as config
import numpy as np


class Wolf(Animal):

    def eat_sheep(self):
        self.energy += 10
        for s in self.world.sheeps:
            if s.position[0] == self.position[0] and s.position[1] == self.position[1]:
                sheep = s
        self.energy += sheep.age * 10
        sheep.die()

    def reproduce(self):
        if self.energy > 80:
            neighbours_valid = []
            for square in self.world.get_neighbors(self.position):
                if not (self.world.has_wolf(square)):
                    neighbours_valid.append(square)
            if len(neighbours_valid) > 0:
                pos = rd.choice(neighbours_valid)
                child = Wolf(self.world, config.WOLF_INITIAL_ENERGY,
                             pos, config.WOLF_ENERGY_LOSS_PER_TURN)
                self.world.wolves.append(child)
                self.energy -= 20

    def get_next_move(self, target):
        dx = target[0] - self.position[0]
        dy = target[1] - self.position[1]
        print('dx dy', dx, ' ', dy)

        if abs(dx) + abs(dy) == 0:
            return (0, 0)

        # probability to go in x direction
        p = abs(dx)/(abs(dx) + abs(dy))
        if np.random.rand() < p:
            sign = int(np.sign(dx))
            return (sign, 0)
        else:
            sign = int(np.sign(dy))
            return (0, sign)

    def move(self):

        nearest_sheep = self.get_nearest_sheep()
        target = nearest_sheep.position if not nearest_sheep is None else rd.choice(
            self.world.get_neighbors(self.position))
        next_move = self.get_next_move(target)

        new_pos = self.position[0] + \
            next_move[0], self.position[1]+next_move[1]
        if self.world.is_valid_coordinates(new_pos) and not (self.world.has_wolf(new_pos)) and not (self.world.has_water(new_pos)):
            self.position = new_pos

    def get_nearest_sheep(self):
        min_distance = float('inf')
        nearest = None
        for s in self.world.sheeps:
            dx = abs(s.position[0] - self.position[0])
            dy = abs(s.position[1] - self.position[1])
            if dx + dy < min_distance:
                min_distance = dx + dy
                nearest = s
        return nearest

    def die(self):
        self.tick = 0
        self.age = 0
        self.world.wolves.remove(self)

    def update(self):
        self.tick += 1
        self.move()

        if self.world.has_sheep(self.position):
            self.eat_sheep()

        self.reproduce()

        self.upgrade_energy(config.WOLF_ENERGY_LOSS_PER_TURN)

        if self.energy < 0:
            self.die()
