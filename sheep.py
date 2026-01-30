import random as rd
import numpy as np
from grass import *
from animal import Animal


class Sheep(Animal):

    def eat_grass(self, grass_position):
        for g in self.world.grasses:
            if g.position[0] == grass_position[0] and g.position[1] == grass_position[1]:
                grass = g
        self.energy += grass.age * 10
        grass.die()

    def reproduce(self):
        pass
    
    def move(self):
        neighbors = self.get_neighbors()
        target = rd.choice(neighbors)

        next_move = self.get_next_move(target)
        print("next_move", next_move)
        new_pos = self.position[0] + \
            next_move[0], self.position[1]+next_move[1]
        if self.world.is_valid_coordinates(new_pos):
            self.position = new_pos

    def get_neighbors(self):
        to_check = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []
        for v in to_check:
            x, y = self.position[0] + v[0], self.position[1] + v[1]
            if self.world.is_valid_coordinates((x, y)):
                neighbors.append((x, y))
        return neighbors
    
    def update(self):
        self.move()
        self.upgrade_energy()

        if self.world.is_there_grass(self.position):
            self.eat_grass(self.position)
            print(f'Grass in {self.position} eaten')
        
        if self.energy < 0:
            self.die()

    def die(self):
        self.compteur = 0
        self.age = 0
        self.world.sheeps.remove(self)
