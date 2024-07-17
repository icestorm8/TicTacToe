

class Player:
    def __init__(self, char: chr, name: str):
        self.player_char: chr = char
        self.__points: int = 0
        self.name: str = name

    # adds a point to the player
    def add_point(self) -> None:
        self.__points += 1

    # resets the points of the player
    def restart(self) -> None:
        self.__points = 0

    # fetches the points of the player
    def get_points(self) -> int:
        return self.__points
