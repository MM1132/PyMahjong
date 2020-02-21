import pygame

# So we could create new tiles
from Tile import Tile

# So we could shuffle the tiles, and create tiles in different order on every launch
import random

# So we could read all the images of for the tiles from the tiles folder
from glob import glob

class Level:
    def __init__(self, file):
        self.file = file

        # Read the tiles locations from the file
        # Decide what type of tiles to create based on how many it found from the file
        # Create the random tiles as specified in the file

        # Read the file into a list
        with open(file) as f:
            # if i != "\n" tells it to skip all empty lines in the file
            # and (i+"-")[0] != "#" tells it to also skip all the lines that have "#" in front
            lines = [list(map(int, i.strip().split())) for i in f if i != "\n" and (i+"-")[0] != "#"]

        # Read all the different tile types from the tiles folder
        tileType = glob("./tiles/*")
        # Put them into a random order
        random.shuffle(tileType)
        # This will hold all the tiles names
        randomTiles = []
        # Count at which texture we are currently at
        counter = 0
        # Loop through half of the length of the tiles
        for i in range(int(len(lines) / 2)):
            # Add two tiles of the same type
            randomTiles.append(tileType[counter])
            randomTiles.append(tileType[counter])
            counter += 1
            if counter > len(tileType)-1:
                counter = 0
        # Once we got all the tiles in the list, put them all into random order
        random.shuffle(randomTiles)

        # Create the tile objects and assign random textures to them
        self.tileCount = []
        for i in range(len(lines)):
            # Tile(x, y, layer, texture)
            self.tileCount.append(Tile(lines[i][0], lines[i][1], lines[i][2], randomTiles[i]))

    def selectTile(self):
        mouse = pygame.mouse.get_pos()
        detected = []
        for i in self.tileCount:
            # If mouse is on the tile
            if i.renderX+98 > mouse[0] > i.renderX and i.renderY+130 > mouse[1] > i.renderY:
                # Add that tile to the detected tiles list
                detected.append(i)
        # If more than 0 tiles were detected
        if detected:
            # Get the highest layer of the ones that were detected
            layer = max([i.layer for i in detected])
            # Loop through all the detected tiles (all the ones that are under the mouses coordinates)
            for i in detected:
                # Find the tile that has the highest layer
                if i.layer == layer:
                    detected = i
                    break
            # Now we need to check wether the tile is selectable or not
            onTop = False
            left = False
            right = False
            # Loop through all the tiles
            for i in self.tileCount:
                # If there is a tile on top of the detected tile, then that means that our tile is blocked by it
                if i.x == detected.x and i.y == detected.y and i.layer == detected.layer + 1:
                    onTop = True
                # If there is a tile on the left of the detected tile
                elif i.x == (detected.x - 1) and i.y == (detected.y) and i.layer == (detected.layer):
                    left = True
                # If there is a tile on the right of the detected tile
                elif i.x == (detected.x + 1) and i.y == (detected.y) and i.layer == (detected.layer):
                    right = True
            # If both the sides are not blocked, or there is no other tile on top of the detected one
            if not(left and right or onTop):
                # If the tile is already selected, deselect it
                if detected.selected:
                    detected.selected = False
                # Or if the tile isn't already selected, select it
                elif not detected.selected:
                    detected.selected = True

            # SEARCH FOR MATCHES
            # Find all the tiles that are currently selected (should never be over 2)
            selected = [i for i in self.tileCount if i.selected]
            # If we have two tiles selected
            if len(selected) == 2:
                # If the two selected tiles are of the same type
                if selected[0].type == selected[1].type:
                    # Remove them both
                    self.tileCount.remove(selected[0])
                    self.tileCount.remove(selected[1])
                    if len(self.tileCount) < 1:
                        return "levelCleared"
                    return True
                # If the two selected tiles are of different types
                else:
                    # Deselect them both
                    selected[0].selected = False
                    selected[1].selected = False
            # If the number of selected tiles somehow manages to go over 2 (which should never happen tho)
            elif len(selected) > 2:
                # Deselect all the tiles
                for i in seleccted:
                    i.selected = False
    
    # Shuffle the tiles
    def shuffle(self):
        types = []
        for i in self.tileCount:
            types.append(i.type)
        random.shuffle(types)
        for i in range(len(types)):
            self.tileCount[i].setType(types[i])
    
    def render(self, window):
        for i in self.tileCount:
            i.render(window)