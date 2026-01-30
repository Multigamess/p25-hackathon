import pygame
from pygame.locals import *
import sys
import numpy as np
from wolf import Wolf
from sheep import Sheep
from world import World


class Game:
    def __init__(self, grid_size, square_size):
        pygame.init()
        self.square_size = square_size
        self.window = pygame.display.set_mode(
            (grid_size*square_size, grid_size*square_size))

        self.is_running = False

        self.world = World(grid_size)

        self.draw_terrain()
        self.update_sheeps()
        self.update_wolves()
        pygame.display.flip()

    def set_square(self, pos, color):
        s = Square(self.square_size, color)
        self.window.blit(
            s.surf, (pos[0]*self.square_size, pos[1]*self.square_size))

    def update_window(self):
        pygame.display.flip()

    def run(self):
        self.is_running = True
        while self.is_running:
            pygame.time.delay(1000)

            self.game_loop()

            pygame.display.flip()

    def draw_terrain(self):
        self.window.fill((125, 63, 24))

        for grass in self.world.grasses:
            self.set_square(grass.position, (34, 214, 9)
                            if grass.age == 1 else (32, 168, 13))

    def game_loop(self):
        print("test")
        # quit window
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.update_grasses()
        self.draw_terrain()

        self.update_sheeps()
        self.update_wolves()

    def update_grasses(self):
        for grass in self.world.grasses:
            grass.update()

    def update_sheeps(self):
        for sheep in self.world.sheeps:
            sheep.move()
            self.draw_sheep(sheep.position)

    def update_wolves(self):
        for wolf in self.world.wolves:
            wolf.move()
            print(wolf.position)
            self.draw_wolf(wolf.position)

    def draw_sheep(self, pos):
        s = Square(self.square_size, (255, 255, 255))
        self.window.blit(
            s.surf, (pos[0]*self.square_size, pos[1]*self.square_size))
        return s

    def draw_wolf(self, pos):
        s = Square(self.square_size, (255, 20, 20))
        self.window.blit(
            s.surf, (pos[0]*self.square_size, pos[1]*self.square_size))
        return s


class Square(pygame.sprite.Sprite):
    def __init__(self, size, color):
        super().__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill(color)


game = Game(40, 16)
world = game.world
world.wolves.append(Wolf(world, 1, (0, 0)))
world.sheeps.append(Sheep(world, 1, (39, 39)))
game.run()
