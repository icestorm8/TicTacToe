import sys

import pygame
from pygame import Vector2

from Logic.Board import Board
from Logic.Player import Player
from UI.EndScreen import EndScreen


class Game:
    def __init__(self, screen, player1: Player = Player("X", "player1"), player2: Player = Player("O", "player2")):
        self.board_arr = Board()
        self.block_size = int(screen.get_width() / 3)
        # players:
        # player 1 = X
        self.player1 = player1
        self.x_frames = [pygame.image.load(f'Assets/X_frames/x_{i}.png') for i in range(0, 9)]
        self.static_x = pygame.image.load("Assets/X_frames/x_8.png")
        self.static_x = pygame.transform.scale(self.static_x, (self.block_size, self.block_size))

        # player 2 = O
        self.player2 = player2
        self.o_frames = [pygame.image.load(f'Assets/O_frames/o_{i}.png') for i in range(0, 11)]
        self.static_o = pygame.image.load("Assets/O_frames/o_10.png")
        self.static_o = pygame.transform.scale(self.static_o, (self.block_size, self.block_size))

        # sounds
        self.good_move = pygame.mixer.Sound("Assets/Sounds/good.mp3")
        self.bad_move = pygame.mixer.Sound("Assets/Sounds/bad.mp3")

        # grids
        self.rects: [[pygame.rect]] = [[None, None, None], [None, None, None], [None, None, None]]
        self.animation_grid = [[{'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0}],
                               [{'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0}],
                               [{'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0}]]

        # custom events
        self.GRID_CLICKED = pygame.USEREVENT + 1
        self.GAME_OVER = pygame.USEREVENT + 2
        self.UPDATE_ANIMATION = pygame.USEREVENT + 3

        # screens & settings
        self.current_player = self.player1
        self.screen = screen
        self.endScreen = EndScreen(self.screen, self.player1, self.player2, self)
        self.game_over = False
        self.winner = None

        self.screen.fill((255, 255, 255))

    def run(self):
        self.current_player = self.player1
        while not self.game_over:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_over = True
                        return
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.check_collision()
                elif event.type == self.GRID_CLICKED:
                    cell_position = event.position
                    row, col = cell_position
                    # if move was successful - draw the move and switch players
                    # else - draw the error and stay with the same player
                    if self.board_arr.do_move(self.current_player, row, col):
                        self.good_move.play()
                        self.draw_player(self.current_player, row, col)
                        self.switch_player()
                    else:
                        self.bad_move.play()
                elif event.type == self.UPDATE_ANIMATION:
                    self.update_animations()
                elif event.type == self.GAME_OVER:
                    self.winner = event.winner
                    if self.winner is self.player1:
                        print(f"{self.player1.name} won")
                        self.player1.add_point()
                    elif self.winner is self.player2:
                        print(f"{self.player2.name} won")
                        self.player2.add_point()
                    else:
                        print("this was a tie! good job!")
                    self.game_over = True

            self.check_board()
            self.draw_grid()
            pygame.display.update()

        # Done! Time to quit.
        action: str = self.endScreen.run(self.winner, self.screen)
        print(action == "continue")
        self.screen.fill((255, 255, 255))
        if action == "continue":
            self.continue_game()
        elif action == "restart":
            self.restart_game()
        else:
            return
        self.run()


    # # this is used to restart the whole game, including the points (player names will stay the same and to change those
    # # user must go to menu
    def restart_game(self):
        self.continue_game()
        self.player1.restart()
        self.player2.restart()

    # # the winner gets a point each round so continue is to keep playing
    def continue_game(self):
        self.board_arr = Board()
        self.game_over = False
        self.rects: [[pygame.rect]] = [[None, None, None], [None, None, None], [None, None, None]]
        self.animation_grid = [[{'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0}],
                               [{'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0}],
                               [{'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0},
                                {'animation': None, 'active': False, 'frame_index': 0}]]
        pygame.time.set_timer(self.UPDATE_ANIMATION, 0)



    def check_board(self):
        winner = self.board_arr.has_winner(self.player1, self.player2)
        if winner is not None and not self.board_arr.is_full():
            custom_event = pygame.event.Event(self.GAME_OVER, winner=winner)
            pygame.event.post(custom_event)
        elif winner is None and self.board_arr.is_full():
            custom_event = pygame.event.Event(self.GAME_OVER, winner=None)
            pygame.event.post(custom_event)
        else:
            return

    def draw_grid(self):
        # block_size = int(self.screen.get_width()/3)  # Set the size of the grid block
        for x in range(0, 3):
            for y in range(0, 3):
                rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
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

    # this function updates all animations available. it uses the animation grid that tracks which animation is on and
    # if its active. this is happening according to the cell and row the user clicked on.
    # the animation checking is an event that happens any given time, posted by the draw_player method, that starts the
    # timer. this is so that each animation would start after the move has been done, and will stop after one loop,
    # living the sign static.
    def update_animations(self):
        for row in range(0, len(self.animation_grid)):
            for col in range(0, len(self.animation_grid[row])):
                cell = self.animation_grid[row][col]
                if cell['animation'] is not None:
                    # print(len(cell['animation']))

                    if cell['active']:
                        scaled_image = pygame.transform.scale(cell['animation'][cell['frame_index']],
                                                              (self.block_size, self.block_size))
                        self.screen.blit(scaled_image,
                                         (self.rects[row][col]))
                        print(cell['frame_index'])
                        cell['frame_index'] += 1
                        if cell['frame_index'] == len(cell['animation']):
                            cell['active'] = False  # Animation completed
                    else:
                        if cell['animation'] == self.x_frames:
                            self.screen.blit(self.static_x, self.rects[row][col])
                        elif cell['animation'] == self.o_frames:
                            self.screen.blit(self.static_o, self.rects[row][col])
                        else:
                            continue

    # this method sets the animation and static image to be played when calling the above function "update_animations"
    # this way the function above knows which animation to play according to the player who made the move on the
    # specific cell
    def draw_player(self, player: Player, row, col):
        print(player.name)
        pygame.time.set_timer(self.UPDATE_ANIMATION, 50)
        if player == self.player1:
            print()

            # Blit the image onto the specified rectangle
            # self.screen.blit(self.static_x, self.rects[row][col])
            self.animation_grid[row][col]['active'] = True
            self.animation_grid[row][col]['animation'] = self.x_frames

            # self.screen.blit(self.static_x, self.rects[row][col])

        else:
            self.animation_grid[row][col]['active'] = True
            self.animation_grid[row][col]['animation'] = self.o_frames
            print()
            # self.screen.blit(self.static_o, self.rects[row][col])

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
