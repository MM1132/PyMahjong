import pygame

from Button import Button
from Selector import Selector

class Menu:
    def __init__(self):
        self.state = 0

        self.elements = {
            0: [Button("Start Game", 1, ["centered", 300]), Button("Quit", "quit", ["centered", 450])],
            1: [Button("Step By Step", "any", ["centered", 300]), Button("Any Level", 2, ["centered", 450]), Button("Back", 0, ["centered", 600])],
            2: [Selector(), Button("Back", 1, ["centered", 800])]
        }

    def render(self, window):
        window.fill((255, 255, 255))
        for i in self.elements[self.state]:
            i.render(window)

    def getInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in self.elements[self.state]:
                        if type(i) == Button:
                            if i.hover:
                                if type(i.returnValue) == str:
                                    if i.returnValue == "quit":
                                        return i.returnValue
                                    else:
                                        # STEP
                                        return "step"
                                elif type(i.returnValue) == int:
                                    self.state = i.returnValue
                        elif type(i) == Selector:
                            for j in i.levelCount:
                                if j.hover:
                                    # ANY
                                    return j.returnValue