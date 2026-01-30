from random import randint as rd
from animal import Animal

dim = 50

class Wolf(Animal) :
    
    def eat_sheep(self):
        self.energy += 10
    
    def move_wolf(self):
        super().move('sheep')