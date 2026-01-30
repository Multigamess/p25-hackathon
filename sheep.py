import random as rd
import numpy as np
from grass.py import *

dim = 50


class Sheep:
    def __init__(self, energy, position):
        self.energy = energy
        self.pos = position
        self.age = 0
    
    def upgrade_energy(self):
        self.age += 1
        self.energy -= 1
    
    def eat_grass(self, grass):
        self.energy += grass.age * 10
        grass.ate()

    def move(self):
        h = grass()
        if h!= (0,0,0,0):
            M = h[0]
            i_max=0
            for i in range(1, 4):
                if h[i]>M:
                    M = h[i]
                    i_max = i
                elif h[i]==M:
                    i_max = rd.choice(i_max, i)
            if i_max==0:
                self.pos[1]+=1
            elif i_max==1:
                self.pos[1]-=1
            elif i_max==2:
                self.pos[0]-=1
            elif i_max==3:
                self.pos[0]+=1
            #(top, down, left, right)
            #grass[i]=-inf si hors de la map
        else :
            if self.pos[0] == 0 :
                n = rd.randint(1,3)
            elif self.pos[0] == 49 :
                n = rd.choice([0,2,3])
            elif self.pos[1] == 0 :
                n = rd.choice([0,1,3])
            elif self.pos[1] == 49 :
                n = rd.randint(0, 2)
            else :
                n = rd.randint(0, 3)
            if n==0:
                if self.pos[0]<dim-1:
                    self.pos[1]+=1
            elif n==1:
                if self.pos[0]>0:
                    self.pos[1]-=1
            elif n==2:
                if self.pos[1]>0:
                    self.pos[0]-=1
            elif n==3:
                if self.pos[1]<dim-1:
                    self.pos[0]+=1

