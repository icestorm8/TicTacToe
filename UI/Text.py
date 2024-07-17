import pygame


class Text:
    def __init__(self, x, y, screen, text: str, font_size: int = 30, color=(0, 0, 0)):
        self.font = pygame.font.SysFont('Berlin Sans FB', font_size)
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.text_render_rect = None

    # this function displays the text object on the screen
    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        self.text_render_rect = text_surface.get_rect(
            topleft=(self.screen.get_width() / 2 - text_surface.get_width() / 2
                     + self.x,
                     self.screen.get_height() / 2 - text_surface.get_height() /
                     2 + self.y))
        self.screen.blit(text_surface, self.text_render_rect)

    # this function checks if the mouse is hovering the text object
    def mouseover(self):
        # this function will return true if mouse is on the button
        pos = pygame.mouse.get_pos()
        if self.text_render_rect.collidepoint(pos):
            return True
        return False
    #  when getting 0 for x - sets the text horizontally centered, otherwise - goes to left or right based on x value
    #  when getting 0 for y - sets the text vertically centered, otherwise - goes to up or down based on y value
