import numpy as np
import random as rd
from grass import Grass
from wolf import Wolf
from sheep import Sheep


class World:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grasses = []
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

    def is_there_grass(self, pos):
        for g in self.grasses:
            if g.position[0] == pos[0] and g.position[1] == pos[1]:
                return True
        return False
    
    def is_there_sheep(self, pos):
        for s in self.sheeps:
            if s.position[0] == pos[0] and s.position[1] == pos[1]:
                return True
        return False

    def is_valid_coordinates(self, pos):
        return 0 <= pos[0] and pos[0] < self.grid_size and 0 <= pos[1] and pos[1] < self.grid_size

    def spawn_wolves(self, wolves_count, initial_energy):
        positions = []
        for i in range(wolves_count):
            pos = (rd.randint(
                0, self.grid_size), rd.randint(0, self.grid_size))

            while pos in positions:
                pos = (rd.randint(
                    0, self.grid_size), rd.randint(0, self.grid_size))

            positions.append(pos)

            wolf = Wolf(self, initial_energy, pos)
            self.wolves.append(wolf)

    def spawn_sheeps(self, sheeps_count, initial_energy):
        positions = []
        for i in range(sheeps_count):
            pos = (rd.randint(
                0, self.grid_size), rd.randint(0, self.grid_size))

            while pos in positions:
                pos = (rd.randint(
                    0, self.grid_size), rd.randint(0, self.grid_size))

            positions.append(pos)

            sheep = Sheep(self, initial_energy, pos)
            self.sheeps.append(sheep)
