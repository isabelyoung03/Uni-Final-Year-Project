import pygame

from src.gui.button import Button


class IconButton(Button):
    def __init__(self, image_name, x, y, width, height, visibility):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.visibility = visibility
        file_path = "src/gui/resources/" + image_name
        self.image = pygame.image.load(file_path)
        self.image = pygame.transform.scale(self.image, (width, height))

    """
    Draws the button on a specfied screen
    """
    def draw(self, screen) -> None:
        if self.visibility:
            screen.blit(self.image, self.rectangle)

    """
    Handles events such as clicking on the button
    """
    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and self.visibility:
            if self.rectangle.collidepoint(event.pos):
                return True
        return False
    
    """
    Change the visibility of the button
    """
    def toggle(self, toggled) -> None:
        self.visibility = not toggled

    """
    Return the visibility of the button
    """
    def get_toggled(self) -> bool:
        return not self.visibility