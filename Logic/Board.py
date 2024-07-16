from Logic.Player import Player

EMPTY_CELL = "-"


class Board:
    def __init__(self):
        self.board_arr: [[chr]] = [[EMPTY_CELL, EMPTY_CELL, EMPTY_CELL], [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
                                   [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]]
        self.__successful_move_count = 0

    def is_legal(self, row: int, col: int) -> bool:
        if row > 2 or col > 2:
            return False
        elif row < 0 or col < 0:
            return False
        elif self.board_arr[row][col] is not EMPTY_CELL:
            return False
        else:
            return True

    def do_move(self, player: Player, row: int, col: int) -> bool:
        if self.is_legal(row, col):
            self.board_arr[row][col] = player.player_char
            self.__successful_move_count += 1
            return True
        else:
            return False

    def is_full(self) -> bool:
        return self.__successful_move_count < 9

    def has_winner(self, player1: Player, player2: Player) -> bool:
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

        # if winner was found update its points
        if winner:
            winning_player.add_point()

        return winner
