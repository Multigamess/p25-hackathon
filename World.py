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

    def display(self):

        pass
