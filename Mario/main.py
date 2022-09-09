# Super Mario
import pygame, sys
from settings import *
from level import Level
from game_data import level_1

# Setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_1, screen)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("grey")
    # Store all game logic
    level.run()

    pygame.display.update()
    clock.tick(60)
