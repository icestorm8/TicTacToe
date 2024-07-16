import sys

import pygame

from Logic.Player import Player
from UI.Button import Button
from UI.Text import Text


class EndScreen:
    def __init__(self, screen, player1: Player, player2: Player, game):
        self.screen = screen
        self.text = None
        self.points = None
        self.winner = None
        self.points_header = None
        self.continue_button = None
        self.restart_button = None
        self.menu_button = None
        self.game = game
        self.player1 = player1
        self.player2 = player2
        self.running = False

    def draw_elements(self, screen):
        if self.winner is None:
            self.text = Text(0, -300, screen, "THAT'S A TIE! GOOD JOB!", 60)
        else:
            self.text = Text(0, -300, screen, f"{self.winner.name} won! [{self.winner.player_char}]", 60)
        self.points_header = Text(0, -100, screen, f"{self.player1.name}[{self.player1.player_char}] | "
                                                   f"{self.player2.name}[{self.player2.player_char}]", 30)
        self.points = Text(0, -40, screen, f"{self.player1.get_points()} | {self.player2.get_points()}", 60)
        self.restart_button = Button(0, -20, 300, 70, "restart game", font_size=50)
        self.continue_button = Button(0, -100, 350, 70, "continue game", font_size=50)
        self.menu_button = Button(0, -180, 350, 70, "go to menu", font_size=50)
        self.text.draw()
        self.points_header.draw()
        self.points.draw()
        self.restart_button.draw(self.screen, True)
        self.continue_button.draw(self.screen, True)
        self.menu_button.draw(self.screen, True)

    def run(self, winner, screen):
        self.running = True
        self.winner = winner
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # occurs when x is clicked on window itself
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return "menu"
                elif event.type == pygame.MOUSEBUTTONUP:  # occurs once when the mouse button is released
                    if self.restart_button.mouseover():
                        self.running = False
                        return "restart"
                    elif self.continue_button.mouseover():
                        self.running = False
                        return "continue"
                    elif self.menu_button.mouseover():
                        return "menu"
                        # self.game.continue_game()

            screen.fill((255, 255, 255))
            self.draw_elements(screen)
            pygame.display.update()

        self.winner = winner

