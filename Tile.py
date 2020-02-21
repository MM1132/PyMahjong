import pygame
from TextureManager import loadTexture
from TextureManager import makeDark

class Tile:
    def __init__(self, x, y, layer, texture):
        self.x = x
        self.y = y
        self.layer = layer
        self.selected = False
        self.type = texture
        self.texture = loadTexture(texture)
        self.texture_dark = makeDark(self.texture)
        self.mask = pygame.mask.from_surface(self.texture)
        self.renderX = self.x * 98 - (self.layer * 17) + 455
        self.renderY = self.y * 130 - (self.layer * 17) + 77

    def render(self, window):
        window.blit(self.texture, (self.renderX, self.renderY))
        if self.selected:
            window.blit(self.texture_dark, (self.renderX, self.renderY))
            # pygame.draw.rect(window, (0, 0, 0), (self.renderX+30, self.renderY+30, 30, 30))