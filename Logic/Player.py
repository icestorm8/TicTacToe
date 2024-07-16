

class Player:
    def __init__(self, char: chr, name: str):
        self.player_char: chr = char
        self.points = 0
        self.name = name

    def add_point(self):
        self.points += 1

