import pygame

class Button:
    def __init__(self, text, returnValue, pos, size = 100):
        self.text = text
        self.returnValue = returnValue
        self.pos = pos

        self.hover = False
        self.color = (200, 50, 50)

        self.font = pygame.font.SysFont("Verdana", size)
        self.fontRender = self.font.render(self.text, 1, self.color)

        # Weather the button is suppoed to be centered of not
        if type(pos[0]) == str and pos[0] == "centered":
            self.pos[0] = 1920 // 2 - self.fontRender.get_width() // 2

    def render(self, window):
        x, y = pygame.mouse.get_pos()

        if self.pos[0] + self.fontRender.get_width() > x > self.pos[0] and self.pos[1] + self.fontRender.get_height() > y > self.pos[1]:
            self.color = (0, 255, 0)
            self.hover = True
        else:
            self.color = (200, 50, 50)
            self.hover = False

        self.fontRender = self.font.render(self.text, 1, self.color)

        window.blit(self.fontRender, self.pos)