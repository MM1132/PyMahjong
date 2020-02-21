import pygame

from glob import glob
from Button import Button

class Selector:
    def __init__(self):
        levels = glob("./levels/*.txt")

        self.levelCount = []
        for i in range(len(levels)):
            self.levelCount.append(Button(levels[i][9:16], levels[i], ["centered", 80*i + 200], 60))

    def render(self, window):
        for i in self.levelCount:
            i.render(window)