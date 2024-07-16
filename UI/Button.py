import pygame


class Button:
    def __init__(self, x, y, width: int, height: int, text: str = '', font_size: int = 30):
        self.rect = None
        self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text: str = text
        self.font_size: int = font_size
        self.font = pygame.font.SysFont('Berlin Sans FB', font_size)

    # this method draws the button on the screen it got as parameter & there's an option for adding an outline
    # it is the displaying of the button that was set when created
    def draw(self, screen, outline=False):
        self.x = screen.get_width()/2 - self.x - self.width / 2
        self.y = screen.get_height()/2 - self.y

        if outline:
            self.rect = pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))

        self.rect = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comics', self.font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 -
                                                                                           text.get_height() / 2)))

    # this method is used to check if the mouse is over the button using the mouse current position and rect
    # collide point on that position
    def mouseover(self):
        # this function will return true if mouse is on the button
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        return False
