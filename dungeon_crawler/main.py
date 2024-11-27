import pygame
import constants
from character import Character

pygame.init()

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

# create player
player = Character(100, 100)

# main game loop
run = True
while run:
    
    # draw player on screen
    player.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event == pygame.quit:
            run = False
    
    pygame.display.update()


pygame.quit()
