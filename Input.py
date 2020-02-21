import pygame

class Input:
    def __init__(self):
        pass

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return 1