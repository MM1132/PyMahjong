import pygame

class Score:
    def __init__(self):
        # This is the score the player has when the game begins
        self.score = 0
        # The score gets bigger by this amount with every pair
        self.step = 100
        # Create the font for displaying the socre
        self.font = pygame.font.SysFont("Verdana", 100)
    
    def increase(self):
        # Just increase the score by the amount :) 
        self.score += self.step
    
    def render(self, window):
        # Render the score onto the screen
        window.blit(self.font.render(str(self.score), 1, (0, 0, 255)), (40, 140))