import pygame

pygame.init()

SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_captions("Dungeon Crawler")

#mainn game loop
run = True
while run:
    #event handler
    for event in pygame.event.get():
        if event == pygame.Quit:
            run = False
            
paygame.quit()