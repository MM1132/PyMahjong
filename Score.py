import pygame

# This will allow us to determine the streak the user is having
from time import time

class Score:
    def __init__(self):
        # The multiplier for score
        self.streak = 1
        # This font will be used to show the player the streak they are in
        self.streakFont = pygame.font.SysFont("Verdana", 100)
        
        # This will remember the last time a pair was matched
        self.pairTime = 0
        # How much time does the player have to score a streak (seconds)
        self.strikeTime = 1.5
        
        # This is the score the player has when the game begins
        self.score = 0
        # The score gets bigger by this amount with every pair
        self.step = 50
        # Create the font for displaying the socre
        self.font = pygame.font.SysFont("Verdana", 100)
    
    def increase(self):
        if time() - self.pairTime < self.strikeTime:
            self.streak += 1
        
        self.pairTime = time()
        
        # Just increase the score by the amount :) 
        self.score += self.step * self.streak

    def decrease(self, amount):
        self.score -= amount

    def update(self):
        if time() - self.pairTime >= self.strikeTime:
            # Set the streak back to it's default value
            self.streak = 1
    
    def render(self, window):
        # Render the score onto the screen
        window.blit(self.font.render(str(self.score), 1, (0, 0, 255)), (40, 140))
        
        # Render the streak the player is having
        window.blit(self.font.render(str(self.streak), 1, (0, 0, 255)), (40, 260))