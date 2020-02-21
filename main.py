import pygame
from Input import Input
from Level import Level
pygame.init()

window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

input = Input()
level = Level("./levels/level_1.txt")

running = True
while running:
    event = input.getEvent()
    if event == 0:
        running = False
    elif event == 1:
        level.selectTile()

    window.fill((255, 255, 255))
    level.render(window)
    pygame.display.flip()

pygame.quit()