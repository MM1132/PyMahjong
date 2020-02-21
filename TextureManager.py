import pygame

# Load in the image and set color key to it
def loadTexture(texture, colorKey = True):
    # Just load in the image from the file and make it's blue corners transparent
    image = pygame.image.load(texture).convert()
    if colorKey:
        image.set_colorkey((0, 38, 255))
    return image

# Convert the image into darker version
def makeDark(image):
    # Create a new surface with the exact same picture
    # We cannot change the image variable itself because it is not the copy of the initial one
    dark_image = pygame.Surface((image.get_width(), image.get_height())).convert()
    dark_image.blit(image, (0, 0))

    # Create a dark surface and blit it over the image, to make it darker
    dark = pygame.Surface((image.get_width(), image.get_height()), flags = pygame.SRCALPHA)
    dark.fill((50, 50, 50, 0))
    dark_image.blit(dark, (0, 0), special_flags = pygame.BLEND_RGBA_SUB)
    # Make the black corners it created transparent
    dark_image.set_colorkey((0, 0, 0))
    return dark_image