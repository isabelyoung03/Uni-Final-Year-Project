from gui.button import Button
"""
A group of buttons where only one can be selected at a time
"""
class ButtonGroup():
    
    def __init__(self, buttons: list = []): 
        self.buttons = buttons

    """
    Draw each button in the group on the screen
    """
    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)
    """
    Handle events for each button - usually if they are being pressed
    """
    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)