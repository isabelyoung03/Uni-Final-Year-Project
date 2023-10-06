import pygame

"""
Class for a button object which is printed on the screen and handles events when pressed
"""
class Button:
    def __init__(self, text, text_size, text_colour, background_colour, x, y, width, height, function):
        self.text = text
        self.text_size = text_size
        self.text_colour = text_colour
        self.background_colour = background_colour
        self.function = function
        self.rectangle = pygame.Rect(x, y, width, height)
        font = pygame.font.Font('freesansbold.ttf', self.text_size)
        self.text = font.render(self.text, True, self.text_colour)

    def __init__(self, text, text_size, text_colour, background_colour, x, y, function):
        self.text = text
        self.text_size = text_size
        self.text_colour = text_colour
        self.background_colour = background_colour
        self.function = function
        font = pygame.font.Font('freesansbold.ttf', self.text_size)
        self.text = font.render(self.text, True, self.text_colour)
        width = self.text.get_width()
        height = self.text.get_height()
        self.rectangle = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_colour, self.rectangle)
        textRect = self.text.get_rect()
        textRect.center = (self.x, self.y)
        screen.blit(self.text, textRect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                if self.function:
                    self.function()

    