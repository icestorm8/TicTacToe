

class Player:
    def __init__(self, char: chr, name: str):
        self.player_char: chr = char
        self.__points: int = 0
        self.name: str = name

    def add_point(self) -> None:
        self.__points += 1

    def restart(self) -> None:
        self.__points = 0

    def get_points(self) -> int:
        return self.__points
