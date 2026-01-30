import numpy as np
import random as rd


class Grass:
    def __init__(self, world, position, age):
        self.world = world
        self.position = position
        self.age = age
        self.compteur = 0
        self.dead = 0

    def die(self):
        self.compteur = 0
        self.age = 0
        self.world.grasses.remove(self)
        self.dead = 1

    def get_neighbors(self):
        voisin = []
        if self.world.is_valid_coordinates((self.position[0]-1, self.position[1])) and not(self.world.is_there_grass((self.position[0]-1, self.position[1]))):
            voisin.append((self.position[0]-1, self.position[1]))
        if self.world.is_valid_coordinates((self.position[0]+1, self.position[1])) and not(self.world.is_there_grass((self.position[0]+1, self.position[1]))):
            voisin.append((self.position[0]+1, self.position[1]))
        if self.world.is_valid_coordinates((self.position[0], self.position[1]-1)) and not(self.world.is_there_grass((self.position[0], self.position[1]-1))):
            voisin.append((self.position[0], self.position[1]-1))
        if self.world.is_valid_coordinates((self.position[0], self.position[1]+1)) and not(self.world.is_there_grass((self.position[0], self.position[1]+1))):
            voisin.append((self.position[0], self.position[1]+1))
        return voisin

    def update(self):

        self.compteur += 1

        if (self.compteur == 10 or self.compteur == 20) and self.age < 3:
            self.age += 1

        if self.compteur%20 == 0:
            voisins = self.get_neighbors()
            if len(voisins)!=0:
                neighbour_selected = rd.choice(voisins)
                grass = Grass(self.world, neighbour_selected, 1)
                self.world.grasses.append(grass)

