from gui.button import Button
"""
A group of buttons where only one can be selected at a time
"""
class ButtonGroup():
    def __init__(self, buttons: list = []): 
        self.buttons = buttons

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)