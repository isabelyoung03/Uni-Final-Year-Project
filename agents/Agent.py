from abc import abstractmethod
import config
class Agent():
    def __init__(self, x, y, maze_map):
        self.x = x #x coord for player in maze map
        self.y = y #y coord for player in maze map
        self.map = maze_map #map of the maze

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