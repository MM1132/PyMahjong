import pygame

class Input:
    def __init__(self):
        pass

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "back"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "back"
                # Shuffle
                elif event.key == pygame.K_s:
                    return 2
            # Left mouse button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return 1