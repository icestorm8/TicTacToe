import sys

import pygame


from UI.Game import Game
from UI.Text import Text

SCREEN_HEIGHT, SCREEN_WIDTH = 700, 700
BACKGROUND_COLOR = (255, 255, 255)


class Menu:
    def __init__(self):
        pygame.init()  # initialize pygame
        pygame.display.set_caption('Tic Tac Toe')  # set window title
        self.screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH], pygame.RESIZABLE)  # creating a window
        self.header = Text(0, -300, self.screen, "Tic Tac Toe", 60)  # header
        self.footer = Text(0, 300, self.screen, "by shaked tamam 2024", 20)  # footer
        self.start_button = Text(0, -100, self.screen, "New Game", 70)  # start button

        running = True
        while running:
            self.screen.fill(BACKGROUND_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # occurs when x is clicked on window itself
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:  # occurs once when the mouse button is released
                    if self.start_button.mouseover():
                        print("starting")
                        Game(self.screen).run()
            clock = pygame.time.Clock()  # creating a clock for the game
            self.display_text()

            pygame.display.update()

        pygame.quit()
        sys.exit()

    def display_text(self):
        self.header.draw()
        self.footer.draw()
        self.start_button.draw()
