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
    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)
    """
    Handle events for each button - usually if they are being pressed
    """
    def handle_event(self, event):
        # for button in self.buttons:
        #     button.handle_event(event)


        # i = 0
        # for button in self.buttons:
        #     if button.handle_event(event):
        #         button.set_selected(True)
        #         break
        #     i += 1
        # for j in range(len(self.buttons)):
        #     if i != j:
        #         self.buttons[j].set_selected(False)

        for button in self.buttons:
                if button.handle_event(event):
                    self.set_selected(button)

        for button in self.buttons:
            if button != self.selected_button:
                button.set_selected(False)
    


    """
    Get the selected button from this group
    """
    def get_result(self):
        for button in self.buttons:
            if button.get_selected:
                print(button.get_selected_value)
                return button.get_selected_value

