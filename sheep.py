import random as rd
import numpy as np
from grass import *
from animal import Animal

dim = 50


class Sheep(Animal):

    def eat_grass(self, grass):
        self.energy += grass.age * 10
        grass.ate()

    def move_wolf(self):
        super().move('grass')
    
    def sheep_ate(self):
        pass
