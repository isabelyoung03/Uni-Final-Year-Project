from abc import abstractmethod

from src.enums.action import Action
class Agent():
    def __init__(self, x, y):
        self.x = x #x coord for player in maze map
        self.y = y #y coord for player in maze map

    """
    Returns the location of the agent
    """
    def get_location(self):
        return (self.x,self.y)

    @abstractmethod
    def move_left(self):
        pass

    @abstractmethod
    def move_right(self):
        pass

    @abstractmethod
    def move_down(self):
        pass

    @abstractmethod
    def move_up(self):
        pass

    @abstractmethod
    def decide(self):
        pass

    """
    Execute specified action
    """
    def execute(self, action) -> None:
        if action == Action.DOWN:
            self.move_down()
        elif action == Action.LEFT:
            self.move_left()
        elif action == Action.RIGHT:
            self.move_right()
        elif action == Action.UP:
            self.move_up()