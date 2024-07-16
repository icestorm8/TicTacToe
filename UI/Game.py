import sys

import pygame
from pygame import Vector2

from Logic.Board import Board
from Logic.Player import Player


class Game:
    def __init__(self, screen):
        self.board_arr = Board()
        self.block_size = int(screen.get_width()/3)
        # player 1 = X
        self.player1 = Player("X", "player1")
        self.x_frames = [pygame.image.load(f'Assets/X_frames/x_{i}.png') for i in range(0, 9)]
        self.static_x = pygame.image.load("Assets/X_frames/x_8.png")
        self.static_x = pygame.transform.scale(self.static_x, (self.block_size, self.block_size))

        # resized_image = pygame.transform.scale(image, (new_width, new_height))
        # player 2 = O
        self.player2 = Player("O", "player2")
        self.o_frames = [pygame.image.load(f'Assets/O_frames/o_{i}.png') for i in range(0, 11)]
        self.static_o = pygame.image.load("Assets/O_frames/o_10.png")
        self.static_o = pygame.transform.scale(self.static_o, (self.block_size, self.block_size))

        self.current_player = self.player1

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
                    cell_position = event.position
                    row, col = cell_position
                    # if move was successful - draw the move and switch players
                    # else - draw the error and stay with the same player
                    if self.board_arr.do_move(self.current_player, row, col):
                        self.draw_player(self.current_player, row, col)
                        self.switch_player()
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
        # block_size = int(self.screen.get_width()/3)  # Set the size of the grid block
        for x in range(0, 3):
            for y in range(0, 3):
                rect = pygame.Rect(x*self.block_size, y*self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 5)
                # row_index = x // block_size
                # col_index = y // block_size
                # print(f"[{x}, {y}]")
                self.rects[x][y] = rect

    def check_collision(self):
        pos = pygame.mouse.get_pos()
        for row in range(0, 3):
            for col in range(0, 3):
                if self.rects[row][col] is not None:
                    if self.rects[row][col].collidepoint(pos):
                        custom_event = pygame.event.Event(self.GRID_CLICKED, position=(row, col))
                        pygame.event.post(custom_event)

    def draw_player(self, player: Player, row, col):
        print(player.name)
        if player == self.player1:
            print()
            # Blit the image onto the specified rectangle
            self.screen.blit(self.static_x, self.rects[row][col])
        else:
            print()
            self.screen.blit(self.static_o, self.rects[row][col])

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
