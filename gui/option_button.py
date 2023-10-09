import pygame
from gui.button import Button

"""
Class for a option button object which is printed on the screen and changes colour when selected
"""
class OptionButton(Button):
    def __init__(self, text, text_size, text_colour, background_colour, x, y, selected_value, width=None, height=None):
        super().__init__(text, text_size, text_colour, background_colour, x, y, width, height)
        self.selected_value = selected_value #value to be returned when this option is selected

    """
    Return the seleced value for this option button 
    """
    def get_selected_value(self):
        return self.selected_value
        
    """
    Handles events such as clicking on the button
    """
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rectangle.collidepoint(event.pos)
    