import pygame
#
# X_IMG = pygame.image.load("assets/X.png")
# O_IMG = pygame.image.load("assets/O.png")

class Player:
    def __init__(self, char: chr, png):
        self.player_char: chr = char
        self.image = png
        self.points = 0

    # def draw(self):
