import numpy as np
import random as rd


class Grass:
    def __init__(self, world, position, age, regrowth_time):
        self.world = world
        self.position = position
        self.age = age
        self.compteur = 0
        self.dead = 0
        self.regrowth_time = regrowth_time

    def die(self):
        self.compteur = 0
        self.age = 0
        self.world.grasses.remove(self)
        self.dead = 1

    def update(self):

        self.compteur += 1

        if (self.compteur == 10 or self.compteur == 20) and self.age < 3:
            self.age += 1

        if self.compteur % self.regrowth_time == 0 and rd.randint(0, 5) == 1:
            voisins = self.world.get_neighbors(self.position)
            if len(voisins) != 0:
                neighbour_selected = rd.choice(voisins)
                if not self.world.is_there_grass(neighbour_selected):
                    grass = Grass(self.world, neighbour_selected,
                                  1, self.regrowth_time)
                    self.world.grasses.append(grass)
