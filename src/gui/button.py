import pygame
import config

"""
Class for a button object which is printed on the screen and handles events when pressed
"""
class Button:
    def __init__(self, text: str, text_size: int, text_colour, background_colour, x:int, y:int, width=None, height=None, selected_colour=config.PINK):
        self.text = text
        self.text_size = text_size
        self.text_colour = text_colour
        self.background_colour = background_colour
        self.font = pygame.font.Font('freesansbold.ttf', self.text_size)
        self.text_surface = self.font.render(self.text, True, self.text_colour)
        self.selected_text_surface = self.font.render(self.text, True, selected_colour)
        
        self.button_with_background = False
        if width == None:
            width = self.text_surface.get_width()
            self.button_with_background = True
        if height == None:
            height = self.text_surface.get_height()
            self.button_with_background = True
        self.rectangle = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y

        self.selected = False

    """
    Draws the button on a specfied screen
    """
    def draw(self, screen) -> None:
        if self.button_with_background:
            pygame.draw.rect(screen, self.background_colour, self.rectangle)
            textRect = self.text_surface.get_rect()
            textRect.center = (self.x + self.rectangle.width // 2, self.y + self.rectangle.height // 2)
        else:
            pygame.draw.rect(screen, self.background_colour, self.rectangle)
            text_x = self.x + (self.rectangle.width - self.text_surface.get_width()) / 2
            text_y = self.y + (self.rectangle.height - self.text_surface.get_height()) / 2
            textRect = self.text_surface.get_rect(topleft=(text_x, text_y))
        if self.selected:
            screen.blit(self.selected_text_surface, textRect)
        else:
            screen.blit(self.text_surface, textRect)

    """
    Handles events such as clicking on the button
    """
    def handle_event(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                self.set_selected(not self.selected)

    """
    Set if the button is selected or not, and change colour if it is
    """
    def set_selected(self, selected) -> None:
        self.selected = selected

    """
    Get if the button is selected or not
    """
    def get_selected(self) -> bool:
        return self.selected
        

    