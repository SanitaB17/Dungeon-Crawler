import pygame
import constants

pygame.init()

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

# main game loop
run = True
while run:

    # event handler
    for event in pygame.event.get():
        if event == pygame.quit:
            run = False


pygame.quit()
