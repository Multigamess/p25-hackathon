import numpy as np
import random as rd
from grass import Grass
from wolf import Wolf
from sheep import Sheep
import gameconfig as config


class World:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.water = []
        self.grasses = []
        self.wolves = []
        self.sheeps = []

    def generate_grass(self, p=0.1, regrowth_time=7):
        grass_init = np.random.rand(self.grid_size, self.grid_size) < p
        grass_positions = np.argwhere(grass_init)

        for pos in grass_positions:
            x, y = pos[0], pos[1]
            if (x, y) not in self.water:
                self.grasses.append(
                    Grass(self, (x, y), rd.randint(1, 2), regrowth_time))

    def tick(self):
        self.world_time.add_second(1)
        pass

<<<<<<< HEAD
=======
    def is_there_wolf(self, square):
        wolves_pos = []
        for w in self.wolves:
            wolves_pos.append(w.position)
        if square in wolves_pos:
            return True
        else:
            return False

>>>>>>> 78e0b63c650f64931a3747186ea0513ae5b6c836
    def get_neighbors(self, pos):
        to_check = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []
        for v in to_check:
            x, y = pos[0] + v[0], pos[1] + v[1]
            if self.is_valid_coordinates((x, y)):
                neighbors.append((x, y))
        return neighbors

    def has_grass(self, pos):
        for g in self.grasses:
            if g.position[0] == pos[0] and g.position[1] == pos[1]:
                return True
        return False

    def has_wolf(self, pos):
        for w in self.wolves:
            if w.position[0] == pos[0] and w.position[1] == pos[1]:
                return True
        return False

    def has_sheep(self, pos):
        for s in self.sheeps:
            if s.position[0] == pos[0] and s.position[1] == pos[1]:
                return True
        return False

    def has_water(self, pos):
        return pos in self.water

    def is_valid_coordinates(self, pos):
        return 0 <= pos[0] and pos[0] < self.grid_size and 0 <= pos[1] and pos[1] < self.grid_size

    def spawn_wolves(self, wolves_count):
        positions = []
        for i in range(wolves_count):
            pos = (rd.randint(
                0, self.grid_size-1), rd.randint(0, self.grid_size-1))

            while pos in positions or pos in self.water:
                pos = (rd.randint(
                    0, self.grid_size-1), rd.randint(0, self.grid_size-1))

            positions.append(pos)

            wolf = Wolf(self, config.WOLF_INITIAL_ENERGY,
                        pos, config.WOLF_ENERGY_LOSS_PER_TURN)
            self.wolves.append(wolf)

    def spawn_sheeps(self, sheeps_count):
        positions = []
        for i in range(sheeps_count):
            pos = (rd.randint(
                0, self.grid_size-1), rd.randint(0, self.grid_size-1))

            while pos in positions or pos in self.water:
                pos = (rd.randint(
                    0, self.grid_size-1), rd.randint(0, self.grid_size-1))

            positions.append(pos)

            sheep = Sheep(self, config.SHEEP_INITIAL_ENERGY,
                          pos, config.SHEEP_ENERGY_LOSS_PER_TURN)
            self.sheeps.append(sheep)

    def get_wolf_heatmap(self):
        heatmap = np.zeros((config.GRID_SIZE, config.GRID_SIZE))
        for wolf in self.wolves:
            neighbors = self.get_neighbors(wolf.position)
            heatmap[wolf.position[0], wolf.position[1]] = 1
            for neigh in neighbors:
                heatmap[neigh[0], neigh[1]] = 0.5
        return heatmap

    def add_lake(self, max_size, x, y):
        size = 0
        lake = []
        to_check = [(x, y)]
        while len(to_check) > 0 and size < max_size:
            pos = rd.choice(to_check)

            if pos not in lake:
                lake.append(pos)
                self.water.append(pos)
                size += 1
                neighbors = self.get_neighbors(pos)
                to_check.extend(neighbors)

    def get_random_coordinates(self):
        return (rd.randint(0, self.grid_size-1), rd.randint(0, self.grid_size-1))
