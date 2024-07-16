import sys

import pygame
from pygame import Vector2

from Logic.Board import Board
from Logic.Player import Player


class Game:
    def __init__(self, screen):
        self.board_arr = Board()
        self.player1 = Player("X", "player1")
        self.player2 = Player("O", "player2")
        self.screen = screen
        self.running = True
        self.rects: [[pygame.rect]] = [[None, None, None], [None, None, None], [None, None, None]]
        self.GRID_CLICKED = pygame.USEREVENT + 1
        # self.end_screen = EndScreen(self.screen)
        while self.running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.check_collision()
                if event.type == self.GRID_CLICKED:
                    print(event.position)


                # if event.type == self.GAME_OVER:
                #     print("game is over!!!")
                #     self.running = False

            # Fill the background
            self.draw_grid()
            # self.screen.fill((0, 0, 0))
            pygame.display.update()
        # Done! Time to quit.
        # self.end_screen.run(self)

    def draw_grid(self):
        block_size = int(self.screen.get_width()/3)  # Set the size of the grid block
        for x in range(0, 3):
            for y in range(0, 3):
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 5)
                # row_index = x // block_size
                # col_index = y // block_size
                # print(f"[{x}, {y}]")
                self.rects[x][y] = rect

    def check_collision(self):
        pos = pygame.mouse.get_pos()
        for row in range(0, 3):
            for col in range(0, 3):
                if self.rects[row][col].collidepoint(pos):
                    custom_event = pygame.event.Event(self.GRID_CLICKED, position=(col, row))
                    pygame.event.post(custom_event)



