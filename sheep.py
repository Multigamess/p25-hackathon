import random as rd
import numpy as np
from grass import *
from animal import Animal
import gameconfig as config


class Sheep(Animal):

    def eat_grass(self, grass_position):
        for g in self.world.grasses:
            if g.position[0] == grass_position[0] and g.position[1] == grass_position[1]:
                grass = g
        self.energy += grass.age * 10
        grass.die()

    def reproduce(self):
        if self.energy > 50:
            pos = rd.choice(self.world.get_neighbors(self.position))
            child = Sheep(self.world, config.SHEEP_INITIAL_ENERGY,
                          pos, config.SHEEP_ENERGY_LOSS_PER_TURN)
            self.world.sheeps.append(child)
            self.energy -= 20

    def move(self):
        neighbors = self.world.get_neighbors(self.position)
        target = rd.choice(neighbors)

        next_move = self.get_next_move(target)

        new_pos = self.position[0] + \
            next_move[0], self.position[1]+next_move[1]
        if self.world.is_valid_coordinates(new_pos) and not (self.world.is_there_sheep(new_pos)):
            self.position = new_pos

    def update(self):
        self.move()

        if self.world.is_there_grass(self.position):
            self.eat_grass(self.position)

        self.upgrade_energy(5)

        self.reproduce()

        if self.energy < 0:
            self.die()

    def die(self):
        self.tick = 0
        self.age = 0
        self.world.sheeps.remove(self)
