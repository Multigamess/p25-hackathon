import pygame
from pygame.locals import *
import sys
import World
import numpy as np


class Game:
    def __init__(self, grid_size, square_size):
        pygame.init()
        self.square_size = square_size
        self.window = pygame.display.set_mode(
            (grid_size*square_size, grid_size*square_size))
        self.window.fill((125, 63, 24))

        self.is_running = False

        self.world = World.World(grid_size)

        for grass in self.world.grasses:
            self.set_square(grass.position, (34, 214, 9)
                            if grass.age == 1 else (32, 168, 13))

    def set_square(self, pos, color):
        s = Square(self.square_size, color)
        self.window.blit(
            s.surf, (pos[0]*self.square_size, pos[1]*self.square_size))

    def update_window(self):
        pygame.display.flip()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.game_loop()

            pygame.display.flip()

    def game_loop(self):
        print("test")
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            game.display_sheep((1, 3))
            game.display_wolf((1, 5))

    def display_sheep(self, pos):
        s = Square(self.square_size, (255, 255, 255))
        self.window.blit(
            s.surf, (pos[0]*self.square_size, pos[1]*self.square_size))

    def display_wolf(self, pos):
        s = Square(self.square_size, (255, 20, 20))
        self.window.blit(
            s.surf, (pos[0]*self.square_size, pos[1]*self.square_size))


class Square(pygame.sprite.Sprite):
    def __init__(self, size, color):
        super().__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill(color)


game = Game(40, 15)
game.run()
