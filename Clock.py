import pygame

from time import time

class Clock:
    def __init__(self, totalTime):
        # The second that we started the game at
        self.startTime = time()
        # The time in total
        self.totalTime = totalTime
        # How many minutes til the end
        self.minutes = int(totalTime / 60)
        # How many seconds til the end
        self.seconds = int(self.totalTime - self.minutes * 60)
        
        # Create the font for displaying the time
        self.font = pygame.font.SysFont("Verdana", 100)
    
    def update(self):
        # timeLeft is the seconds til the end
        timeLeft = self.totalTime - (time() - self.startTime)
        
        # If the time has ran out
        if timeLeft < 0:
            return False
        
        # We get the sort it nicely into minutes and seconds so it is easy to display it
        self.minutes = int(timeLeft / 60)
        self.seconds = int(timeLeft - self.minutes * 60)
    
    def render(self, window):
        # Render the minutes:seconds onto the screen
        window.blit(self.font.render("{}:{:02}".format(self.minutes, self.seconds), 1, (0, 0, 255)), (40, 20))