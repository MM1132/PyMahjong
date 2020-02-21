import pygame
from TextureManager import loadTexture
from TextureManager import makeDark

class Tile:
    def __init__(self, x, y, layer, texture):
        # Tiles position
        self.x = x
        self.y = y
        self.layer = layer
        
        # Wether the tile is selected or not
        self.selected = False
        
        # We are using the name of the tiles texture image name as it's type
        self.type = texture
        
        # Load in the image of the tile
        self.texture = loadTexture(texture)
        # Also generate a darker version of the tiles image, this will be used when the tile is selected
        self.texture_dark = makeDark(self.texture)
        
        # Calculate the coordinates that the tile will be rendered at
        self.renderX = self.x * 98 - (self.layer * 17) + 455
        self.renderY = self.y * 130 - (self.layer * 17) + 85

    # This function is used for changing the tiles type when shuffling
    def setType(self, type):
        self.type = type
        self.texture = loadTexture(type)
        self.texture_dark = makeDark(self.texture)

    def updateRenderCoordinates(self):
        self.renderX = self.x * 98 - (self.layer * 17) + 455
        self.renderY = self.y * 130 - (self.layer * 17) + 77
    
    def render(self, window):
        # Render the tile onto the screen at the calculated coordiantes
        window.blit(self.texture, (self.renderX, self.renderY))
        # If the tile happens to be selected, use the darker version of the image to indicate that
        if self.selected:
            window.blit(self.texture_dark, (self.renderX, self.renderY))