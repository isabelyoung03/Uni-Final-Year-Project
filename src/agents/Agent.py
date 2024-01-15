from abc import abstractmethod
class Agent():
    def __init__(self, x, y, search_algorithm):
        self.x = x #x coord for player in maze map
        self.y = y #y coord for player in maze map
        self.search_algorithm = search_algorithm #search algorithm the agent follows

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

    @abstractmethod
    def execute(self, action):
        pass

    
    # @abstractmethod
    # def revise(self):
    #     pass