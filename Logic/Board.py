from Logic.Player import Player

EMPTY_CELL = "-"


class Board:
    def __init__(self):
        self.board_arr: [[chr]] = [[EMPTY_CELL, EMPTY_CELL, EMPTY_CELL], [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                                   [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
        self.__successful_move_count = 0

    # checks if the move is legal or not (meaning there isn't any player who already is on the position on the board
    # or if the move is in a legal position
    def __is_legal(self, row: int, col: int) -> bool:
        if row > 2 or col > 2:
            return False
        elif row < 0 or col < 0:
            return False
        elif self.board_arr[row][col] is not EMPTY_CELL:
            return False
        else:
            return True

    # checks if the move is legal. if it is, does the move and returns that the move was successful. otherwise,
    # returns false and does nothing. anytime a move is good, the move count goes up by 1 (this helps to check if
    # the board is full without going over the entire array
    def do_move(self, player: Player, row: int, col: int) -> bool:
        if self.__is_legal(row, col):
            self.board_arr[row][col] = player.player_char
            self.__successful_move_count += 1
            return True
        else:
            return False

    # checks if the board is full
    def is_full(self) -> bool:
        return self.__successful_move_count == 9

    # checks if there was a row/col/diagonal of the same player chars on the board and returns the player if there
    # was a winner
    def has_winner(self, player1: Player, player2: Player) -> Player or None:
        winner = False
        winning_player = None
        # Check the rows
        for row in range(0, 3):
            if self.board_arr[row][0] == self.board_arr[row][1] == self.board_arr[row][2] == player1.player_char:
                winner = True
                winning_player = player1

            elif self.board_arr[row][0] == self.board_arr[row][1] == self.board_arr[row][2] == player2.player_char:
                winner = True
                winning_player = player2

        # Check the columns
        for col in range(0, 3):
            if self.board_arr[0][col] == self.board_arr[1][col] == self.board_arr[2][col] == player1.player_char:
                winner = True
                winning_player = player1
            elif self.board_arr[0][col] == self.board_arr[1][col] == self.board_arr[2][col] == player2.player_char:
                winner = True
                winning_player = player2

        # Check the diagonals
        if self.board_arr[0][0] == self.board_arr[1][1] == self.board_arr[2][2] == player1.player_char:
            winner = True
            winning_player = player1

        elif self.board_arr[0][0] == self.board_arr[1][1] == self.board_arr[2][2] == player2.player_char:
            winner = True
            winning_player = player2

        elif self.board_arr[0][2] == self.board_arr[1][1] == self.board_arr[2][0] == player1.player_char:
            winner = True
            winning_player = player1

        elif self.board_arr[0][2] == self.board_arr[1][1] == self.board_arr[2][0] == player2.player_char:
            winner = True
            winning_player = player2

        return winning_player
