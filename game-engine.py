import pygame
from pygame.locals import *
import sys
import numpy as np
from wolf import Wolf
from sheep import Sheep
from world import World

GRID_SIZE = 40
PIXEL_SIZE = 16
INITIAL_SHEEPS = 50
INITIAL_WOLVES = 10
INITIAL_GRASS_COVERAGE = 0.3

SHEEP_INITIAL_ENERGY = 20
WOLF_INITIAL_ENERGY = 40


class Game:
    def __init__(self):
        pygame.init()
        self.tick = 0
        self.square_size = PIXEL_SIZE
        self.window = pygame.display.set_mode(
            (GRID_SIZE*PIXEL_SIZE, GRID_SIZE*PIXEL_SIZE))

        self.is_running = False

        self.world = World(GRID_SIZE)
        self.world.generate_grass(INITIAL_GRASS_COVERAGE)

        self.draw_terrain()
        self.update_sheeps()
        self.update_wolves()
        pygame.display.flip()

    def display_hud(self):
        font = pygame.font.Font(None, 32)
        wolf_text = font.render(
            f'Wolves {len(self.world.wolves)}', True, (0, 0, 255), (0, 0, 0))
        sheep_text = font.render(
            f'Sheeps {len(self.world.sheeps)}', True, (0, 0, 255), (0, 0, 0))
        grass_text = font.render(
            f'Grass {len(self.world.grasses)}', True, (0, 0, 255), (0, 0, 0))

        wolf_rect = wolf_text.get_rect()
        wolf_rect.center = (56, 16)
        self.window.blit(wolf_text, wolf_rect)

        sheep_rect = sheep_text.get_rect()
        sheep_rect.center = (56, 56)
        self.window.blit(sheep_text, sheep_rect)

        grass_rect = grass_text.get_rect()
        grass_rect.center = (56, 96)
        self.window.blit(grass_text, grass_rect)

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
            pygame.time.delay(1000)

    def draw_terrain(self):
        self.window.fill((125, 63, 24))

        for grass in self.world.grasses:
            self.set_square(grass.position, (34, 214, 9)
                            if grass.age == 1 else (32, 168, 13))

    def game_loop(self):
        self.tick += 1

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

        self.display_hud()

    def update_grasses(self):
        for grass in self.world.grasses:
            grass.update()

    def update_sheeps(self):
        for sheep in self.world.sheeps:
            if self.tick % 2 == 0:
                sheep.update()
            self.draw_sheep(sheep.position)

    def update_wolves(self):
        for wolf in self.world.wolves:
            wolf.update()
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


game = Game()
world = game.world
world.spawn_wolves(INITIAL_WOLVES, WOLF_INITIAL_ENERGY)
world.spawn_sheeps(INITIAL_SHEEPS, SHEEP_INITIAL_ENERGY)
# world.wolves.append(Wolf(world, 1, (0, 0)))
# world.sheeps.append(Sheep(world, 1, (30, 30)))
game.run()
