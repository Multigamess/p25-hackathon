import numpy as np
import random as rd
from grass import Grass
from wolf import Wolf


class World:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grasses = []
        self.generate_grass(p=0.8)
        self.wolves = []
        self.sheeps = []

    def generate_grass(self, p=0.1):
        grass_init = np.random.rand(self.grid_size, self.grid_size) < p
        grass_positions = np.argwhere(grass_init)

        for pos in grass_positions:
            self.grasses.append(Grass(self, pos, rd.randint(1, 2)))

    def tick(self):
        self.world_time.add_second(1)
        pass

    def is_there_wolf(self, square):
        wolves_pos = []
        for w in self.wolves:
            wolves_pos = w.pos.append()
        if square in wolves_pos:
            return True
        else:
            return False

    def is_there_grass(self, square):
        grass_pos = []
        for g in self.grasses:
            grass_pos.append(g.position)
        if square in grass_pos:
            return True
        else:
            return False

    def is_valid_coordinates(self, pos):
        return 0 <= pos[0] and pos[0] < self.grid_size and 0 <= pos[1] and pos[1] < self.grid_size

    def display(self):

        pass
