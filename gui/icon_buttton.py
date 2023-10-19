import pygame

from gui.button import Button


class IconButton(Button):
    def __init__(self, image_name, x, y, width, height):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        file_path = "gui/resources/" + image_name
        self.image = pygame.image.load(file_path)
        self.image = pygame.transform.scale(self.image, (width, height))

    """
    Draws the button on a specfied screen
    """
    def draw(self, screen):
        screen.blit(self.image, self.rectangle)

    """
    Handles events such as clicking on the button
    """
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                return True
        return False
