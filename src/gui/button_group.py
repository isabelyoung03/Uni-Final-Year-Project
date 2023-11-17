"""
A group of buttons where only one can be selected at a time
"""
class ButtonGroup():

    def __init__(self, buttons: list = []): 
        self.buttons = buttons
        self.selected_button = buttons[0]
        self.selected_button.set_selected(True)

    """
    Draw each button in the group on the screen
    """
    def draw(self, screen) -> None:
        for button in self.buttons:
            button.draw(screen)
    """
    Handle events for each button - usually if they are being pressed
    """
    def handle_event(self, event) -> None:
        for button in self.buttons:
            if button.handle_event(event):
                self.selected_button = button
                button.set_selected(True)
            if self.selected_button != button:
                button.set_selected(False)

    """
    Get the selected button from this group
    """
    def get_result(self):
        return self.selected_button.get_selected_value()