import pygame
from pygame.locals import *
import sys
import numpy as np
from wolf import Wolf
from sheep import Sheep
from world import World
import gameconfig as config


class Game:
    def __init__(self):
        pygame.init()
        self.tick = 0
        self.square_size = config.PIXEL_SIZE
        self.window = pygame.display.set_mode(
            (config.GRID_SIZE*config.PIXEL_SIZE, config.GRID_SIZE*config.PIXEL_SIZE))

        self.is_running = False

        self.world = World(config.GRID_SIZE)

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
            pygame.time.delay(500)

    def draw_terrain(self):
        self.window.fill((125, 63, 24))

        for water_pos in self.world.water:
            self.set_square(water_pos, (0, 0, 255))

        for grass in self.world.grasses:
            self.set_square(grass.position, (34, 214, 9)
                            if grass.age == 1 else (32, 168, 13))

    def game_loop(self):
        self.tick += 1

        print("Tick")
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
lake_coord1 = world.get_random_coordinates()
world.add_lake(25, lake_coord1[0], lake_coord1[1])
lake_coord2 = world.get_random_coordinates()
world.add_lake(40, lake_coord2[0], lake_coord2[1])
world.generate_grass(
    config.INITIAL_GRASS_COVERAGE, config.GRASS_REGROWTH_TIME)
world.spawn_wolves(config.INITIAL_WOLVES)
world.spawn_sheeps(config.INITIAL_SHEEPS)
# world.wolves.append(Wolf(world, 1, (0, 0)))
# world.sheeps.append(Sheep(world, 1, (30, 30)))
game.run()
