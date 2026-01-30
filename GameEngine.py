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
        self.window.fill((0, 255, 0))

        self.is_running = False

        self.world = World.World(grid_size)

        for pos, value in np.ndenumerate(self.world.heightmap):
            self.set_square(pos, (0, int(value * 255), 0))

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


class Square(pygame.sprite.Sprite):
    def __init__(self, size, color):
        super().__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill(color)


game = Game(40, 15)
game.run()
