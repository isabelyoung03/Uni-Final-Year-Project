import pygame

"""
Class for a button object which is printed on the screen and handles events when pressed
"""
class Button:
    def __init__(self, text, text_size, text_colour, background_colour, x, y, function, width=None, height=None):
        self.text = text
        self.text_size = text_size
        self.text_colour = text_colour
        self.background_colour = background_colour
        self.function = function
        font = pygame.font.Font('freesansbold.ttf', self.text_size)
        self.text = font.render(self.text, True, self.text_colour)
        self.button_with_backround = False
        if width == None:
            width = self.text.get_width()
            self.button_with_backround = True
        if height == None:
            height = self.text.get_height()
            self.button_with_backround = True
        self.rectangle = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y

    """
    Draws the button on a specfied screen
    """
    def draw(self, screen):
        if self.button_with_backround:
            pygame.draw.rect(screen, self.background_colour, self.rectangle)
            textRect = self.text.get_rect()
            textRect.center = (self.x, self.y)
            screen.blit(self.text, textRect)

        else:
            pygame.draw.rect(screen, self.background_colour, self.rectangle)
            text_x = self.x + (self.rectangle.width - self.text.get_width()) / 2
            text_y = self.y + (self.rectangle.height - self.text.get_height()) / 2
            textRect = self.text.get_rect()
            textRect.topleft = (text_x, text_y)
            screen.blit(self.text, textRect)

    """
    Handles events such as clicking on the button or hovering over it
    """
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                if self.function:
                    self.function()

    