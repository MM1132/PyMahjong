import pygame
from Input import Input
from Level import Level
# This class handles the clock of the game
from Clock import Clock
# This is the class to handle the score in the game
from Score import Score

from Menu import Menu

# To give the player information after they have finished a level
from Message import Message

# To find the list of all levels
from glob import glob

pygame.init()

window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("PyMahjong version 0.2")

input = Input()
clock = Clock(180)
score = Score()
levelList = []

menu = Menu()
level = None
gameType = None
message = None

def menu_state():
    global levelList
    event = menu.getInput()
    if event == "quit":
        return "quit"
    elif type(event) == str and event[-4:] == ".txt":
        levelList = []
        levelList.append(event)
        return event
    elif event == "step":
        levelList = glob("./levels/*")
        return levelList[0]
    menu.render(window)

def level_state():
    event = input.getEvent()
    if event == "back":
        return event
    elif event == 1:
        pairAndDone = level.selectTile()
        if pairAndDone == "levelCleared":
            score.increase()
            return "levelCleared"
        elif pairAndDone == True:
            score.increase()
    # When S is pressed, shuffle the tiles
    elif event == 2:
        if score.score >= 1000:
            level.shuffle()
            score.decrease(1000)

    window.fill((255, 255, 255))

    # The timer of the score... wether to get more points or not
    score.update()

    # If the time has ran out, close the game
    if clock.update() == False:
        running = False

    clock.render(window)
    level.render(window)
    score.render(window)

def message_state():
    event = message.getInput()
    message.render(window)
    if event == "quit":
        return event
    elif event == "back":
        return event
    elif event == "next":
        return event



game_state = menu_state
running = True

while running:
    event = game_state()
    if event == "quit":
        running = False
    elif event == "back":
        level = input = clock = score = None
        menu = Menu()
        game_state = menu_state
    elif event and event[-4:] == ".txt":
        level = Level(event)
        input = Input()
        clock = Clock(180)
        score = Score()
        menu = None
        game_state = level_state
    elif event == "levelCleared":
        message = Message(level.file[-11:-4] + " completed!", [clock.minutes, clock.seconds], score.score)
        game_state = message_state
        input = clock = menu = None
    elif event == "next":
        if len(levelList) > 1:
            levelList.remove(level.file)
            level = Level(levelList[0])
            input = Input()
            clock = Clock(180)
            game_state = level_state
        else:
            level = input = clock = score = None
            menu = Menu()
            game_state = menu_state
            levelList = []

    pygame.display.flip()

pygame.quit()