import pygame
from Input import Input
from Level import Level
# This class handles the clock of the game
from Clock import Clock
# This is the class to handle the score in the game
from Score import Score

pygame.init()

window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("PyMahjong version 0.2")

input = Input()
level = Level("./levels/level_1.txt")
clock = Clock(300)
score = Score()

running = True
while running:
    event = input.getEvent()
    if event == 0:
        running = False
    elif event == 1:
        if level.selectTile():
            score.increase()

    window.fill((255, 255, 255))
    clock.update()
    
    clock.render(window)
    level.render(window)
    score.render(window)
    pygame.display.flip()

pygame.quit()