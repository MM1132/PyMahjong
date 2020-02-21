import pygame

from Button import Button

class Message:
    def __init__(self, message, time, score):
        self.message = message

        self.time = time
        self.score = score

        self.font = pygame.font.SysFont("Verdana", 100)
        self.fontSmall = pygame.font.SysFont("Verdana", 50)
        self.button = Button("Next Level", "next", ["centered", 600])

    def render(self, window):
        window.fill((255, 255, 255))
        window.blit(self.font.render(self.message, 1, (20, 40, 200)), [200, 200])
        window.blit(self.fontSmall.render("Score: {}".format(self.score), 1, (0, 0, 0)), [200, 400])
        window.blit(self.fontSmall.render("Time left: {}:{:02}".format(self.time[0], self.time[1]), 1, (0, 0, 0)), [200, 460])
        self.button.render(window)

    def getInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "back"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.button.hover:
                        return self.button.returnValue