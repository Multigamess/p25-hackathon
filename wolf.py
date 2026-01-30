from random import randint as rd
from animal import Animal

dim = 50


class Wolf(Animal):

    def eat_sheep(self):
        self.energy += 10

    def move(self):

        nearest_sheep = self.get_nearest_sheep()
        if not nearest_sheep is None:
            next_move = self.get_next_move(nearest_sheep.position)
            new_pos = self.position[0] + \
                next_move[0], self.position[1]+next_move[1]
            if self.world.is_valid_coordinates(new_pos):
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
