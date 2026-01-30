import numpy as np
import random as rd


class Time:
    def __init__(self, second, minute, hour):
        self.second = second
        self.minute = minute
        self.hour = hour

    def add_hour(self, h):
        self.hour += h

    def add_minute(self, m):
        self.set_hour((self.minute + m)//60)
        self.minute = (self.minute + m) % 60

    def add_second(self, s):
        self.set_minute((self.second + s)//60)
        self.second = (self.second + s) % 60


class Grass:
    def __init__(self, position, age):

        self.position = position
        self.age = age
        self.compteur = 0

    def update_grass(self):

        self.compteur += 1

        if (self.compteur == 10 or self.compteur == 20) and self.age < 3:
            self.age += 1

    def grass_ate(self):

        self.compteur = 0
        self.age = 0


class World:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.world_time = Time(0, 0, 0)
        self.grasses = []
        self.generate_grass(p=0.8)
        self.wolves = []
        self.sheeps = []

    def generate_grass(self, p=0.1):
        grass_init = np.random.rand(self.grid_size, self.grid_size) < p
        grass_positions = np.argwhere(grass_init)

        for pos in grass_positions:
            self.grasses.append(Grass(pos, rd.randint(1, 2)))

    def tick(self):
        self.world_time.add_second(1)
        pass

    def display(self):

        pass
